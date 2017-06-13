import random
from django import template
from rca_show import models
from rca import models as rca_models

register = template.Library()


@register.simple_tag
def show_subpage_url(show_index, name, *args, **kwargs):
    if show_index.is_programme_page and name in ['student', 'programme'] and 'school_slug' in kwargs:
        del kwargs['school_slug']

    return show_index.reverse_subpage(name, *args, **kwargs)


@register.simple_tag
def get_programme_display(programme):
    return programme.display_name


@register.simple_tag
def get_school_display(school):
    # TODO: Historical display name
    return school.display_name


SCHOOL_LOGOS_2016 = {
    'schoolofcommunication': 'rca_show/images/logo-2016-1.svg',
    'schoolofhumanities': 'rca_show/images/logo-2016-2.svg',
    'schooloffineart': 'rca_show/images/logo-2016-3.svg',
    'schoolofmaterial': 'rca_show/images/logo-2016-4.svg',
    'schoolofdesign': 'rca_show/images/logo-2016-5.svg',
    'schoolofarchitecture': 'rca_show/images/logo-2016-6.svg',
}
@register.assignment_tag
def get_school_logo_2016(school):
    """
    For a given school identifier, find the filename of the top bar logo for that school.

    This is to make the logo selection easier for the dynamic logo that should appear for each school. If no
    school is selected, the regular show-wide logo is returned.
    """
    if not school or school.slug not in SCHOOL_LOGOS_2016:
        return 'rca_show/images/logo-2016.svg'

    return SCHOOL_LOGOS_2016[school.slug]

@register.assignment_tag
def get_schools(show_index):
    if show_index is None:
        return []

    return show_index.get_schools()


@register.assignment_tag
def get_school_programmes(show_index, school):
    if show_index is None:
        return []

    return show_index.get_school_programmes(school)


@register.assignment_tag
def get_school_students(show_index, school, random = False):
    if show_index is None:
        return []

    if random:
        return show_index.get_rand_students(school=school)
    else:
        return show_index.get_students(school=school)


@register.assignment_tag
def get_programme_students(show_index, programme, random = False):
    if show_index is None:
        return []
    if random:
        return show_index.get_rand_students(programme=programme)
    else:
        return show_index.get_students(programme=programme)

@register.assignment_tag
def get_programme_works(show_index, programme):
    # Instead of getting a list of students (get_programme_students),
    # this gets the same list of students but ordered by their dissertation/work title
    if show_index is None:
        return []
    else:
        return show_index.get_students(programme=programme, orderby="show_work_title")

@register.assignment_tag
def randsize(rangeStart, rangeEnd):
    return random.randrange(rangeStart, rangeEnd)


@register.assignment_tag
def secondary_menu(calling_page=None):
    pages = []
    if calling_page:
        pages = calling_page.menu_items

    return pages


@register.assignment_tag
def get_maps_for_campus(campus):
    maps = models.ShowExhibitionMapPage.objects.filter(live=True, campus=campus)

    return maps


@register.assignment_tag
def get_school_for_programme(programme):
    return programme.school
