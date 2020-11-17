class Dimension3(object):
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

    def add(self, another):
        X=self.x + another.x
        Y=self.y + another.y
        Z=self.z + another.z
        print("加法=（{}，{}，{}）".format(X,Y,Z))
    def sub(self, another):
        X=self.x = another.x
        Y=self.y = another.y
        Z=self.z = another.z
        print("减法=（{}，{}，{}）".format(X, Y, Z))
    def chen(self, another):
        X=self.x * another.x
        Y=self.y * another.y
        Z=self.z * another.z
        print("乘法=（{}，{}，{}）".format(X, Y, Z))
    def chu(self, another):
        X=self.x / another.x
        Y=self.y / another.y
        Z=self.z / another.z
        print("除法=（{}，{}，{}）".format(X, Y, Z))

c1 = Dimension3(1, 2, 3)
c2 = Dimension3(2, 3, 4)

c1.add(c2)

c1.chen(c2)
c1.chu(c2)
c1.sub(c2)
