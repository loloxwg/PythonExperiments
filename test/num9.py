# 文件内容操作

# os 模块

# 文本文件
# 二进制

# utf8 中文为3位


s = 'hello\nhihih'

with open('sample.txt', 'w')as fp:
    fp.write(s)
with open('sample.txt')as fp:
    print(fp.read())

import pickle
import shelve

