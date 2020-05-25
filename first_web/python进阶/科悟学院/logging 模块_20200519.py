import datetime
def days(x):
    days_ago_x = datetime.date.today() - datetime.timedelta(days=x)
    return days_ago_x
li = []
for i in range(7,15):
    days_list = days(i)
    li.append(days_list)

print(li)