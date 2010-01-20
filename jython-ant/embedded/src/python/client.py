"""
Hello world example client for Apache Ant.
"""

import logging
logging.basicConfig(level=logging.DEBUG,
           format='%(asctime)s %(levelname)-5.5s %(message)s')


from pyamf.remoting.client import RemotingService

url = 'http://localhost:8000'
gateway = RemotingService(url, logger=logging)

echo_service = gateway.getService('echo.echo')
result = echo_service('Hello world!')

logging.info(result)
