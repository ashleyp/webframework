# Specify modules to import, functions to import, routes to match.

views = (
    'forum.views',
    'forum.test_views',
)

urls = (  
    ('/', 'index'),
    ('/testing', 'testing'),
    ('/peanut/butter', 'peanut'),
)
