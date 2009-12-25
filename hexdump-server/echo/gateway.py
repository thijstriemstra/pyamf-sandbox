# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Echo example gateway for Django.

@author: U{Arnar Birgisson<mailto:arnarbi@gmail.com>}
@since: 0.1.0
"""

from pyamf.remoting.djangogateway import DjangoGateway

import echo

echoGateway = DjangoGateway({'echo': echo.echo}, expose_request=False)
