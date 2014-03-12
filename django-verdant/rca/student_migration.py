from django.utils.text import slugify
from itertools import chain
import re
from wagtail.wagtailcore.models import Page
from rca.models import (
    StudentPage, NewStudentPage,

    NewStudentPagePreviousDegree,
    NewStudentPageExhibition,
    NewStudentPageExperience,
    NewStudentPageContactsEmail,
    NewStudentPageContactsPhone,
    NewStudentPageContactsWebsite,
    NewStudentPagePublication,
    NewStudentPageConference,
    NewStudentPageAwards,
    NewStudentPageShowCarouselItem,
    NewStudentPageShowCollaborator,
    NewStudentPageShowSponsor,
    NewStudentPageResearchCarouselItem,
    NewStudentPageResearchAwards,
    NewStudentPageResearchCollaborator,
    NewStudentPageResearchSponsor,
    NewStudentPageResearchSupervisor,
)


class StudentPageProxy(StudentPage):
    class Meta:
        proxy = True

    @property
    def is_research_page(self):
        return self.degree_qualification in ['mphil', 'phd', 'researchstudent', 'innovationrca-fellow']

    @property
    def is_ma_page(self):
        return self.degree_qualification == 'ma'

    @property
    def is_in_show(self):
        return self.get_parent().id == 5255

    @property
    def is_in_rcanow(self):
        return self.get_parent().id == 36


class StudentMigration(object):
    def __init__(self, save=False, index_page=None):
        self.save = save
        self.skipped_students = []
        self.index_page = Page.objects.get(pk=index_page) if index_page else None

    def migrate_page(self, new_page, page):
        # General info
        new_page.first_name = page.first_name
        new_page.last_name = page.last_name
        new_page.profile_image = page.profile_image
        new_page.statement = page.statement
        #twitter_handle
        new_page.funding = page.funding
        new_page.feed_image = page.feed_image
        new_page.show_on_homepage = page.show_on_homepage

        # Show info
        new_page.show_work_type = page.work_type
        new_page.show_work_location = page.work_location
        new_page.show_work_description = page.work_description

        # MA info
        if page.is_ma_page:
            new_page.ma_school = page.school
            new_page.ma_programme = page.programme
            new_page.ma_graduation_year = page.graduation_year or page.degree_year
            new_page.ma_specialism = page.specialism
            new_page.ma_in_show = page.is_in_show

        # Research info
        if page.is_research_page:
            new_page.research_school = page.school
            new_page.research_programme = page.programme
            new_page.research_start_year = page.degree_year
            new_page.research_graduation_year = page.graduation_year
            new_page.research_qualification = page.degree_qualification
            #research_dissertation_title
            #research_statement
            new_page.research_in_show = page.is_in_show

        # General child objects
        for degree in page.degrees.all():
            new_page.previous_degrees.add(NewStudentPagePreviousDegree(degree=degree.degree))

        for exhibition in page.exhibitions.all():
            new_page.exhibitions.add(NewStudentPageExhibition(exhibition=exhibition.exhibition))

        for experience in page.experiences.all():
            new_page.experiences.add(NewStudentPageExperience(experience=experience.experience))

        for email in page.email.all():
            new_page.emails.add(NewStudentPageContactsEmail(email=email.email))

        for phone in page.phone.all():
            new_page.phones.add(NewStudentPageContactsPhone(phone=phone.phone))

        for website in page.website.all():
            new_page.websites.add(NewStudentPageContactsWebsite(website=website.website))

        for publication in page.publications.all():
            new_page.publications.add(NewStudentPagePublication(name=publication.name))

        for conference in page.conferences.all():
            new_page.conferences.add(NewStudentPageConference(name=conference.name))

        for award in page.awards.all():
            new_page.awards.add(NewStudentPageAwards(award=award.award))

        for supervisor in page.supervisors.all():
            new_page.research_supervisors.add(NewStudentPageResearchSupervisor(supervisor=supervisor.supervisor, supervisor_other=supervisor.supervisor_other))

        # Move carousel items/collaborators/sponsors to research if this is a research student
        if page.is_research_page:
            for carousel_item in page.carousel_items.all():
                new_page.research_carousel_items.add(NewStudentPageResearchCarouselItem(
                    image=carousel_item.image,
                    overlay_text=carousel_item.overlay_text,
                    link=carousel_item.link,
                    link_page=carousel_item.link_page,
                    embedly_url=carousel_item.embedly_url,
                    poster_image=carousel_item.poster_image,
                ))

            for collaborator in page.collaborators.all():
                new_page.research_collaborators.add(NewStudentPageResearchCollaborator(name=collaborator.name))

            for sponsor in page.sponsor.all():
                new_page.research_sponsors.add(NewStudentPageResearchSponsor(name=sponsor.name))

        # If this is not a research student, move carousel items/collaborators/sponsors to show
        if not page.is_research_page:
            for carousel_item in page.carousel_items.all():
                new_page.show_carousel_items.add(NewStudentPageShowCarouselItem(
                    image=carousel_item.image,
                    overlay_text=carousel_item.overlay_text,
                    link=carousel_item.link,
                    link_page=carousel_item.link_page,
                    embedly_url=carousel_item.embedly_url,
                    poster_image=carousel_item.poster_image,
                ))

            for collaborator in page.collaborators.all():
                new_page.show_collaborators.add(NewStudentPageShowCollaborator(name=collaborator.name))

            for sponsor in page.sponsor.all():
                new_page.show_sponsors.add(NewStudentPageShowSponsor(name=sponsor.name))

    def migrate_student(self, name, page):
        # Create new page
        new_page = NewStudentPage()
        new_page.title = name
        new_page.slug = slugify(name)
        new_page.live = page.live
        new_page.has_unpublished_changes = not new_page.live

        # Migrate old page
        self.migrate_page(new_page, page)

        # Save new page
        if self.save and self.index_page:
            self.index_page.add_child(new_page)
            new_page.save_revision()

    def run(self):
        # Couple of regexes for cleaning titles
        multi_space = re.compile(' +')
        start_space = re.compile('^ +')
        end_space = re.compile(' +$')

        # Get students
        students = {}
        for student in StudentPageProxy.objects.all():
            name = student.title

            # Some student pages have a suffix, remove the suffix
            bad_suffixes = [', PhD', ', MPhil', ' MA', ' PhD', ' CX PhD Candidate']
            for bad_suffix in bad_suffixes:
                if name.endswith(bad_suffix):
                    name = name[:-len(bad_suffix)]

            # Some student pages contain extra spaces
            name = multi_space.sub(' ', name)
            name = start_space.sub('', name)
            name = end_space.sub('', name)

            # Put the student page in the students mapping
            if name in students.keys():
                students[name].append(student)
            else:
                students[name] = [student]

        # Migrate each one
        for student, pages in students.items():
            # Skip if this student has multiple pages
            if len(pages) > 1:
                self.skipped_students.append(student)
                continue

            # Migrate student
            self.migrate_student(student, pages[0])


def run(*args, **kwargs):
    sm = StudentMigration(*args, **kwargs)
    sm.run()

    print repr(sm.skipped_students)
