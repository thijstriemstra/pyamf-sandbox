from pyamf import register_class

import model

session = model.Session()

class CustomerService(object):
    def getCategories(self):
        """
        Returns all the categories
        """
        return session.query(model.Category).all()

if __name__ == '__main__':
    from pyamf.gateway.wsgi import WSGIGateway
    from wsgiref import simple_server

    gw = WSGIGateway({'service': CustomerService})

    httpd = simple_server.WSGIServer(
        ('127.0.0.1', 8000),
        simple_server.WSGIRequestHandler,
    )

    httpd.set_app(gw)

    httpd.serve_forever()
