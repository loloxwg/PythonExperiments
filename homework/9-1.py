import os

filename1 = "a.txt"
filename2 = "b.txt"
with open(filename1, 'r',encoding="utf-8") as f1:
    with open(filename2,'w', encoding="utf-8")as f2:
        # lines =f1.readlines()
        for line in f1.readlines():
            print(line.rstrip())
            f2.write(line.swapcase())
