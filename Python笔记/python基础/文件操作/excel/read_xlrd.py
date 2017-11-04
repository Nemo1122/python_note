import xlrd, os


# 打开一个excel
data = xlrd.open_workbook(file)

#通过sheet名称打开
#table = data.sheet_by_name("login")
#通过index打开,0开始
table = data.sheet_by_index(0)

#获取整行和整列的值（数组）　　
# row_value = table.row_values(0)
# col_value = table.col_values(0)

# 获取行数和列数
# nrows = table.nrows
# ncols = table.ncols

# 单元格
# cell_A1 = table.cell(0, 0).value
# cell_C4 = table.cell(2, 3).value


# 使用行列索引
# cell_A1 = table.row(0)[0].value
# cell_A2 = table.col(1)[0].value

# 获取数据组成([row1],[row2])

# e_list = []
# for n_row in range(1, table.nrows):
#      e_list.append(table.row_values(n_row))
# e_tuple = tuple(e_list)

# print(e_tuple)
# print(table.cell(0, 0).value)
# print(table.row(0)[0].value)
# print(table.col(1))


e_list = []
header_row = table.row_values(0)
for n_row in range(1, table.nrows):
    e_list.append(dict(zip(header_row, table.row_values(n_row))))
    # print(zip(header_row, table.row_values(n_row)))
    # zip函数接受任意多个(包括0个和1个)序列作为参数,返回一个tuple列表。[<zip object at 0x0000018AF18D6FC8>, <zip object at 0x0000018AF18D6E48>]

print(e_list)


