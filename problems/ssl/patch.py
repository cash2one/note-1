#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ssl版本问题的解决办法"""

import ssl
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class MyAdapter(HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLSv1
            )

s = requests.Session()
s.mount('https://', MyAdapter())  # 所有的https连接都用ssl.PROTOCOL_SSLV3去连接
s.get('https://xxx.com')


# **********************************************************************************
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
# **********************************************************************************

import httplib, ssl, urllib2, socket


class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv3)
        except ssl.SSLError:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)


class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)

urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))


if __name__ == "__main__":
    r = urllib2.urlopen("https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse")
    print(r.read())
