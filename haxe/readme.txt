= Using haXe and Python with AMF =

1. Install haXe (http://haxe.org/compile)
2. Make sure this directory is on the HAXE_LIBRARY_PATH
3. Compile the file by running: haxe server.hxml
4. Enable mod_neko in Apache (http://haxe.org/tutos/mod_neko/ubuntu)
5. Create an Alias in your vhost:
   Alias /gateway/haxe /home/username/haxe/server.n
6. Browse to http://yourserver.com/gateway/haxe which should print:
   haXe remoting gateway
7. Start the client.py to test the Python/haXe communication

Thijs Triemstra, may 2008.
