from random import random

times = int(input('请输入投掷飞镖次数'))
hist = 0
for i in range(times):  # range 生成一个连续数字序列
    x = random()  # 生成随机数
    y = random()
    if x * x + y * y < 1:
        hist += 1
print(4.0 * hist / times)


# 蒙特·卡罗方法是一种通过概率来得到问题近似解的方法，在很多领域都有重要的应用，
# 其中就包括圆周率近似值的计算问题。假设有一块边长为 2 的正方形木板，上面画一个单位
# 圆，然后随意往木板上扔飞镖，落点坐标(x, y)必然在木板上（更多的时候是落在单位圆内），
# 如果扔的次数足够多，那么落在单位圆内的次数除以总次数再乘以 4，这个数字会无限逼近
# 圆周率的值