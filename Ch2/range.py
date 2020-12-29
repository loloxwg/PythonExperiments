#range()是Python开发中非常常用的一个内置函数，语法格式为range([start,] end [, step] )，有range(stop)、range(start, stop)和range(start, stop, step)三种用法。该函数返回具有惰性求值特点的range对象，其中包含左闭右开区间[start,end)内以step为步长的整数。参数start默认为0，step默认为1。


range(5)#start默认为0，step默认为1

a=list(range(1,10,2))

b=list(range(9,0,-2))

