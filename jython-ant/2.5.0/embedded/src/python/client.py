"""
Hello world example client.
"""

from pyamf.remoting.client import RemotingService

gateway = RemotingService('http://localhost:8000')

echo_service = gateway.getService('echo.echo')

print echo_service('Hello world!')
