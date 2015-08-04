#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd


book = xlrd.open_workbook('CRM系统账号名单.xlsx')

# 获取一个工作表
sheet = book.sheets()[0]
# sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name(u'Sheet1')

# 获取整行和整列的值
sheet.row_values(i)
sheet.col_values(i)

# 获取行数和列数
nrows = sheet.nrows
ncols = sheet.ncols

# 循环行列表数据
for i in range(nrows ):
    print sheet.row_values(i)

# 单元格
cell_A1 = sheet.cell(0,0).value
cell_C4 = sheet.cell(2,3).value

# 使用行列索引
cell_A1 = sheet.row(0)[0].value
cell_A2 = sheet.col(1)[0].value

# 简单的写入
row = 0
col = 0
## 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1
value = '单元格的值'
xf = 0 # 扩展的格式化
sheet.put_cell(row, col, ctype, value, xf)
sheet.cell(0,0)  #单元格的值'
sheet.cell(0,0).value #单元格的值'