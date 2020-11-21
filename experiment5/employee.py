class Employee():
    def __init__(self, Name, Id, Basic):
        self.name = Name
        self.id = Id
        self.bisic = Basic

    def display(self):
        print(self.name, self.id, self.bisic)


class Saler(Employee):
    def __init__(self, Name, Id, Basic):
        super().__init__(Name, Id, Basic)
        self.sales = self.bisic*0.1

    def display(self):
        print(self.name, self.id, self.sales)

class Manager():
    def __init__(self,Name,Id):
        self.name=Name
        self.id=Id
        self.money=8000
    def display(self):
        print(self.name,self.id,self.money)


class SManager(Saler,Manager):
    def __init__(self,Name,Id,Basic):
        super().__init__(Name,Id,Basic)
        self.fixmoney=5000
        self.basic=Basic
        self.sales=self.fixmoney+self.basic*0.05
    def display(self):
        print(self.name,self.id,self.sales)
if __name__ == '__main__':
    employee = Employee("标准员工", "000", 10000)
    employee.display()
    saler = Saler("销售员", "001", 10000)
    saler.display()
    manager=Manager("经理","002")
    manager.display()
    smanager=SManager("销售经理","003",10000)
    smanager.display()