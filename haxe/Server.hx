// from http://haxe.org/tutos/remoting/client_server

class Server {
    function new() {
    }
 
    function foo(x,y) { return x + y; }
 
    static function main() {
        var r = new neko.net.RemotingServer();
        r.addObject("Server",new Server());
        if( r.handleRequest() )
            return;
        // handle normal browser request
        neko.Lib.print("haXe remoting gateway");
    } 
}
