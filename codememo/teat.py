import numpy as np
tes = np.array([1,2,3])
weight = np.ones(3)#计算卷积  array([1., 3., 5., 3.])
# weight = weight*(1/2)#计算移动平均数  array([0.5, 1.5, 2.5, 1.5])
result = np.convolve(tes,weight)
print(result)