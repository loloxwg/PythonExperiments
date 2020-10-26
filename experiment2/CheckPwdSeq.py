# password = input("请输入你的密码：")
 # p = list(password)
# x = 0
# for i in p:
#     if i == " ":
#         x = 1
# if x == 1:
#     print("密码格式不对")  # 密码中不能包含空格
# elif password.isdigit() == True or password.isalpha() == True:  # 全为数字或字母
#     print("安全强度：弱")
# elif password.isalnum() == True:  # 只有数字和字母
#     print("安全强度：中")
# else:
#     print("安全强度：强")  # 密码包含数字、字母、特殊符号时安全强度为强

import string

password = input("请输入你的密码：")
def check(pwd):
    # 密码必须至少包含6个字符
    if not isinstance(pwd, str) or len(pwd) < 6:
        return 'not suitable for password'
    # 密码强度等级与包含字符种类的对应关系
    d = {1: 'weak', 2: 'below middle', 3: 'above middle', 4: 'strong'}
    # 分别用来标记pwd是否含有数字、小写字母、大写字母和指定的标点符号
    r = [False] * 4
    for ch in pwd:
        # 是否包含数字
        if not r[0] and ch in string.digits:
            r[0] = True
        # 是否包含小写字母
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        # 是否包含大写字母
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        # 是否包含指定的标点符号
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True
    # 统计包含的字符种类，返回密码强度
    return d.get(r.count(True), 'error')


print(check(password))
