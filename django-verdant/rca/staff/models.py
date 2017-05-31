from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.views.decorators.vary import vary_on_headers
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from rca.models import StaffPage
from rca.utils.models import SocialFields


# TODO: Move StaffPage, StaffIndexPage and all related models here

@register_snippet
class AreaOfExpertise(models.Model):
    name = models.CharField(max_length=128)

    panels = [
        FieldPanel('name'),
    ]

    def __unicode__(self):
        return self.name


class ExpertsIndexPage(Page, SocialFields):
    intro = RichTextField(blank=True)
    twitter_feed = models.CharField(max_length=255, blank=True,
                                    help_text="Replace the default Twitter feed by providing an alternative "
                                              "Twitter handle (without the @ symbol)")
    feed_image = models.ForeignKey('rca.RcaImage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                                   help_text="The image displayed in content feeds, such as the news carousel. "
                                             "Should be 16:9 ratio.")
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('twitter_feed'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('slug'),
        ], 'Common page configuration'),

        MultiFieldPanel([
            FieldPanel('show_in_menus'),
            ImageChooserPanel('feed_image'),
            FieldPanel('search_description'),
        ], 'Cross-page behaviour'),

        MultiFieldPanel([
            ImageChooserPanel('social_image'),
            FieldPanel('social_text'),
        ], 'Social networks'),
    ]

    ajax_template = 'staff/experts_index_page_listing.html'

    @vary_on_headers('X-Requested-With')
    def serve(self, request, *args, **kwargs):
        return super(ExpertsIndexPage, self).serve(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        # Get all live and public expert pages
        staff_pages = StaffPage.objects.live().public().filter(is_expert=True)

        # Allow to filter by Area of expertise
        try:
            selected_area_of_expertise_pk = int(request.GET.get('area_of_expertise'))

            staff_pages = staff_pages.filter(
                areas_of_expertise__area_of_expertise__pk=selected_area_of_expertise_pk
            )

            # We have to do that because Wagtail doesn't support filtering
            # on related fields, at the moment.
            staff_pages = StaffPage.objects.filter(pk__in=[page.pk for page in staff_pages])
        except (ValueError, TypeError):
            # area_of_expertise is invalid or not present in a request
            selected_area_of_expertise_pk = None

        # Search
        query_string = request.GET.get('q')
        if query_string:
            staff_pages = staff_pages.search(query_string, operator='and')

        # Paginate
        paginator_page_size = 20
        paginator = Paginator(staff_pages, paginator_page_size)
        try:
            staff_pages = paginator.page(request.GET.get('p'))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            staff_pages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            staff_pages = paginator.page(paginator.num_pages)

        # Get all Areas of expertise for filtering UI
        all_areas_of_expertise = AreaOfExpertise.objects.all().values_list('pk', 'name')

        filters = [
            {
                'name': 'area_of_expertise',
                'current_value': selected_area_of_expertise_pk,
                'options': [''] + list(all_areas_of_expertise.values_list('pk', flat=True)),
            },
        ]

        context = super(ExpertsIndexPage, self).get_context(request, *args, **kwargs)
        context.update({
            'search_results': staff_pages,
            'paginator_page_size': paginator_page_size,
            'query_string': query_string,
            'selected_area_of_expertise_pk': selected_area_of_expertise_pk,
            'filters': filters,
            'all_areas_of_expertise': all_areas_of_expertise,
        })

        return context