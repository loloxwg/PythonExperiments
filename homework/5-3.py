# 字符串判断统计
def judge_element(str):
    low_element = 0
    up_element = 0
    digit_element = 0
    other_element = 0
    for element in str:
        if element.islower():
            low_element += 1
        elif element.isupper():
            up_element += 1
        elif '0'<=element<='9':
            digit_element += 1
        else:
            other_element += 1
    print(('大写字母的个数',up_element))
    print(('小写字母的个数',low_element))
    print(('数字的个数',digit_element))
    print(('其他字符的个数',other_element))
    tup=(up_element,low_element,digit_element,other_element)
    print(tup)
judge_element("wdxweWWWWhucuwuiy27177e3189&*((7")



###################################

def acc(w):
    M = m = n = d = 0
    for i in w:
        if 'A' <= i <= 'Z':
            M += 1
        elif 'a' <= i <= 'z':
            m += 1
        elif '0' <= i <= '9':
            n += 1
        else:
            d += 1

    return (M, m, n, d)


w = input('请输入：')
print(w)
print(acc(w))