import os, sys
from os.path import abspath, dirname, join

BASE_DIR = abspath(dirname(__file__))

if os.name == 'nt':
    ECHO_RUNNER = join(BASE_DIR, 'echorunner.exe')
elif sys.platform == 'darwin':
    ECHO_RUNNER = join(BASE_DIR, 'echorunner.app',
                            'Contents', 'MacOS', 'echorunner')
else:
    ECHO_RUNNER = join(BASE_DIR, 'echorunner')