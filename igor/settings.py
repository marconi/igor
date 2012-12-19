# -*- coding: utf-8 -*-

import os


HOST = 'localhost'
PORT = 8080
URL_SCHEME = 'http'
STATIC_PATH = os.path.join(os.path.expanduser('~'), "Igor's Dump")

if not os.path.exists(STATIC_PATH):
    os.mkdir(STATIC_PATH)
