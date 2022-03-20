
from werkzeug.wrappers import Request, Response


class APIServer():

    def wsgi_app(self, environ, start_response):
        req    = Request(environ)
        path   = environ.get('PATH_INFO')
        output = ""
        #
        # http://localhost:9000/hello?name=world
        if path == "/hello":
            if "name" in req.args.keys():
                output = "Hello " + req.args["name"]
        response = Response(output.encode(), mimetype="text/plain")
        return response(environ, start_response)
    
    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def main(): 
    from werkzeug.serving import run_simple
    app = APIServer()
    run_simple('localhost', 9000, app)
    

if __name__ == '__main__':
    main()