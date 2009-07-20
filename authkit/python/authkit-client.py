"""
Hello world example client for Authkit.
"""

import base64

from pyamf.remoting import RemotingError
from pyamf.remoting.client import RemotingService

import logging
logging.basicConfig(level=logging.INFO,
           format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')


username = 'nick'
password = 'nick'

realm = 'Test Realm'
credentials = base64.encodestring('%s:%s' % (username, password))[:-1]

url = 'http://localhost:8080/gateway'
client = RemotingService(url, logger=logging)
client.addHTTPHeader("WWW-Authenticate", 'Basic realm="%s"' % realm)
client.addHTTPHeader("Authorization", 'Basic %s' % credentials)

service = client.getService('auth.echo')

try:
    result = service('Hello world!')
except RemotingError, e:
    result = "Incorrect username/password!"

logging.info(result)
