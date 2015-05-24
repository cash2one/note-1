#coding: UTF-8

import re
import sys
import urllib
import urllib2
import datetime
from win32clipboard import *
from win32con import CF_TEXT

def get_Clipboard():
         OpenClipboard()
         text = GetClipboardData(CF_TEXT)
         CloseClipboard()
         return text


 
class CFlvcd(object):
      def __init__(self):
         self.url = ""
         self.pattern = re.compile(r"<a href *= *\"(http://f\.youku\.com/player/getFlvPath/[^\"]+)")
         self.headers = {"Accept":"*/*", "Accept-Language":"zh-CN", "":"", 
                         "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)", 
                         #"Accept-Encoding":"gzip, deflate", 
                         "Connection":"Keep-Alive"}
  
      def parse(self, url):
         self.url = "http://www.flvcd.com/parse.php?kw=" + url + "&format=super"
         req = urllib2.Request(url=self.url, headers=self.headers)
         res = urllib2.urlopen(req)
         data = res.read()
         hfilename = "flvcd.txt"
         htmlfile = open(hfilename,"w")
         htmlfile.write(data)
         re_res = self.pattern.findall(data)
         if re_res != None:
             filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S.lst")
             fhandle = open(filename, "w")
             for url in re_res:
                 # 注意是\r\n还是\n
                 fhandle.write(url + "\n")
             fhandle.close()
             print("Parse URL Done!")
         else:
             print("URL Not Found")
 
def main():
         flvcd=CFlvcd()
         print'你要下载的视频地址是'
         print get_Clipboard()
         print'确定获取请按1'
         a=raw_input()
         if (a=='1'):
                  flvcd.parse(get_Clipboard())
     
     
     
if __name__ == "__main__":
    main()
