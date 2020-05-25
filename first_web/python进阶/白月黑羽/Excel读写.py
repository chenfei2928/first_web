import xlrd

book = xlrd.open_workbook('income.xlsx')

print(f"包含表单数量 {book.nsheets}")

print(f"表单名称分布为{book.sheet_names()}")


sheet = book.sheet_by_index(0)  # 表单索引从0开始，获取第一个表单对象

print(sheet.name) # 表单名
print("表单索引为:",sheet.number) # 表单索引
print(sheet.nrows)  # 行数
print(sheet.ncols)  # 列数


print(f'单元格A1内容是:{sheet.cell_value(rowx=5,colx=1)}')

print(f'第一行内容是：{sheet.row_values(rowx=0)}')

print(f'第一列内容是：{sheet.col_values(colx=0)}')



incomes = sheet.col_values(colx=1,start_rowx=1)
print(incomes)

print(f"2017年总收入为{sum(incomes)}")


