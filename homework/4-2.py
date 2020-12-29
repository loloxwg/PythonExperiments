# 闰年判断
try:
    a = int(input("请输入年份"))
except ValueError:
    print("请输入数字")
else:
    if ((a % 4 != 0) or (a % 100 == 0 and a % 400 != 0)):
        print("不是闰年")
    else:
        print("是闰年")

x = input('Please input an integer of 4 digits meaning the year:')
x = eval(x)
if x % 400 == 0 or (x % 4 == 0 and not x % 100 == 0):
    print('Yes')
else:
    print('No')
