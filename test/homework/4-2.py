a = int(input())
if ((a % 4 != 0) or (a % 100 == 0 and a % 400 != 0)):
    print("不是闰年")
else:
    print("闰年")
