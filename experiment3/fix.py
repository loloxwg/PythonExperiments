num1 = input('请输入数字1：')
if num1.strip() == '':
    print('输入错误。')
    exit()
elif num1[0] != '.':
    for i in num1:
        if not ('0' <= i <= '9' or i == '.'):
            print('输入错误。')
            exit()
    num1 = float(num1)
else:
    print('输入错误。')
    exit()
num2 = input('请输入数字2：')
if num2.strip() == '':
    print('输入错误。')
    exit()
elif num2[0] != '.':
    for i in num2:
        if not ('0' <= i <= '9' or i == '.'):
            print('输入错误。')
            exit()
    num2 = float(num2)
else:
    print('输入错误。')
    exit()
su = num1 + num2
su = [str(su), int(su)][int(su) == su]
num1 = [str(num1), int(num1)][int(num1) == num1]
num2 = [str(num2), int(num2)][int(num2) == num2]

print('{} + {} = {}'.format(num1, num2, su))