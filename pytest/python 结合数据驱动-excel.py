"""
读取excel文件
第三方库
    xlrd
    xlwings
    pandas
openpyxl
    官方文档：https://openpyxl.readthedocs.io/en/stable/
    安装： pip install openpyxl
    导入：import openpyxl
"""
import openpyxl
"""
openpyxl库的操作：
    读取工作簿
    读取工作表
    读取单元格
"""
# 获取工作簿
book = openpyxl.load_workbook("block 各版本测试信息.xlsx")
# 获取工作表
sheet = book.active
# 获取对应的单元格
a_1 = sheet["A1"].value
print(a_1)