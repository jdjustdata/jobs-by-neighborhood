"""
    List of View Components
    Think of components as major sections, pages, or areas of the application.
    Components must be defined here to identify the page resource location used for
    language translation services, and to populate the page content.

    The keys identified below generally follow the pattern: first letter + first consonant.
    Keys, however, must be unique.
"""

ABOUT = 'ab'
ADMINISTRATION = 'ad'
ANALYTICS = 'an'
BUSINESSES = 'bs'
GEOGRAPHY = 'gg'
JOBS = 'jb'
MENUBAR = 'mn'
USERS = 'us'

COMPONENT_CHOICES = [
    (ABOUT, 'About'),
    (ADMINISTRATION, 'Administration'),
    (ANALYTICS, 'Analytics'),
    (BUSINESSES, 'Business'),
    (JOBS, 'Jobs'),
    (MENUBAR, 'Menubar'),
    (USERS , 'Users')
]

COMPONENT_KEYS = [component[0] for component in COMPONENT_CHOICES]
COMPONENT_NAMES = [component[1] for component in COMPONENT_CHOICES]