import pickle

dic = {'TOM': 60, 'JERRY': 100, 'ALEX': 89, 'THUMP': 44}
filename = 'sc.dat'


with open(filename, 'wb')as file_object:
    pickle.dump(dic, file_object)

with open(filename, 'rb')as file_object:
    dict=pickle.load(file_object)
    print(dict)

