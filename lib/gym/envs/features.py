#-*- coding:utf-8 –*-

import numpy as np




class Features(object):
    def __init__(self):
        self.dim = 0
        self.name=""
        self.dtype=np.float32

    def byte_histogram(self,str):
        #bytes=np.array(list(str))
        bytes=[ord(ch) for ch in list(str)]
        #print bytes

        h = np.bincount(bytes, minlength=256)   ##将字符串转换为256维数据，因为ascii最大不超过256
        from more_itertools import chunked
        histogram = h.astype(self.dtype).flatten() / h.sum()
        return np.concatenate([
            [h.sum()],  # total size of the byte stream
            #[sum(x) / len(x) for x in chunked(histogram, 8)],  # normalized the histogram
            histogram
        ])
    ##状态空间为将字符串转换为ascii的256维向量，并且统计每个字符出现得的次数，然后每个字符出现次数除以总次数

    def extract(self,str):

        featurevectors = [self.byte_histogram(str)]
        return np.concatenate(featurevectors)


if __name__ == '__main__':
    f=Features()
    a=f.extract("alert()")
    print(a)
    print(a.shape)
    #print a.shape[0]