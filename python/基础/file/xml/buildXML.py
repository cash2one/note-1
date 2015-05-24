#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: buildXML.py
# Created: 08/01/2014 10:29:14
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------


#from xml.etree import ElementTree as ET
import os
from lxml import etree as ET

path = r'C:/Documents and Settings/CWAC/config.xml'

def createXmlFile():
    '''创建xml'''
    if not os.path.exists(path):
        try:
            os.makedirs(r'C:/Documents and Settings/CWAC')
        except WindowsError:
            pass
        
        root = ET.Element('config')

        addr_e = [('Ash','localhost','12001'),
                  ('MZML','localhost','12002')]
        for e in addr_e:
            addr = ET.SubElement(root, 'Addr')
            addr.set('id', e[0])
            tcp = ET.SubElement(addr,'tcp')
            tcp.text = e[1]
            port = ET.SubElement(addr,'port')
            port.text = e[2]

        serialport_e = [('I7017','1'),('ad','2')]
        for e in serialport_e:
            sp = ET.SubElement(root, 'Dev')
            sp.set('id', e[0])
            com = ET.SubElement(sp,'com')
            com.text = e[1]

        elist = [('SampleInterval','1000'),
             ('source','0'),
             ('offset','0')]
        for e in elist:
            sube = ET.SubElement(root,e[0])
            sube.text = e[1]

        tree = ET.ElementTree(root)
        #tree.write(path, encoding='UTF-8',xml_declaration=True, default_namespace=None, method="xml")
        tree.write(path, encoding='UTF-8',xml_declaration=True,method="xml")

def prettyXmlFile():
    '''格式化xml'''
    parser = ET.XMLParser(remove_blank_text=False, resolve_entities=True, strip_cdata=True)
    xmlfile = ET.parse(path, parser)
    pretty_xml = ET.tostring(xmlfile, encoding = 'UTF-8', xml_declaration = True,pretty_print = True)
    #doctype='<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    file = open(path, "w")
    file.writelines(pretty_xml)
    file.close()
        
        

if __name__ == "__main__":
    createXmlFile()
    prettyXmlFile()
