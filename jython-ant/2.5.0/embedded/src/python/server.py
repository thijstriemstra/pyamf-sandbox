"""
Hello world example server.
"""

def echo(data):
    """
    Just return data back to the client.
    """
    return data

services = {
    'echo.echo': echo
}

if __name__ == '__main__':
    import os
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

