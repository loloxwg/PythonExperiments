# 读写文本文件并添加行号


# lst1 = ['0\n' for i in range(100)]
# lst2 = [str(i)+'\n' for i in range(100)]
#
# with open(filename, 'w') as fp:
#     fp.writelines(lst1)
#     fp.writelines(lst2)
# fp.close()
filename = 'area.txt'
with open(filename, 'r',encoding="UTF_8") as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))
fp.close()

lines = ['#'+str(index)+line.rstrip().ljust(maxLength)+'\n' for index, line in enumerate(lines)]
with open(filename[:-4]+'new.txt', 'w') as fp:
    fp.writelines(lines)
fp.close()