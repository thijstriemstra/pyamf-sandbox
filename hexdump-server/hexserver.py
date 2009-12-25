"""
A port forwarding proxy server that hex-dumps AMF traffic in both directions.

Based on http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/502293
by Andrew Ellerton (activestate-at->ellerton.net) Copyright (C) 2005-2007
"""

import sys, getopt, logging, re

from pyamf.util import hexdump

from twisted.python import failure
from twisted.internet import reactor, error, address, tcp
from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.web.http import HTTPFactory

logger = logging.getLogger()
logname=None
logger.setLevel(logging.INFO)
  
def transport_info(t):
  if isinstance(t, tcp.Client): return transport_info(t.getHost())
  elif isinstance(t, address.IPv4Address): return "%s:%d" % (t.host, t.port)
  else: return repr(t)

class HexdumpClientProtocol(Protocol):
  def __init__(self, factory):
    self.factory=factory

  def connectionMade(self):
    logger.debug("bridge connection open %s" % transport_info(self.transport))
    self.factory.owner.clientName=transport_info(self.transport)
    self.writeCache()

  def write(self, buf):
    self.transport.write(buf)

  def dataReceived(self, recvd):
    self.factory.owner.write(recvd)

  def writeCache(self):
    while self.factory.writeCache:
      item = self.factory.writeCache.pop(0)
      self.write(item)

class HexdumpClientFactory(ClientFactory):
  def __init__(self, owner):
    self.owner = owner
    self.writeCache = []

  def startedConnecting(self, connector):
    logger.debug('connection opening...')

  def buildProtocol(self, addr):
    logger.debug('connecting to remote server %s' % transport_info(addr))
    p = HexdumpClientProtocol(self)
    self.owner.dest = p
    return p

  def clientConnectionLost(self, connector, reason):
    if isinstance(reason, failure.Failure):
      if reason.type == error.ConnectionDone:
        logger.info("remote server closed connection")
      else:
        logger.info("remote server connection lost, reason: %r" % reason)
    self.owner.close()

  def clientConnectionFailed(self, connector, reason):
    logger.debug("dest: connection failed: %r" % reason)
    self.owner.close()

class HexdumpServerProtocol(Protocol):
  def __init__(self, serverFactory):
    self.factory=serverFactory
    self.clientFactory = HexdumpClientFactory(self)
    self.clientName=id(self) # this is repopulated later
    self.serverName=None

  def serverName(self):
    return "%s:%d" %(self.factory.remote_host,self.factory.remote_port)

  def connectionMade(self):
    self.serverName="%s:%d" %(self.factory.remote_host,self.factory.remote_port)
    logger.info("client %s opened connection -> server %s" % (
      self.clientName, self.serverName))

    # cxn to this server has opened. Open a port to the destination...
    reactor.connectTCP(self.factory.remote_host,
      self.factory.remote_port, self.clientFactory)

  def connectionLost(self, reason):
    logger.info("client %s closed connection" % self.clientName) # str(reason)
    if self.dest and self.dest.transport: self.dest.transport.loseConnection()

  def connectionFailed(self, reason):
    logger.debug("proxy connection failed: %s" % str(reason))

  def dataReceived(self, recvd):
    logger.info("client %s -> server %s (%d bytes)\n%s" % (
      self.clientName, self.serverName, len(recvd), hexdump(recvd)))
    if hasattr(self, "dest"):
      self.dest.write(recvd)
    else:
      logger.debug("caching data until remote connection is open")
      self.clientFactory.writeCache.append(recvd)

  def write(self, buf):
    logger.info("client %s <= server %s (%d bytes)\n%s" % (
      self.clientName, self.serverName, len(buf), hexdump(buf)))
    self.transport.write(buf)

  def close(self):
    self.dest = None
    self.transport.loseConnection()

class HexdumpServerFactory(HTTPFactory):
  def __init__(self, listen_port, remote_host, remote_port, max_connections = None):
    self.listen_port = listen_port
    self.remote_host = remote_host
    self.remote_port = remote_port
    self.max_connections = max_connections
    self.numConnections = 0

  def startFactory(self):
    if logname: handler=logging.FileHandler(logname)
    else: handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("hex-dump proxy listening on port %d" % self.listen_port)
    
  def buildProtocol(self, addr): # could process max/num connections here
    return HexdumpServerProtocol(self)

