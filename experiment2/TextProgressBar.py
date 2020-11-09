# Text progress bar

# 文本进度条：编程通过格式化字符串输出和时间延迟实现控制台风格文
import time as t
scale = 10
print("{0:*^16}".format("执行开始"))
start =t.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur=t.perf_counter()-start
    # print("{0:^3.0f}%[{1}->{2}]".format(c,a,b))
    print("\r{:1.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur))
    t.sleep(.1)
print("{0:*^16}".format("执行结束"))
