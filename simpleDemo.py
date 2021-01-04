import xlrd, xlwt # 读写Excel

import pyecharts # 可视化

workbook = xlrd.open_workbook('销售数据.xlsx') # 读取 Excel
sheets_ = workbook.sheets()[0] # 读取 Sheet

print(sheets_.nrows) # 最大行数
print(sheets_.ncols) # 最大列数

print(sheets_.row_values(0)) # 输出指定行数据
print(sheets_.col_values(0)) # 输出指定列数据

# 遍历所有行
for row in range(0, sheets_.nrows):
    print(sheets_.row_values(row))

# 提取姓名和销售额
names = []
sales = []

for row in range(0, sheets_.nrows):
    row_data = sheets_.row_values(row) # ['姓名', '地区', '销售额', '部门']

    name = row_data[0]
    names.append(name)

    sale = row_data[2]
    sales.append(sale)

# 可视化处理
bar = pyecharts.charts.Bar() # 柱状图
bar.add_xaxis(names) # X轴
bar.add_yaxis('销售业绩',sales) # Y 轴
bar.render('业绩统计表.html') # 生成页面
