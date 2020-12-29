class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __rmul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar, self.z * scalar)

    # 空间坐标
    def __repr__(self):
        return 'Point({0.x!r}, {0.y!r}, {0.z!r})'.format(self)

    # 两点是否是同一点
    def isEqual(self, other):
        if (self.x == other.x) and (self.y == other.y) and (self.z == other.z):
            return True
        else:
            return False

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    # 复制该点
    def copy(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z


class Vector(Point):
    def __init__(self, x=0.0, y=0.0, z=0.0, i=0.0, j=0.0, k=0.0):
        Point.__init__(self, x, y, z)
        self.n = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        self.a = (x / self.n)
        self.b = (y / self.n)
        self.c = (z / self.n)
        self.i = i
        self.j = j
        self.k = k

    @property
    # 向量模
    def norm(self):
        return 'Norm = {0.n!r}'.format(self)

    @property
    # 单位向量
    def unit(self):
        return 'Unit({0.a!r}, {0.b!r}, {0.c!r})'.format(self)

    # 向量点乘
    def dot(self, other):
        self.x = self.x * other.x
        self.y = self.y * other.y
        self.z = self.z * other.z
        return 'Dot({0.x!r}, {0.y!r}, {0.z!r})'.format(self)

    # 向量叉乘
    def cross(self, other):
        self.i = self.y * other.z - self.z * other.y
        self.j = self.z * other.x - self.x * other.z
        self.k = self.x * other.y - self.y * other.x
        return 'Cross({0.i!r}, {0.j!r}, {0.k!r})'.format(self)

    # 向量和
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return 'Add({0.x!r}, {0.y!r}, {0.z!r})'.format(self)

    # 向量差
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return 'Add({0.x!r}, {0.y!r}, {0.z!r})'.format(self)


V1 = Vector(1, 2, 1)
V2 = Vector(1, 1, 1)
V3 = V1.__add__(V2)
print(V3)