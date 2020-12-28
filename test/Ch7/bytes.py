print(type("中国"))

a=type("中国".encode('gbk'))

print(a)

b="中国".encode().decode()
print(b)