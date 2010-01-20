#!/usr/bin/env python
#
# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Echo test server.

You can use this example with the echo_test.swf client on the
U{EchoTest<http://pyamf.org/wiki/EchoTest>} wiki page.

@author: U{Nick Joyce<mailto:nick@boxdesign.co.uk>}
@since: 0.1.0
"""

import sys

import echo
from util import parse_args, run_server

options = parse_args(sys.argv[1:])
services = {options[0].service: echo.echo}

run_server('Echo Test', options[0], services)
