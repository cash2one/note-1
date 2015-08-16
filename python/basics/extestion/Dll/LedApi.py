# -*- coding: utf-8 -*-

from ctypes import *

ledApi = windll.LoadLibrary('LEDSender.dll')
#dll = cdll.LoadLibrary('flycamera.dll')

#设备参数结构体的处理
class DeviceParam(Structure):
    _fields_ = [("devType",c_int),
                ("Speed",c_int),
                ("ComPort",c_int),
                ("FlowCon",c_int),
                ("locPort",c_int),
                ("rmtPort",c_int),
                ("memory",c_int),
                ("Phone",c_char*32),
                ("Reserved",c_int*5)]

devParam = DeviceParam()
#define DEVICE_TYPE_COM    0
#define DEVICE_TYPE_UDP    1
#define DEVICE_TYPE_485    2
devParam.devType = 0
#define SBR_9600           0
#define SBR_14400          1
#define SBR_19200          2
#define SBR_38400          3
#define SBR_57600          4
#define SBR_115200         5
devParam.Speed = 4
devParam.ComPort = 5

#对象区域
class Rect(Structure):
    _fields_ = [("left",c_int),
                ("top",c_int),
                ("right",c_int),
                ("bottom",c_int)]
#灰分值区域
rect1 = Rect()
rect1.left = 3
rect1.top = 32
rect1.right = 192
rect1.bottom  = 64
#年月日区域
rect2 = Rect()
rect2.left = 3
rect2.top = 3
rect2.right = 192
rect2.bottom = 64
#时分秒区域
rect3 = Rect()
rect3.left = 123
rect3.top = 3
rect3.right = 192
rect3.bottom = 64
#仓号区域
rect4 = Rect()
rect4.left = 131
rect4.top = 24
rect4.right = 192
rect4.bottom = 64
#煤种区域
rect5 = Rect()
rect5.left = 131
rect5.top = 45
rect5.right = 192
rect4.bottom = 64

def openDev(devParam):
    devID = ledApi.LED_Open(byref(devParam),0,0,0)#byref处理结构体指针
    return devID

def closeDev(devID):
    ledApi.LED_Close(devID)

def sendToScreen(devID):
    ledApi.LED_SendToScreen(devID,0,'',0)

#define ROOT_PLAY       0x11
#define ROOT_DOWNLOAD   0x12

#define SCREEN_UNICOLOR    1
#define SCREEN_COLOR       2
#define SCREEN_FULLCOLOR   3
#define SCREEN_GRAY        4

#define DF_YMD             1      //年月日  "2004年12月31日"
#define DF_HN              2      //时分    "19:20"
#define DF_HNS             3      //时分秒  "19:20:30"
#define DF_Y               4      //年      "2004"
#define DF_M               5      //月      "12" "01" 注意：始终显示两位数字
#define DF_D               6      //日
#define DF_H               7      //时
#define DF_N               8      //分
#define DF_S               9      //秒
#define DF_W               10     //星期    "星期三"
    
def makeRoot():
    ret = ledApi.MakeRoot(17,2)
    return ret

def addLeaf():
    ret = ledApi.AddLeaf(10000)
    return ret

def addDateTime(rect,DF):
    ret = ledApi.AddDateTime(byref(rect),1,'宋体',12,255,DF)
    return ret

def addText(text,rect):
    ret = ledApi.AddText(text,byref(rect),1,2,1,'宋体',12,255)
    return ret


if __name__ == '__main__':
    pass


















