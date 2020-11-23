import random as r
import string
a1 = ['张', '金', '李', '王', '赵']

a2 = ['玉', '明', '龙', '芳', '军', '玲']

a3 = ['', '立', '玲', '', '国', '']

for i in range(15):
    name = r.choice(a1) + r.choice(a2) + r.choice(a3)
    print(name)


Words=string.digitals




readlines