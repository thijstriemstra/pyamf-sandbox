= Using haXe and Python with AMF =

1. Install haXe (http://haxe.org/compile) and PyAMF
   (http://pyamf.org/wiki/Install)
2. Make sure the directory containing the haXe sample server is on the
   HAXE_LIBRARY_PATH
3. Compile the file by running: haxe server.hxml
4. Enable mod_neko in Apache (http://haxe.org/tutos/mod_neko/ubuntu)
5. Create an Alias in your vhost:
   Alias /gateway/haxe /home/username/haxe/server.n
6. Browse to http://yourserver.com/gateway/haxe which should print:
   haXe remoting gateway
7. Start client.py to test the Python/haXe communication
8. Start haxe.swf to test the Flash/haXe remoting
9. (optional) If you have the Flex SDK installed, adjust the path
   to the SDK in flex/build.xml and run ./build.sh which will compile
   haxe.swf using Apache Ant. You can use this SWF to connect to the
   haXe remoting server.

Author: Thijs Triemstra, may 2008.
