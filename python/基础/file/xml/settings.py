#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: settings.py
# Created: 11/12/2013 11:27:26
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

from xml.etree import ElementTree as ET
import os

AshTcp = ''
AshPort = 0
MZMLTcp = ''
MZMLPort = 0
I7017Com = 0
adCom = 0
source = 0
offset = 0
sampleInterval = 1000
path = r'C:/Documents and Settings/CWAC/config.xml'

def createSettingsFile():
    if not os.path.exists(path):
        os.makedirs(r'C:/Documents and Settings/CWAC/')
        root = ET.Element('config')
        
        AddrAsh = ET.SubElement(root, 'Addr')
        AddrAsh.set('id', 'Ash')
        ashTcp = ET.Element('tcp')
        ashTcp.text = 'localhost'
        ashTcp.append(AddrAsh)
        ashPort = ET.Element('port')
        ashPort.text = '12001'
        ashPort.append(AddrAsh)

        AddrMZML = ET.SubElement(root, 'MZML')
        AddrMZML.set('id', 'MZML')
        MZMLTcp = ET.Element('tcp')
        MZMLTcp.text = 'localhost'
        MZMLTcp.append(AddrMZML)
        MZMLPort = ET.Element('port')
        MZMLPort.text = '12002'
        MZMLPort.append(AddrMZML)

        SerialPortI7017 = ET.SubElement(root, 'SerialPort')
        SerialPortI7017.set('id', 'I7017')
        comI7017 = ET.Element('com')
        comI7017.text = '1'
        comI7017.append(SerialPortI7017)
        
        SerialPortI7017 = ET.SubElement(root, 'SerialPort')
        SerialPortI7017.set('id', 'I7017')
        comI7017 = ET.Element('com')
        comI7017.text = '1'
        comI7017.append(SerialPortI7017)
        

def readSettings():
    global AshTcp
    global AshPort
    global MZMLTcp
    global MZMLPort
    global I7017Com
    global adCom
    global source
    global offset
    global sampleInterval
    
    tree = ET.parse(path)
    root = tree.getroot()
    
    #先查找到所有的节点，然后已节点属性为键存储在字典中，再根据键去确定指定的节点，来获取节点值
    Addr = root.findall('Addr')
    dic = dict()
    for addr in Addr:
        dic[addr.attrib['id']]=addr
        
    AshTcp = dic['Ash'].find('tcp').text
    AshPort = int(dic['Ash'].find('port').text)
    MZMLTcp = dic['MZML'].find('tcp').text
    MZMLPort = int(dic['MZML'].find('port').text)
    
    serialPort = root.findall('SerialPort')
    dic = dict()
    for com in serialPort:
        dic[com.attrib['id']]=com
    I7017Com = int(dic['I7017'].find('com').text)
    adCom = int(dic['ad'].find('com').text)

    sampleInterval = int(root.find('SampleInterval').text)
    source = int(root.find('source').text)
    offset = int(root.find('offset').text)
    
def writeSettings():
    tree = ET.parse(path)
    root = tree.getroot()
    
    Addr = root.findall('Addr')
    dic = dict()
    for addr in Addr:
        dic[addr.attrib['id']]=addr
        
    dic['Ash'].find('tcp').text = AshTcp
    dic['Ash'].find('port').text = str(AshPort)
    dic['MZML'].find('tcp').text = MZMLTcp
    dic['MZML'].find('port').text = str(MZMLPort)
    
    serialPort = root.findall('SerialPort')
    dic = dict()
    for com in serialPort:
        dic[com.attrib['id']]=com
    dic['I7017'].find('com').text = str(I7017Com)
    dic['ad'].find('com').text = str(adCom)

    root.find('SampleInterval').text = str(sampleInterval)
    root.find('source').text = str(source)
    root.find('offset').text = str(offset)
    
    tree.write(path, encoding="utf-8", xml_declaration=True, default_namespace=None, method="xml")


if __name__ == '__main__':
    createSettingsFile()














