# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Echo test mod_wsgi example.

You can use this example with the echo_test.swf client on the
U{EchoTest<http://pyamf.org/wiki/EchoTest>} wiki page.

@author: U{Thijs Triemstra<mailto:info@collab.nl>}
@since: 0.1.0
"""

import sys
sys.path.append('/usr/src/pyamf/')
sys.path.append('/home/pyamf/examples/echo/')

import echo

from pyamf.remoting.gateway.wsgi import WSGIGateway

services = {'echo': echo.echo}

application = WSGIGateway(services)
