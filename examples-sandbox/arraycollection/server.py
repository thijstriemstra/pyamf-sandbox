#!/usr/bin/env python

"""
Being in the sandbox, this file requires that the echo example dir is in the 
path
"""

import sys

from util import parse_args, run_server

import acpb

options = parse_args(sys.argv[1:])
services = {'acpb':acpb.acpb}

run_server('ArrayCollection Test', options[0], services)
