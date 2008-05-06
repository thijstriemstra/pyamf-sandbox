#!/bin/bash

export HAXE_LIBRARY_PATH="/usr/local/haxe/std:."
haxe server.hxml
echo "Build complete."
