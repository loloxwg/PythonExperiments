# 模拟轮盘抽奖游戏
import random
#
# rewardDict = {
#     '一等奖': {0, 0.08},
#     '二等奖': {0.08, 0.3},
#     '三等奖': {0.3, 1.0}
# }
#
#
# def rewardFun():
#     num = random.random()
#
#     for k, v in rewardDict.items():
#         if v[0] <= num < v[1]:
#             return k
#
#
# resultDict = {}
#
# for i in range(1000):
#     res = rewardFun()
#     if res in resultDict:
#         resultDict[res] = +1
#     else:
#         resultDict[res] = 1
#
# for k, v in rewardDict.items():
#     print(k, '-->', v)
import random

rewardDict = {
    '一等奖':(0,0.08),
    '二等奖':(0.08,0.3),
    '三等奖':(0.3,1.0)
}

def rewardFun():
    """用户得奖等级"""
    #生成一个0～1之间的随机数
    num = random.random()
    #判断随机转盘转的是几等奖
    for k,v in rewardDict.items():
        if v[0] <= num < v[1]:
            return k

resultDict = {}

for i in range(1000):
    res = rewardFun()
    if res not in resultDict:
        resultDict[res] = 1
    else:
        resultDict[res] += 1

for k,v in resultDict.items():
    print(k,'------>',v)
