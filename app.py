from wsgiref.simple_server      import make_server
from webframework.route_manager import routeManager

class application:

    routeManager = routeManager('urls')
    loadedUrls   = routeManager.routes

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        print environ['PATH_INFO']

    def __iter__(self):
        result = self.url_match()
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        return iter(result)

    def url_match(self):
        url = self.environ['PATH_INFO']
        if self.loadedUrls.has_key( url ):
            return self.loadedUrls[url]()
        else:
            return self.notfound()

    def notfound(self):
        yield "Not Found\n"


httpd = make_server( 'localhost', 5000, application )
print 'running on port 5000...'

httpd.serve_forever()

