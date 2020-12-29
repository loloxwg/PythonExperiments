class Dimension3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Add(self, another):
        X = self.x + another.x
        Y = self.y + another.y
        Z = self.z + another.z
        print("add（{}，{}，{}）".format(X, Y, Z))

    def Sub(self, another):
        X = self.x = another.x
        Y = self.y = another.y
        Z = self.z = another.z
        print("sub（{}，{}，{}）".format(X, Y, Z))

    def Mult(self, another):
        X = self.x * another.x
        Y = self.y * another.y
        Z = self.z * another.z
        print("mult（{}，{}，{}）".format(X, Y, Z))

    def Div(self, another):
        X = self.x / another.x
        Y = self.y / another.y
        Z = self.z / another.z
        print("div（{}，{}，{}）".format(X, Y, Z))


c1 = Dimension3(1, 2, 3)
c2 = Dimension3(2, 4, 6)

c3add = c1.Add(c2)
c3sub = c1.Sub(c2)
c3mult = c1.Mult(c2)
c3div = c1.Div(c2)


#print("add{},sub{},mult{},div{}".format(c3add,c3sub,c3mult,c3div))