# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
#
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
#
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manager.py','w'))
#
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
#
# map(lambda f:f.close(),l)


# # 导入整个包
# import glance  # 默认执行包下的__init__.py
#
# glance.api.policy.get()   # 不能直接这样使用

import glance.api.policy

glance.api.policy.get()


from glance.api import policy   #推荐导包方案
policy.get()



"""
绝对导入  
    绝对路径导入，安全

相对导入
    .当前包
    ..上一层包
    

"""