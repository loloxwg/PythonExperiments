import random as r
import string as s
import pickle
first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋']
last_name = ['萱', '轩', '雨', '瑞', '军', '', '哈', '玲', '', '灵', '']

AddrDict=set()

def randName():
    FirstName = r.choice(first_name)
    SecondName = "".join(r.choice(last_name)
                         for i in range(r.randint(1, 2)))
    return FirstName+ SecondName



# def Get_Name():
#
#     for i in range(5):
#         name = r.choice(first_name) + r.choice(last_name) + r.choice(last_name)
#     print(name)


def randEmail():
    end_index = ['@qq.com', '@163.com', '@gmail.com', '@outlook.com']
    first_index = ['A', 'B', 'C', 'D', 'E']

    for i in range(5):
        email1 = r.choice(first_index) + r() + r.choice(end_index)
    return email1

def randAddr():

    StreetName = "".join(r.choice(last_name)
                         for i in range(r.randint(2, 3)))+"省"
    CommunityName = "".join(r.choice(first_name)
                            for i in range(r.randint(2, 4))) + "市"
    No = r.randint(1, 99)
    return StreetName + CommunityName + str(No) + "号"



def randPerson():
    name=randName()
    email=randEmail()
    city=randAddr()
    info = "{},{},{}".format(name, email,city)
    return info
if __name__ == '__main__':

    with open("a.txt", encoding="utf-8") as fo:
        # for line in fo.readlines():
        for line in fo.write(s):



