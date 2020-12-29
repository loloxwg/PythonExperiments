class A(object):
    def __init__(self, value):
        self.__value = value

    def show(self):
        print(self.__value)


a = A(5)
a._A__value = 3
a.show()
