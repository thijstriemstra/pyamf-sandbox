// from http://haxe.org/tutos/remoting/client_server

class Client {
    static function display(v) {
        trace(v);
    }
    static function main() {
        var URL = "http://localhost/gateway/haxe";
        var cnx = haxe.remoting.AsyncConnection.urlConnect(URL);
        cnx.onError = function(err) { trace("Error : "+Std.string(err)); };        
        cnx.Server.foo.call([1,2],display);
    }
}
