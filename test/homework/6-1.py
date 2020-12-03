class Person():

    def __init__(self, name="", age=20, sex="man"):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        # if not inistance(name,str):
        #     print("name must be string")
        #     return
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSex(self, sex):
        self.__sex = sex

    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)


class Student(Person):
    def __init__(self, name='', age=20, sex='man', sdept='CS'):
        super(Student, self).__init__(name, age, sex)
        self.setSdept(sdept)

    def setSdept(self, sdept):
        self.__sdept = sdept

    def show(self):
        super(Student, self).show()
        print(self.__sdept)


if __name__ == '__main__':

    a = Person("Tom", 100, "man")


    stu = Student("Jerry", 20, 'woman', "CS")
    stu.show()
    print("\n")
    stu.setSdept("EE")

    stu.show()
