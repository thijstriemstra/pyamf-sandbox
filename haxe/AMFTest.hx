// from http://haxe.org/tutos/remoting/flash_amf

class AMFTest {
    static function displayResult( r : Dynamic ) {
	trace("result : "+r);
    }
 
    static function main() {
	var c = haxe.remoting.AsyncConnection.urlConnect("http://demo.pyamf.org/gateway/helloworld");
	c.onError = function(e) {
	    trace("error : "+Std.string(e));
	};
	c.echo.call(["Hello World!"],displayResult);
    }
}
