class A(object):
    def __init__(self, age=0, name='zzz'):
        self.__age = age
        self.__name = name

    def show(self):
        print(self.__age, self.__name)


class C():
    def __index__(self, maj=2222222222222):
        self.maj = maj

    def showmaj(self):
        print(self.maj)


class B(A):
    def __init__(self, age, name, sex):
        super(B, self).__init__(age, name)
        self.sex = sex
        self.maj = C()

    def show(self):
        super(B, self).show()
        print(self.sex)


a = A(0, 'zzz')
a.show()
b = B(2, 'zx3', 'man')
b.show()
b.maj.showmaj()
