class A():
    def __init__(self, age=0, name='zzz'):
        self.__age = age
        self.__name = name

    def show(self):
        print(self.__age, self.__name)


class C():
    def __init__(self, id=2020):
        self.id = id

    def show_id(self):
        print(str(self.id))


class B(A):
    def __init__(self, age, name):
        super(B, self).__init__(age, name)
        self.sex = 20
        self.maj = C()  # 实例用作了属性

    def show(self):
        super(B, self).show()
        print(self.sex)


a = A(0, 'zzz')
a.show()
b = B(2, 'zx3')
b.show()
b.maj.show_id()
