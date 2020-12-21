import random as r
import pickle



first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋','川']
last_name = ['萱', '轩', '雨', '瑞', '军', '哈', '玲', '灵','卫滨','牧野','解放','建国']
address = ['龙亭', '顺河', '鼓楼', '禹王台', '祥符', '杞', '尉氏', '通许', '兰考']
shengfen = ['山西', '山东', '广东', '湖南', '四川']

# 新乡市---红旗区|卫滨区|凤泉区|牧野区|新乡县|获嘉县|原阳县|---延津县|封丘县|长垣市|卫辉市|辉县市
# 焦作市---解放区|中站区|马村区|山阳区|修武县|博爱县|武陟县|温县|沁阳市|孟州市
# # 濮阳市---华龙区|清丰县|南乐县|范县|台前县|濮阳县
# 许昌市---魏都区|建安区|鄢陵县|襄城县|禹州市|长葛市

def randName():
    for i in range(5):
        FirstName = r.choice(first_name)
        SecondName = "".join(r.choice(last_name))
        return FirstName + SecondName


# def Get_Name():
#
#     for i in range(5):
#         name = r.choice(first_name) + r.choice(last_name) + r.choice(last_name)
#     print(name)


def randEmail():
    end_index = ['@qq.com', '@163.com', '@gmail.com', '@outlook.com']
    first_index = ['A', 'B', 'C', 'D', 'E']

    for i in range(5):
        email = r.choice(first_index) + r.choice(first_index) + r.choice(end_index)
    return email


def randAddr():
    for i in range(5):
        StreetName = "".join(r.choice(shengfen)) + "省"
        CommunityName = "".join(r.choice(address)) + "市"
        No = r.randint(1, 99)
        return StreetName + CommunityName + str(No) + "号"


def randPerson():
    name = randName()
    email = randEmail()
    city = randAddr()
    info = "{},{},{}".format(name, email, city)

    return info


if __name__ == '__main__':
    filename = 'a.dat'
    with open(filename, 'wb') as fo:
        for i in range(10):
            pickle.dump(randPerson()+"\n",fo)

    with open(filename,"rb")as fo:
        for i in range(10):
            a=pickle.load(fo)
            print(a)

# -*-coding:utf-8-*-
# import os
# file_obj = open("test2.txt")
# all_lines = file_obj.readlines()
# for line in all_lines:
#   print line
# file_obj.close()
# # 写之前，先检验文件是否存在，存在就删掉
# if os.path.exists("dest.txt"):
#   os.remove("dest.txt")
