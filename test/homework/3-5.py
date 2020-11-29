#3-5
x=input("输入一个列表:")
xlist=x.split(",")
xlist=[int(xlist[i]) for i in range(len(xlist))]
print(xlist)
a=int(input("输入第一个下标:"))
b=int(input("输入第二个下标:"))
w=xlist[a:b+1]
print(w)

