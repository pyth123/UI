# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 20:20
# @Author  : Vicky
# @File    : demo-test01.py
# @Software: PyCharm

import json
a = '{"isOK":1, "isRunning":"None"}'
# b = json.dumps(a)
c = json.loads(a)
print(c["isOK"])
# print(str(c))