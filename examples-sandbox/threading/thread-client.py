#!/usr/bin/python

"""
AMF test client for new multiprocessing module in Python 2.6
"""

import logging

from pyamf.remoting.client import RemotingService

from service import SharedObject

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
)

client = RemotingService('http://localhost:8000')
service = client.getService('echo')

result = service('hello world!')

print result
