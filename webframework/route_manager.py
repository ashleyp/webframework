from settings.urls import urls

class routeManager:
    routes = {}

    def __init__(self, module):
        self.update_routes()

    def update_routes(self):
        for url in urls:
            prefix = url[0]
            module = url[1]
            loaded_module = __import__(module, globals(), locals(), ['urls', 'views'], -1)
            for view_module in loaded_module.views:
                print "loaded routes from: %s" % view_module
                exec("import " + view_module + " as temp")
                for tup in loaded_module.urls:
                   route = tup[0]
                   func  = tup[1]
                   try: # if function is not in module, ignore and continue.
                       self.routes[prefix + route] = getattr(temp, func)
                   except:
                       pass
