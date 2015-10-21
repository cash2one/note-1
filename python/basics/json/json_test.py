#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''json test'''

import json


info = {'Personal':{'name':u'郑国文', 'phone':'15901095956', 'sex':u'男'},
        'Assets':{'house':u'郑国文', 'car':u'郑国文', 'fin':u'建设银行', 'wealth':120000},
        'Brand':{'sumsung':1, 'lenovo':2, 'apple':3, 'BMW':4, 'ZARA':5},
        'Media':{'month3':{'sohu':{'visitdays':101},
                           'sina':{'visitdays':211},
                           'baidu':{'visitdays':1001},
                           },
                 'month6':{'sohu':{'visitdays':101},
                           'sina':{'visitdays':211},
                           'baidu':{'visitdays':1001},
                           },
                 'month12':{'sohu':{'visitdays':101},
                            'sina':{'visitdays':211},
                            'baidu':{'visitdays':1001},
                            }
                 },
        'Consumption':{'month3':{'food':{'visits':321, 'pay':1298, 'number':'32'},
                                 'clothes':{'visits':321, 'pay':1298, 'number':'32'},
                                 'electronic product':{'visits':321, 'pay':1298, 'number':'32'},
                                 },
                       'month6':{'food':{'visits':321, 'pay':1298, 'number':'32'},
                                 'clothes':{'visits':321, 'pay':1298, 'number':'32'},
                                 'electronic product':{'visits':321, 'pay':1298, 'number':'32'},
                                 },
                       'month12':{'food':{'visits':321, 'pay':1298, 'number':'32'},
                                 'clothes':{'visits':321, 'pay':1298, 'number':'32'},
                                 'electronic product':{'visits':321, 'pay':1298, 'number':'32'},
                                 },
                       'level':{'food':0.321, 'clothes':0.11, 'electronic product':0.17}
                       }
        }


json_obj = json.dumps(info)
print json_obj
print type(json_obj)
res = json.loads(json_obj)
print
print
print res
print type(res)

