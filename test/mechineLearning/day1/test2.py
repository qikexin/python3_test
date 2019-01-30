# -*- conding:utf-8 -*-
# 2019/1/29
# Author: lpw
# Description :
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

def countvec():
    """
    对文本进行特征值化
    第一步：分词，将文章中所有的单词去重，且不包括单个字母，返回单词列表
    第二步：对每篇文章，在词的列表中进行标记
    :return: None
    """
    data = ["life is short,i like python","life is to long,i dislike python"]
    cv = CountVectorizer()
    result = cv.fit_transform(data)
    print(cv.get_feature_names())
    print(result.toarray())
    return None

def hanzivec():
    """
    中文分词
    :return:
    """
if __name__ == '__main__':
    countvec()