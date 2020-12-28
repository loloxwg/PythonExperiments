import string
import random
x=string.digits+string.ascii_letters+string.punctuation
print(x)
def generateStrongPwd(k):
    '''生成指定长度密码字符串'''
    return ''.join(random.choice(x)for i in range(k))

print(random.choice(x))
a=generateStrongPwd(8)
print(a)
