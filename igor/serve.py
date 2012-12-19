# -*- coding: utf-8 -*-

import os
import fapws._evwsgi as evwsgi
from fapws import base
from fapws.contrib import views
from mako.template import Template
import pkg_resources as pkgr

from .settings import STATIC_PATH, HOST, PORT, URL_SCHEME

index_template = pkgr.resource_filename('igor', 'templates/index.mako')


def start():
    evwsgi.start(HOST, str(PORT))
    evwsgi.set_base_module(base)

    evwsgi.wsgi_cb(('/static', views.Staticfile(STATIC_PATH)))
    evwsgi.wsgi_cb(('/broadcast', broadcast))

    evwsgi.set_debug(0)
    evwsgi.run()


def broadcast(environ, start_response):
    template = Template(filename=index_template)

    fnames = os.listdir(STATIC_PATH)
    urls = ["%s://%s:%s/static/%s" % (URL_SCHEME, HOST, PORT, f) \
        for f in fnames if f[0] != '.']

    start_response('200 OK', [('Content-Type', 'text/html; charset=UTF-8')])
    response = template.render_unicode(urls=urls).encode('utf-8', 'replace')
    return [response]
