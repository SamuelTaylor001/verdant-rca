from collections import defaultdict
from optparse import make_option

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, get_page_models

HEADING_TAGS = [
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
]

TAGS_REMOVE_EMPTY = ["a"] + HEADING_TAGS

VOID_ELEMENTS = [
    "br",
    "embed",
    "hr",
    "img",
]

TEST_HTML = '''
<h1 class="empty-heading"></h1>
<h2 class="empty-heading"></h2>
<h3 class="empty-heading"></h3>
<h4 class="empty-heading"></h4>
<h5 class="empty-heading"></h5>
<h6 class="empty-heading"></h6>

<h1>has some text content</h1>
<h2>has some text content</h2>
<h3>has some text content</h3>
<h4>has some text content</h4>
<h5>has some text content</h5>
<h6>has some text content</h6>

<h1 class="heading-with-void"><img src="http://imagesource.com" /></h1>
<h2 class="heading-with-void"><embed alt="An example wagtail embed" embedtype="image" /></h2>
<h3 class="heading-with-void"><br/><h3>
<h4 class="heading-with-void"><hr/><h4>
'''


def tag_has_no_text(tag):
    return len(tag.get_text(strip=True)) == 0


def tag_has_void_elements(tag):
    return tag.find_all(VOID_ELEMENTS)


# TODO: is there a cleaner way to make sure html, head and body
# are not appended to richtext html?
def remove_html_wrappers(soup):
    soup.body.unwrap()
    soup.html.unwrap()
    soup.head.decompose()


def get_class_richtext_fields(page_class):
        return [
            f.name for f in page_class._meta.fields
            if issubclass(f.__class__, RichTextField)
        ]


def list_all_page_type_richtext_fields():
    for content_class in get_page_models():
        richtext_fields = get_class_richtext_fields(content_class)
        if richtext_fields:
            print(content_class.__name__)
            for f in richtext_fields:
                print("    " + f)


# WARNING: for development use only
def get_single_example_page():
    # return Page.objects.get(pk=18797).specific
    return Page.objects.get(pk=17272).specific


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--fix',
            action='store_true',
            dest='fix',
            default=False,
            help="Fix any issues found by this script"
        ),
        make_option('--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help="Fix any issues found by this script"
        ),
        make_option('--list-fields',
            action='store_true',
            dest='list_fields',
            default=False,
            help="Fix any issues found by this script"
        ),
        make_option(
            '--limit',
            dest='limit',
            default=None,
            help="Limit number of pages sanitised."
        ),
        make_option('--csv',
            action='store_true',
            dest='csv',
            default=False,
            help="Output the resulting alterations in CSV format."
        ),
    )

    def __init__(self):
        self.tags_removed = defaultdict(dict)
        self.tags_unwrapped = defaultdict(dict)
        self.pages_processed = 0

    def log_alterations(self, page_id, field, tags_removed, tags_unwrapped):
        if tags_removed:
            self.tags_removed[page_id][field] = tags_removed
            # if self.tags_removed.get(page_id, None):
            # else:
            #     self.tags_removed[page_id] = {field: tags_removed}
        if tags_unwrapped:
            if self.tags_unwrapped.get(page_id, None):
                self.tags_unwrapped[page_id][field] = tags_unwrapped
            else:
                self.tags_unwrapped[page_id] = {field: tags_unwrapped}

    def remove_empty_tags(self, page, field):
        html = getattr(page, field)
        soup = BeautifulSoup(html, "html5lib")
        potentially_empty_tags = soup.find_all(TAGS_REMOVE_EMPTY)

        tags_removed = []
        tags_unwrapped = []

        for tag in potentially_empty_tags:
            if tag_has_no_text(tag):
                if not tag.descendants:
                    # Its genuinely empty so can remove
                    tags_removed.append(str(tag))
                    tag.decompose()
                elif tag.name in HEADING_TAGS:
                    if tag_has_void_elements(tag):
                        # This is a heading that contains a void element ie img/embed
                        # so just remove wrapping heading element
                        tags_unwrapped.append(str(tag))
                        tag.unwrap()
                    else:
                        # Heading has valid descendants but no text to display
                        tags_removed.append(str(tag))
                        tag.decompose()

        self.log_alterations(page.id, field, tags_removed, tags_unwrapped)

        remove_html_wrappers(soup)

        self.pages_processed += 1
        return str(soup)

    def handle(self, options):
        list_fields = options["list_fields"]
        verbose = options["verbose"]
        limit = options["limit"]
        csv = options["csv"]
        # if csv:
        #     verbose = False

        # List the rich text fields on each page type
        # instead of processing (debugging)
        if list_fields:
            list_all_page_type_richtext_fields()
            return

        # Iterate through all page types and process their richtext fields
        for content_class in get_page_models():
            richtext_fields = get_class_richtext_fields(content_class)
            pages = content_class.objects.public().live().specific()

            if limit:
                pages = pages[:limit]
            if verbose:
                print("{}: {}".format(
                    content_class.__name__,
                    str(richtext_fields))
                )

            for page in pages:
                if verbose:
                    print("page {}".format(page.id))

                for field in richtext_fields:
                    self.remove_empty_tags(page, field)

        # if verbose:
        #     print("=====================")
        print("{} pages were processed".format(self.pages_processed))
        print("Tags were removed from richtext on {} pages".format(
            len(self.tags_removed))
        )

        if csv:
            import csv

            # TODO: This may need to be output to standard out or to S3
            # Unless the migration is done locally and then db switched.
            with open("richtext_tag_removals.csv", "wb") as f:
                w = csv.writer(f)
                w.writerow(['Page ID', 'Rich Text Field', 'Tags Removed'])
                page_tags = self.tags_removed
                fields = page_tags.values()[0].keys()
                for page_id in page_tags.keys():
                    try:
                        w.writerow([page_id] + [field] + [page_tags[page_id][field] for field in fields])
                    except KeyError:
                        pass

            with open("richtext_tag_unwraps.csv", "wb") as f:
                w = csv.writer(f)
                w.writerow(['Page ID', 'Rich Text Field', 'Tags Unwrapped'])
                page_tags = self.tags_unwrapped
                fields = page_tags.values()[0].keys()
                for page_id in page_tags.keys():
                    try:
                        w.writerow([page_id] + [field] + [page_tags[page_id][field] for field in fields])
                    except KeyError:
                        pass
