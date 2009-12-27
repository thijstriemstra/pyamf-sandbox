# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

import sys, os
sys.path.append(os.getcwd())

from twisted.application import internet, service
from server import TimerFactory, SocketPolicyFactory

appPort = 8000
policyPort = 843
factory = TimerFactory()

# this is the important bit
application = service.Application('echo-runner-example')

timerService = internet.TCPServer(appPort, factory)
socketPolicyService = internet.TCPServer(policyPort, SocketPolicyFactory('socket-policy.xml'))

timerService.setServiceParent(application)
socketPolicyService.setServiceParent(application)
