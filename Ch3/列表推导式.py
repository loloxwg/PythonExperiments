# 阿凡提与国王比赛下棋，国王说要是自己输了的话阿凡提想要什么他都可以拿得出来。阿凡提说那就要点米吧，棋盘一共64个小格子，在第一个格子里放1粒米，第二个格子里放2粒米，第三个格子里放4粒米，第四个格子里放8粒米，以此类推，后面每个格子里的米都是前一个格子里的2倍，一直把64个格子都放满。需要多少粒米呢？
from functools import *
# [   xx for i in range()]
# [列表推导式]
a = sum([2 ** i for i in range(64)])
seq = list(2 ** i for i in range(64))
b = reduce(lambda x, y: x + y, seq)
c=int('1'*64, 2)
c=int('1'*64, 2)