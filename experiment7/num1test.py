
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# 加载数据
X = np.array(
    [[1, 180, 85], [1, 180, 86], [1, 180, 90],
     [1, 180, 100], [1, 185, 120], [1, 175, 80],
     [1, 175, 60], [1, 170, 60],[1, 175, 90],
     [1, 175, 100], [1, 185, 90], [1, 185, 80]])
y = np.array(['稍胖', '稍胖', '稍胖',
              '过胖', '太胖', '正常',
              '偏瘦', '正常', '过胖',
              '太胖', '正常', '偏瘦'])
# print(y)

# 建立模型
model_knn = KNeighborsClassifier(n_neighbors=1)

# 特征缩放
ms = MinMaxScaler()
X = ms.fit_transform(X)

# 训练
model_knn.fit(X, y)
print(model_knn.score(X, y))
X_te = [[1, 180, 70], [1, 160, 90], [1, 170, 85]]
X_te = ms.fit_transform(X_te)
print(model_knn.predict(X_te))
'''
训练准确率是： 1.0
训练集测试数据如下：
 ['稍胖' '稍胖' '稍胖' '过胖' '太胖' '正常' '偏瘦' '正常' '过胖' '太胖' '正常' '偏瘦']
测试集测试数据如下：
 ['偏瘦' '太胖' '过胖']
'''
