"""
Hello world example server for Apache Ant.
"""

def echo(data):
    """
    Just return data back to the client.
    """
    return data


if __name__ == '__main__':
    import os, sys
    import logging
    from pyamf.remoting.gateway.wsgi import WSGIGateway
    from wsgiref import simple_server

    logging.basicConfig(level=logging.DEBUG,
           format='%(asctime)s %(levelname)-5.5s %(message)s')

    services = {
        'echo.echo': echo
    }

    gw = WSGIGateway(services, logger=logging, debug=True)

    httpd = simple_server.WSGIServer(
        ('localhost', 8000),
        simple_server.WSGIRequestHandler,
    )

    httpd.set_app(gw)

    logging.info("Running Ant AMF gateway on http://localhost:8000")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

