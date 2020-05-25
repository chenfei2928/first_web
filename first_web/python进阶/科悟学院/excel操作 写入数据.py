import xlwt

# 创建一个workbook
workbook = xlwt.Workbook()

sheet = workbook.add_sheet('周杰伦')

#准备写入数据

lst = [
    {"ID": 1, "name": "张无忌"},
    {"ID": 2, "name": "张三丰"},
    {"ID": 3, "name": "张翠山"},
    {"ID": 4, "name": "灭绝师太"},
    {"ID": 5, "name": "杨逍"},
    {"ID": 6, "name": "赵敏"},
    {"ID": 7, "name": "周芷若"},
    {"ID": 8, "name": "小昭"},

]

# 表头
sheet.write(0,0,"id")
sheet.write(0,1,'name')

for i in range(len(lst)):
    dic = lst[i]
    value_lst = list(dic.values())
    for j in range(len(value_lst)):
        sheet.write(i+1,j,value_lst[j])

workbook.save("倚天屠龙记2.xls")