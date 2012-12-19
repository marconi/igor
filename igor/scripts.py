# -*- coding: utf-8 -*-

import subprocess
from docopt import docopt
from fabric.api import env, run

import igor
from igor.serve import start as start_serving
from igor.download import download

env.use_ssh_config = True


def igor_cmd():
    """
    Usage:
      igor server (start|stop)
      igor fetch <host> <magnet_uri>
      igor fetch local <host> <magnet_uri>

    Arguments:
      host          Host settings from your ssh config file.
      magnet_uri    Magnet URI enclosed in double quotes.

    Options:
      -h --help     Show this screen.
      --version     Show version.
    """

    args = docopt(igor_cmd.__doc__, version=igor.__version__)
    if args['fetch']:
        igor_fetch_cmd(args['<magnet_uri>'], args['<host>'], args['local'])

    elif args['server']:
        igor_server(args['start'], args['stop'])


def igor_download():
    """
    Usage:
      igor_download <magnet_uri>

    Arguments:
      host          Host settings from your ssh config file.
      magnet_uri    Magnet URI enclosed in double quotes.

    Options:
      -h --help     Show this screen.
      --version     Show version.
    """

    args = docopt(igor_download.__doc__, version=igor.__version__)
    download(args['<magnet_uri>'])


def igor_fetch_cmd(magnet_uri, host, local):
    if not local:
        env.host_string = host
        run('igor fetch %s' % magnet_uri)
    else:
        cmd = 'igor_download "%s"' % magnet_uri
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            shell=True)


def igor_server(start, stop):
    if start and not stop:
        start_serving()
    elif stop and not start:
        # TODO: stop the server
        pass
