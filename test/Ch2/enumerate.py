a=list(enumerate("abcd"))

b=list(enumerate({'a':97,'b':33,'c':55}.items()))
#枚举字典中的元素
c=list(enumerate(["hhhhhh","gtgggggg"]))
#枚举列表中的元素

for index,value in enumerate(range(10,15)):
    print((index,value))

    print(index,end=" ")

    print(value,end=" ")

 #枚举range对象中的元素