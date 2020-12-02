class Person():

    def __init__(self, name="", age=20, sex="man"):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSex(self, sex):
        self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex)


class Student(Person):
    def __init__(self, name='', age=20, sex='man', sdept='CS'):
        super(Student, self).__init__(name, age, sex)
        self.setSdept(sdept)

    def setSdept(self, sdept):
        self.__sdept = sdept

    def show(self):
        super(Student, self).show()
        print(self.__sdept)



a = Person("Tom", 100, "man")
a.show()

stu = Student("Jerry", 20, 'woman', "CS")
stu.show()

stu.setSdept("EE")
stu.setAge(99)
stu.setSex("men")
stu.show()
