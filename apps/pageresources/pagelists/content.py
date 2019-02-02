"""
    List of Content Type Categories
    Think of content categories as the types of textual content in the application,
    such as titles, headings, descriptions, labels, buttons, lists.
    Content type categories must be defined here to help identify page resources for
    language translation services, and to populate the page content.

    Content types will be assigned to a component (or view).
    A component may have many content types, and even many of the same content types.

    The keys identified below generally follow the pattern: first letter + first consonant.
    Keys, however, must be unique.
"""

BUTTON = 'bt'
DESCRIPTION = 'ds'  # E.g., page text; lower order than heading
HEADING = 'hd'      # E.g., section heading; lower order than title
HELPTEXT = 'hl'     # E.g., help text on hover
LABEL = 'lb'        # E.g., input field label
LIST = 'ls'
OPTION = 'op'       # E.g., option default text in drop down option field
PLACEHOLDER = 'pl'  # E.g., default placeholder in input field
TITLE = 'tt'        # Page title; higher order than heading

CONTENT_CHOICES = [
    (BUTTON, 'Button'),
    (DESCRIPTION, 'Description'),
    (HEADING, 'Heading'),
    (HELPTEXT, 'Help Text'),
    (LABEL, 'Label'),
    (LIST, 'List'),
    (OPTION, 'Option'),
    (PLACEHOLDER, 'Placeholder'),
    (TITLE, 'Title')
]

CONTENT_KEYS = [content[0] for content in CONTENT_CHOICES]
CONTENT_NAMES = [content[1] for content in CONTENT_CHOICES]