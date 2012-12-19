# -*- coding: utf-8 -*-

import os
import uuid
import time
import shutil
import logging
import tarfile
import libtorrent as lt

from .settings import STATIC_PATH

logger = logging.getLogger(__name__)


def download(magnet_uri):
    # compose filename where to save downloaded file
    download_uuid = str(uuid.uuid4())
    tar_filename = "%s.tar.gz" % download_uuid
    save_path = os.path.join(STATIC_PATH, download_uuid)

    # start torrent listening
    session = lt.session()
    session.listen_on(6881, 6891)

    # add magnet url
    h = session.add_torrent({'url': magnet_uri, 'save_path': save_path})
    name = h.name()
    logger.info('starting: %s' % name)

    state_str = ['queued', 'checking', 'downloading metadata', 'downloading',
                 'finished', 'seeding', 'allocating', 'checking fastresume']

    # download file
    while not h.is_seed():
        stat = h.status()
        print '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (
            stat.progress * 100, stat.download_rate / 1000,
            stat.upload_rate / 1000, stat.num_peers, state_str[stat.state])
        time.sleep(1)

    logger.info('downloading complete!')
    logger.info('Compressing...')

    tar = tarfile.open(os.path.join(STATIC_PATH, tar_filename), "w")
    tar.add(save_path, name)
    tar.close()

    shutil.rmtree(save_path)
    logger.info('compressing complete!')
