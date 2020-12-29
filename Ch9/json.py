import json

with open('test.txt', 'w')as fp:
    json.dump({"a":1, 'b':2, 3: '4'}, fp)
with open('test.txt', 'r')as fp:

    print(json.load(fp))