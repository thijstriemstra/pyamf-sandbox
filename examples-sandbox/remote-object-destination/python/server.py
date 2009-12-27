#!/usr/bin/python

class RemoteObjectService:
    def hello(self):
        return 'hello world'

services = {
    'RemoteObjectService': RemoteObjectService()
}

if __name__ == '__main__':
    from pyamf.remoting.gateway.wsgi import WSGIGateway
    from wsgiref import simple_server

    gw = WSGIGateway(services)

    httpd = simple_server.WSGIServer(
        ('localhost', 8000),
        simple_server.WSGIRequestHandler,
    )

    httpd.set_app(gw)

    print "Running AMF gateway on http://localhost:8000"

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
