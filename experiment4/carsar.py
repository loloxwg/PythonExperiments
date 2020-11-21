def Caesar(string, n):
    for i in range(0, len(string)):
        if 'A' <= string[i] <= 'Z':
            # 减去相对位置，以及偏移量
            num = ord(string[i]) - 65 - n
            # 加上相对位置
            s = chr(num % 26 + 65)
            print(s, end="")
        if 'a' <= string[i] <= 'z':
            num = ord(string[i]) - 97 - n
            s = chr(num % 26 + 65 + 32)
            print(s, end="")
    print("")


if __name__ == "__main__":
    Caesar("Fdhvdu", 3)
