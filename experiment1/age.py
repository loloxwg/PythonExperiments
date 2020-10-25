age = 27
print("猜年龄")
count = 0
while count < 3:
    input_age = int(input("请输入您猜测的数字:"))
    if age > input_age:
        print("您输入的数字小，请重试")
    elif age < input_age:
        print("您输入的数字大，请重试")
    else:
        print("Bingo!!!")
        break
    count += 1
else:
    print("输入太多次了，稍后再试。")
