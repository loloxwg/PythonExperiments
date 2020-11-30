from sklearn.neighbors import KNeighborsClassifier
"""
使用python程序模拟KNN算法


"""
import numpy as np
import collections as cs

data = np.array([
    [203, 1], [126, 1], [89, 1], [70, 1], [196, 2], [211, 2], [221, 2], [311, 3], [271, 3]
])
feature = data[:, 0]  # 特征
print(feature)

label = data[:, -1]  # 结果分类
print(label)

predictPoint = 200  # 预测数据
print("预测输入特征为：" + str(predictPoint))

distance = list(map(lambda x: abs(predictPoint - x), feature))  # 各点到预测点的距离
print(distance)

sortIndex = np.argsort(distance)  # 排序，返回排序后各数据的原始下标
print(sortIndex)

sortLabel = label[sortIndex]  # 根据下标重新进行排序
print(sortLabel)

# k = 3 # 设置k值大小为3

for k in range(1, label.size + 1):
    result = cs.Counter(sortLabel[0:k]).most_common(1)[0][0]  # 根据k值计算前k个数据中出现次数最多的分类，即为预测的分类
    print("当k=" + str(k) + "时预测分类为：" + str(result))
