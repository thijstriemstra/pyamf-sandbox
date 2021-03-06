# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Echo test client.

You can use this example with the echo test server.

@author: U{Thijs Triemstra<mailto:info@collab.nl>}
@author: U{Nick Joyce<mailto:nick@boxdesign.co.uk>}
@since: 0.1.0
"""

import sys

from util import parse_args, new_client

options = parse_args(sys.argv[1:])
service = options[0].service

client = new_client('Echo Test', options[0], service)

print client('Hello World')
