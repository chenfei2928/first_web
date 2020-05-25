import  xlrd
workbook = xlrd.open_workbook(r'd:\各项目人员信息统计.xlsx')
sheet = workbook.sheet_by_name('娃哈哈')
title_row = sheet.row(0)  # 表头
# print(title_row)
print(title_row[1].value)
print(sheet.nrows)  # 最大行号

lst = []
for i in range(1,sheet.nrows):
    data_row = sheet.row(i)   # 拿到每行数据
    dic = {}
    for j in range(sheet.ncols):  #列编号
        col = data_row[j]  # 每一个单元格

        if col.ctype == xlrd.XL_CELL_DATE:  #判断值有误日期类型
            value = xlrd.xldate_as_datetime(col.value,0).strftime(('%Y-%m-%d'))  # 转换为年月日格式
        elif col.ctype == xlrd.XL_CELL_NUMBER:
            value = int(col.value)
        else:
            value = col.value

        dic[title_row[j].value] = value
    lst.append(dic)
print(lst)

