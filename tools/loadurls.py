from settings.urls import urls

routes = {}

for url in urls:
    prefix = url[0]
    module = url[1]
    blah = __import__(module, globals(), locals(), ['urls', 'views'], -1)
    for view_module in blah.views:
        print view_module
        exec("import " + view_module + " as forum")
        for tup in blah.urls:
           route = tup[0]
           func  = tup[1]
           try:
               routes[prefix + route] = getattr(forum, func)
           except AttributeError:
               pass

for key,value in routes.items():
    print value()
