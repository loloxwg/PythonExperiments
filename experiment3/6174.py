# #!/usr/bin/env python3
# # coding:utf8
#
# import itertools
# s=list(itertools.combinations(range(10),4))
# flag=False
#
# for i in s:
#     snum=''.join(list(map(lambda x: str(x),i)))
#     count=0
#     flag=False
#     for j in range(7):
#         l=sorted(snum)
#         min=int(''.join(l))
#         max=int(''.join(reversed(l)))
#         if(max-min==6174):
#             flag=True
#             break
#         else:
#             snum=str(max-min)
#     if(flag==False):
#         break
#
#
# if(flag):
#     print('6174猜想正确！')
# else:
#     print('6174猜想错误！')
# 6174猜想：对任意各位数字不相同的四位数，使用各位数字能组
# 成的最大数减去能组成的最小数，对得到的差重复操作，最终能得到6174，
# 并且这个操作最多不会超过7次。
num=int(input())

c=num

while c!=6174:

    digits=list(str(c))

    digits.sort(reverse=True)#排列最大数和最小数

    if len(digits)<4:

        digits.append('0')

    a=int(''.join(digits))

    digits.reverse()

    b=int(''.join(digits))

    c=a-b

    print("%d-%d=%d" %(a,b,c))