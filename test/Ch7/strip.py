x = '\n\n\nhello world\t'
'''删除两端连续空白字符或指定字符'''
print(x.strip())
y = 'bbbbbbaaaaaaabb'
print(y.strip('b'))

z = 'bbbkkkkkkaa'
print(z.strip('ba'))

'''判断是否是数字字符，里边有个‘.’所以不是'''
a = "1234.0".isdigit()
print(a)

print(type("1234.0"))
'''center(),ljust(),rjust()'''
print("hello".center(20, '-'))
print("hello".ljust(20, '#'))

'''zfill()'''
print('abc'.zfill(5))
print('abc'.zfill(2))

'''input()输入的全是字符串型'''
# x=input('input a list:')
# print(type(x))
# print(x)
# eval(x)
# print(x)
# print(type(print("hello")))

''''''

path="hello world"
print(path[:-4])
print(path[-4:])
# hello w
# orld