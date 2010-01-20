#!/usr/bin/env python
#
# Copyright (c) 2009 The PyAMF Project.
# See LICENSE.txt for details.

"""
Example client for Authkit.
"""

import base64

from server import host_info

from pyamf.remoting import RemotingError
from pyamf.remoting.client import RemotingService

import logging
logging.basicConfig(level=logging.DEBUG,
           format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-p", "--port", default=host_info[1],
    dest="port", help="Port number [default: %default]")
parser.add_option("-c", "--host", default=host_info[0],
    dest="host", help="Host address [default: %default]")
parser.add_option("-u", "--username", default="nick",
    dest="username", help="Password [default: %default]")
parser.add_option("-k", "--password", default="nick",
    dest="password", help="Username [default: %default]")
parser.add_option("-r", "--realm", default=host_info[2],
    dest="realm", help="Realm [default: %default]")
(opt, args) = parser.parse_args()


realm = opt.realm
credentials = base64.encodestring('%s:%s' % (opt.username, opt.password))[:-1]

logging.debug('Realm: %s' % opt.realm)
logging.debug('Username: %s' % opt.username)
logging.debug('Password: %s' % opt.password)

url = 'http://%s:%d/gateway' % (opt.host, int(opt.port))
client = RemotingService(url, logger=logging)
client.addHTTPHeader("WWW-Authenticate", 'Basic realm="%s"' % realm)
client.addHTTPHeader("Authorization", 'Basic %s' % credentials)

service = client.getService('auth.echo')

try:
    result = service('Hello world!')
except RemotingError, e:
    result = "Incorrect username/password!"

logging.info(result)
