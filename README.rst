Igor
====

A sort-of download proxy.

Tell me more
------------

Downloading torrent files directly to local machine is slow when you have slow internet connection, Igor will fetch your torrent files from your remote host and prepare them ready for you to download.

This works because most connection in remote hosts are faster than where I am right now and downloading files from my host to my machine uses HTTP with the file already formed unlike in a torrent where the file still needs to be asembled from different resources.

Requirements
------------

Aside from those under setup.py, Igor also needs `libtorrent <http://www.rasterbar.com/products/libtorrent/>`_ with `python bindings <http://www.rasterbar.com/products/libtorrent/python_binding.html>`_ enabled.

TODO
----

- Daemonize server
- Teach Igor how to shutdown daemonized server

Screenshots
-----------

.. image:: http://github.marconijr.com/igor/no_files.png
.. image:: http://github.marconijr.com/igor/with_files.png
