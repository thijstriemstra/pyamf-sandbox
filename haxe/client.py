#!/usr/bin/python

# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Example client for haXe/Python communication using AMF.

@author: U{Thijs Triemstra<mailto:info@collab.nl>}
@since: 0.3.1
"""
import logging
from pyamf.remoting.client import RemotingService

gateway = RemotingService('http://localhost/gateway/haxe')
gateway.logger.setLevel(logging.DEBUG)

haxe_service = gateway.getService('foo')

print haxe_service(1, 2) # prints '3'
