from xlrd import open_workbook
from xlutils.copy import copy

# 打开文件
rb = open_workbook("data.xls")
# 复制
wb = copy(rb)
# 选取表单
s = wb.get_sheet("login")
# 写入数据
s.write(3, 0, 'tom')
s.write(3, 1, '333')
s.write(3, 2, 'success')

# 保存
wb.save('data.xls')