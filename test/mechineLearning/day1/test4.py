# -*- conding:utf-8 -*-
# 2019/1/30
# Author: lpw
# Description :
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler,Imputer
import numpy
from sklearn.feature_selection import VarianceThreshold

def mm():
    mm =  MinMaxScaler()
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)

def stand():
    std = StandardScaler()
    data = std.fit_transform([[1,-1,3],[2,4,2],[4,6,-1]])
    print(data)
def im():
    """
    缺失值处理
    :return: None
    """
    im = Imputer(missing_values="Nan",strategy='mean',axis=0)
    data = im.fit_transform([1,2],[np.nan,3],[7,6])
    print(data)
    return None

def var():
    """
    特征选择-删除低方差的特征

    :return:
    """
if __name__ == '__main__':
    mm()
    print("========")
    stand()