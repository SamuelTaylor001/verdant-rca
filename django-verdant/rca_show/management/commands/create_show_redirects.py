import re

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from wagtail.wagtailredirects.models import Redirect

from rca_show.models import ShowIndexPage


SUB_EXPRESSIONS = (
    # Removes '/' characters
    (r'\/', ''),

    # Removes multiple spaces
    (r' +', ' '),

    # Removes leading spaces
    (r'^ ', ''),

    # Removes trailing spaces
    (r' $', ''),

    # Removes spaces around hyphens
    (r' - ', '-'),

    # Converts spaces to hyphens
    (r' ', '-'),
)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('show_index_id', type=int)

    def handle(self, show_index_id, **options):
        # Find show index page
        show_index = ShowIndexPage.objects.get(id=show_index_id)

        sub_expressions_compiled = [(re.compile(sub_expr[0]), sub_expr[1]) for sub_expr in SUB_EXPRESSIONS]

        for student in show_index.get_students():
            # Work out a URL to redirect from
            name = student.title

            for sub_expr in sub_expressions_compiled:
                name = sub_expr[0].sub(sub_expr[1], name)

            from_url = 'show2018/' + slugify(name) + '/'

            # Find students url inside
            if show_index.is_programme_page:
                to_url = show_index.reverse_subpage('student', programme_slug=student.programme.slug, slug=student.slug)
            else:
                to_url = show_index.reverse_subpage('student', school_slug=student.school.slug, programme_slug=student.programme.slug, slug=student.slug)

            # Normalise the URL
            from_url_normalised = Redirect.normalise_path(from_url)

            # Create the redirect
            redirect, created = Redirect.objects.get_or_create(old_path=from_url_normalised, defaults={'redirect_link': to_url})

            # Print message
            if created:
                print "Created redirect: " + from_url_normalised + " to: " + to_url + " for student: " + student.title + " (" + str(student.id) + ")"
