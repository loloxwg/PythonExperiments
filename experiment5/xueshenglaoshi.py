class Person():

    def __init__(self, NAME, ID):
        self.name = NAME
        self.id = ID


class Student(Person):

    def __init__(self, NAME, ID, AGE, CLASS, GRADE):
        super().__init__(NAME, ID)
        self.age = AGE
        self.cl = CLASS
        self.sc = GRADE
        print(self.name, self.id, self.age, self.cl, self.sc)


class Teacher(Person):
    def __init__(self, NAME, ID, ZHICHEN, BUMEN):
        super().__init__(NAME, ID)
        self.zc = ZHICHEN
        self.bm = BUMEN
        print(self.name, self.id, self.zc, self.bm)



stu1 = Student("zxw", 2020230034, 22,812001, 20)
tea1 = Teacher("hy", 1001, "教授", "自动化")

if __name__=='__main__':
    print(1)