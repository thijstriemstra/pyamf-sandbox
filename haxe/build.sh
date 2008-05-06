#!/bin/bash

echo "Building haXe server..."
export HAXE_LIBRARY_PATH="/usr/local/haxe/std:."
haxe server.hxml

echo ""
echo "Compiling SWF..."
ant -f flex/build.xml

echo "Build complete."
