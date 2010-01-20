#!/usr/bin/python

from pyamf.remoting.client import RemotingService

gw = RemotingService('http://localhost:8000/')
service = gw.getService('RemoteObjectService')

print service.hello() # returns 'hello world'