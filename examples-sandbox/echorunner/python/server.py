#!/usr/bin/env python
#
# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Echo Test runner AIR app.

 1. Start this server
 2. Launch the AIR application and pass in the gateway and service info
 3. The AIR application runs the tests and returns the results to Twisted
 4. Twisted writes the results to file
 5. AIR application terminates after last request
 6. Python server exits after receiving last request

@since: 0.3.1
"""

try:
    import twisted
except ImportError:
    print "This application requires the Twisted framework. Download it from http://twistedmatrix.com"
    raise SystemExit

import setup_cfg as cfg

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.web import server, static, resource

import os
from os.path import join
from subprocess import call
from sys import exit
from datetime import datetime

import pyamf
from pyamf.remoting.gateway.twisted import TwistedGateway

class TimerProtocol(Protocol):
    interval = 3.0 # interval in seconds to send the time
    encoding = pyamf.AMF0
    timeout = 300 

    def __init__(self):
        self.started = False
        self.encoder = pyamf.get_encoder(self.encoding)
        self.stream = self.encoder.stream

    def connectionLost(self, reason):
        Protocol.connectionLost(self, reason)

        self.factory.number_of_connections -= 1

    def connectionMade(self):
        if self.factory.number_of_connections >= self.factory.max_connections:
            self.transport.write('Too many connections, try again later')
            self.transport.loseConnection()

            return

        self.factory.number_of_connections += 1
        self.timeout_deferred = reactor.callLater(TimerProtocol.timeout, self.transport.loseConnection)

    def dataReceived(self, data):
        data = data.strip()
        if data == 'start':
            # start sending a date object that contains the current time
            if not self.started:
                self.start()
        elif data == 'stop':
            self.stop()

        if self.timeout_deferred:
            self.timeout_deferred.cancel()
            self.timeout_deferred = reactor.callLater(TimerProtocol.timeout, self.transport.loseConnection)

    def start(self):
        self.started = True
        self.sendTime()

    def stop(self):
        self.started = False

    def sendTime(self):
        if self.started:
            self.encoder.writeElement(datetime.now())
            self.transport.write(self.stream.getvalue())
            self.stream.truncate()

            reactor.callLater(self.interval, self.sendTime)

class TimerFactory(Factory):
    protocol = TimerProtocol
    max_connections = 1000

    def __init__(self):
        self.number_of_connections = 0

class SocketPolicyProtocol(Protocol):
    """
    Serves strict policy file for Flash Player >= 9,0,124.
    
    @see: U{http://adobe.com/go/strict_policy_files}
    """
    def connectionMade(self):
        self.buffer = ''

    def dataReceived(self, data):
        self.buffer += data

        if self.buffer.startswith('<policy-file-request/>'):
            self.transport.write(self.factory.getPolicyFile(self))
            self.transport.loseConnection()

class SocketPolicyFactory(Factory):
    protocol = SocketPolicyProtocol

    def __init__(self, policy_file):
        """
        @param policy_file: Path to the policy file definition
        """
        self.policy_file = policy_file

    def getPolicyFile(self, protocol):
        return open(self.policy_file, 'rt').read()

if __name__ == '__main__':
    import echo
    services = {'echo': echo.echo}
    
    gw = TwistedGateway(services, expose_request=False)
    root = resource.Resource()

    root.putChild('', gw)
    root.putChild('/gateway', gw)
    root.putChild('crossdomain.xml', static.File(os.path.join(
        os.getcwd(), os.path.dirname(__file__), 'crossdomain.xml'),
        defaultType='application/xml'))

    print "Started Echo Runner server"

    reactor.listenTCP(8080, server.Site(root), 50, 'localhost')
    reactor.listenTCP(8000, TimerFactory())
    reactor.listenTCP(8043, SocketPolicyFactory('socket-policy.xml'))
    reactor.run()
    
