with open('data.txt', 'r') as fp:
    data=fp.readlines()
data=[line.strip() for line in data]
data=','.join(data)
data=data.split(',')
data=[int(item) for item in data]
data.sort()
data=','.join(map(str,data))
with open('data_asc.txt', 'w') as fp:
    fp.write(data)

