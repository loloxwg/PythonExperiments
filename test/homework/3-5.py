x=input()
xlist=x.split(",")
xlist=[int(xlist[i]) for i in range(len(xlist))]
print(xlist)
a=int(input())
b=int(input())
w=xlist[a:b+1]
print(w)

