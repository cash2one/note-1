#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd


book = xlrd.open_workbook('CRM系统账号名单.xlsx')

# 获取一个工作表
sheet = book.sheets()[0]
# sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name(u'Sheet1')

row_data = sheet.row_values(3)
# def row_encode(row_data):
#     ret = []
#     for data in row_data:
#         try:
#             data = data.encode('utf-8')
#         except AttributeError:
#             data = str(int(data))
#         ret.append(data)
#     return ret

# row_data = row_encode(row_data)
print len(row_data)
for data in row_data:
    print data


# def read_sheet(sheet):
#     return [row_encode(sheet.row_values(i)) for i in range(sheet.nrows)]

# data = read_sheet(sheet)
# print data
