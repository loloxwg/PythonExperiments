import matplotlib.pyplot as plt
import numpy as np


# 阻尼正弦波计算公式
def f(t):
    'A damped exponential'
    s1 = np.cos(2 * np.pi * t)  # 余弦
    e1 = np.exp(-t)  # 自然数e的幂
    return s1 * e1


t1 = np.arange(0.0, 5.0, 0.01)  # 定义x轴(可以将步长改小，图像就很明显)

l = plt.plot(t1, f(t1), 'ro')  # t1是x轴上的点, f(t1)是y轴上的点, ro表示点是红色+圆形
plt.setp(l, markersize=10)  # 设置点的大小
plt.setp(l, markerfacecolor='g')  # 颜色

plt.show()
