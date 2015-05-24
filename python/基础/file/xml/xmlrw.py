# -*- coding: utf-8 -*-

from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse('csms_com.xml')
serialport = tree.find("serialPort")
print serialport.text
serialport.text = str(6)
tree.write('csms_com.xml',encoding="utf-8", xml_declaration=True, default_namespace=None, method="xml")

#if __name__ == '__main__':
