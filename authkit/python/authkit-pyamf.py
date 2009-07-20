#!/usr/bin/env python

"""
This code demonstrates some of the features of authkit.authorize in combination
with PyAMF.
"""

import os.path
import logging

from authkit.permissions import UserIn
from authkit.authorize import authorized, authorize, PermissionError
from authkit.authorize import middleware as authorize_middleware

from paste import httpexceptions

from pyamf.remoting.gateway.wsgi import WSGIGateway


# Host and port to run the server on
host_info = ('localhost', 8080)

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')

# users allowed to access the gateway
my_users = ['nick']


class AuthService(object):
    """
    Provide a simple server for testing.
    """
    def valid(self, environ, username, password):
        """
        Sample, very insecure validation function
        """
        return username == password
    
    def auth(self, username, password):
        return username == password

    @authorize(UserIn(users=my_users))
    def echo(self, data):
        """
        Return data with greeting.
        """
        return 'Hello %s!' % data


class NoSuchActionError(httpexceptions.HTTPNotFound):
    pass


class AuthorizeExampleApp(object):
    def __call__(self, environ, start_response):
        if environ['PATH_INFO'] == '/':
            method = 'index'
        elif environ['PATH_INFO'].startswith('/assets/'):
            method = 'assets'
        else:
            method = environ['PATH_INFO'].split('/')[1]
        if not hasattr(self, method):
            raise NoSuchActionError('No such method')

        app = getattr(self,method)

        # This facilitates an alternative way you might want to check permisisons
        # rather than using an authorize() decorator
        if hasattr(app, 'permission'):
            app = authorize_middleware(app, app.permission)

        return app(environ, start_response) 

    def index(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/html')])
        file = open('index.html', 'r')
        result = [file.read()]
        
        return result

    def assets(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/html')])
        path = os.path.basename(environ['PATH_INFO'])
        file = open('assets/%s' % path, 'r')
        result = [file.read()]
        
        return result

    @authorize(UserIn(users=my_users))
    def gateway(self, environ, start_response):
        """
        Authorize using a decorator
        """
        return gw(environ, start_response)


if __name__ == '__main__':
    from paste.httpserver import serve
    from authkit.authenticate import middleware

    realm = 'Test Realm'
    service = AuthService()
    
    # Configure the remoting services
    services = {
        'auth.echo': service.echo
    }

    gw = WSGIGateway(services, logger=logging)

    app = httpexceptions.make_middleware(AuthorizeExampleApp())
    app = middleware( app, setup_method='basic', basic_realm=realm, 
                      basic_authenticate_function=service.valid
    )

    print """
Clear the HTTP authentication first by closing your browser if you have been
testing other basic authentication examples on the same port.

All users apart from `nick' (with password 'nick') will be denied access to the
resources.
"""

    serve(app, host=host_info[0], port=host_info[1])
