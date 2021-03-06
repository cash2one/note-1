# -*- coding: utf-8 -*-

"""
重载httplib中的HTTPSConnection, 解决https中ssl的bug
"""

import ssl
import socket
import httplib
from httplib import HTTPConnection, HTTPS_PORT


class HTTPSConnection(HTTPConnection):
    """This class allows communication via SSL."""
    default_port = HTTPS_PORT

    def __init__(self, host, port=None, key_file=None, cert_file=None,
                 strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None):
        HTTPConnection.__init__(self, host, port, strict, timeout, source_address)
        self.key_file = key_file
        self.cert_file = cert_file

    def connect(self):
        """Connect to a host on a given (SSL) port."""
        sock = socket.create_connection((self.host, self.port),
                self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        # this is the only line we modified from the httplib.py file
        # we added the ssl_version variable
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

# now we override the one in httplib
httplib.HTTPSConnection = HTTPSConnection
# ssl_version corrections are done
