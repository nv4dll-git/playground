import numpy as np
from scipy.optimize import minimize
import math
import csv

config = {  'xatol': 1e-6, # 精度
            'fatol' : 1e-6, # 精度
            'dim': 9 # 多少个变量
}

def func(x, Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp, Edmodel):
    # Ncom = Na**(x1) + Nrho**(x2) + Nmiu**(x3) + Nc**(x4) + Nb**(x5)
    # Ed =  a * math.log(Ncom) + b
    # 顺序按依次 Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp， 常数a ,常数b
    res = (Edmodel - x[7] * math.log(Na**(x[0]) * Nrho**(x[1]) * Nmiu**(x[2]) * Nc**(x[3]) * Nb**(x[4]) * Nw**(x[5])* Vdp**(x[6])) - x[8])**2
    return res

def fitmodel(i,Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp, Edmodel):

    x = np.zeros([config['dim']]) # 初始猜测值 每个变量都是0
    res = minimize(func,x,method='nelder-mead', 
                    args=(Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp, Edmodel),
                    options={'xatol': config['xatol'],'fatol':config['fatol'], 'disp': True})

    print("拟合结果方案：",i)
    print(res.x)
    print("sqrt error is:", func(res.x,Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp, Edmodel),'\n')

def splitdata(filename):
    with open(filename,'r',encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        result = list(reader)
        nplist = np.asarray(result[1:][:])
        nplist = nplist.astype(np.float)
        Na     = nplist[:,0]
        Nrho   = nplist[:,1]
        Nmiu   = nplist[:,2]
        Nc     = nplist[:,3]
        Nb     = nplist[:,4]
        Nw     = nplist[:,5]
        Vdp    = nplist[:,6]
        Edmodel= nplist[:,7]
    data = np.vstack((Na, Nrho, Nmiu, Nc, Nb, Nw, Vdp, Edmodel))

    split = [0,5,11,16,26,32,36,40,45,52,56,61,62] #数据按方案划分
    i = 0
    meanNa,meanNaNrho,meanNmiu,meanNc,meanNb,meanNw,meanVdp,meanEdmodel = [],[],[],[],[],[],[],[]
    for i in range(len(split)):
        if i < len(split)-1:
            meanNa.append(      np.mean(data[0,split[i]:split[i+1]]))
            meanNaNrho.append(  np.mean(data[1,split[i]:split[i+1]]))
            meanNmiu.append(    np.mean(data[2,split[i]:split[i+1]]))
            meanNc.append(      np.mean(data[3,split[i]:split[i+1]]))
            meanNb.append(      np.mean(data[4,split[i]:split[i+1]]))
            meanNw.append(      np.mean(data[5,split[i]:split[i+1]]))
            meanVdp.append(     np.mean(data[6,split[i]:split[i+1]]))
            meanEdmodel.append( np.mean(data[7,split[i]:split[i+1]]))
        else :
            pass
    print("get mean value for each set")
    data = np.vstack((meanNa, meanNaNrho, meanNmiu, meanNc, meanNb, meanNw, meanVdp, meanEdmodel))
    return data
if __name__ == "__main__":

    data = splitdata('data2.csv')
    print(data[0])
    for i in range(len(data[0])):
        fitmodel(i+1,data[0,i],data[1,i],data[2,i],data[3,i],data[4,i],data[5,i],data[6,i],data[7,i])