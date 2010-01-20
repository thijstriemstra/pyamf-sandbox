"""
Video to ByteArray server.

@author: Thijs Triemstra
"""

def saveData(name, data):
    """
    Save data to disk.
    """
    try:
        amf_file = open(name, 'wb')
        amf_file.write(data.getvalue())
        amf_file.close()
    except:
        return 'failed'
    
    return 'success'

services = {
    'gti.saveData': saveData
}

if __name__ == '__main__':
    from pyamf.remoting.gateway.wsgi import WSGIGateway
    from wsgiref import simple_server

    gw = WSGIGateway(services)

    httpd = simple_server.WSGIServer(
        ('localhost', 8000),
        simple_server.WSGIRequestHandler,
    )

    httpd.set_app(gw)

    print "Running Video -> ByteArray AMF gateway on http://localhost:8000"

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
