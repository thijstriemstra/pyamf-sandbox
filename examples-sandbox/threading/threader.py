import os, logging, sys

from multiprocessing import Process, current_process, freeze_support
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler

from pyamf.remoting.gateway.wsgi import WSGIGateway

def echo(txt):
    return txt

services = {
    'echo': echo
}

application = WSGIGateway(services)

if sys.platform == 'win32':
    import multiprocessing.reduction    # make sockets pickable/inheritable

def note(format, *args):
    sys.stderr.write('[%s]\t%s\n' % (current_process().get_name(),format%args))

class RequestHandler(WSGIRequestHandler):
    # we override log_message() to show which process is handling the request
    def log_message(self, format, *args):
        note(format, *args)

def serve_forever(server):
    note('starting server')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

def runpool(address, number_of_processes):
    # create a single server object -- children will each inherit a copy
    #server = HTTPServer(address, RequestHandler)

    httpd = simple_server.WSGIServer(
        address, RequestHandler,
    )
    
    # create child processes to act as workers
    for i in range(number_of_processes-1):
        Process(target=serve_forever, args=(httpd,)).start()

    httpd.set_app(application)
    
    # main process also acts as a worker
    serve_forever(httpd)

def test():
    DIR = os.path.join(os.path.dirname(__file__), '..')
    ADDRESS = ('localhost', 8000)
    NUMBER_OF_PROCESSES = 4

    print 'Serving AMF at http://%s:%d using %d worker processes' % \
          (ADDRESS[0], ADDRESS[1], NUMBER_OF_PROCESSES)
    print 'To exit press Ctrl-' + ['C', 'Break'][sys.platform=='win32']

    os.chdir(DIR)
    runpool(ADDRESS, NUMBER_OF_PROCESSES)

if __name__ == '__main__':
    freeze_support()
    test()
