'''
Copyright (C) 2020 nv4dll
E-mail contact: nv4dll@outlook.com
'''
import math
import numpy as np
import copy
import csv
import sys
import time
sys.setrecursionlimit(50000)

def getrandom(num,swant,kaverge):
    #klayer = np.array([1400,np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),np.random.randint(100,2000),0])
    mu = kaverge  #期望为1
    sigma = swant*kaverge  #标准差为3 #个数为10000
    klayer = np.random.normal(mu, sigma, num)
    #klayer[9] = kaverge - klayer.mean()
    return klayer
    
def check(num,k,swant,kaverge,converge):
    count = 0
    for i in range(len(k)):
        if k[i] < 0 or abs(k.mean()-kaverge)/kaverge > converge :
            k = getrandom(num,swant,kaverge)
            return check(num,k,swant,kaverge,converge)
        else:
            count += 1  
        if count == len(k):
            return k

def iterator(num,swant,kaverge,converge):
    r'''
    根据给出的平均值、长度和变异系数返回一个数组并储存为csv文件。
    ----------
    num : int 数组长度
    
    swant : float 目标变异系数

    kaverge : float 平均值
    
    converge : float 平均值误差

    '''
    e = 100
    i = 0 
    while e > 0.05:
        i += 1 
        k = getrandom(num,swant,kaverge)
        kpos = check(num,k,swant,kaverge,converge)
        stdk=np.std(kpos)
        snow = stdk/kaverge
        e = abs(snow - swant)
        kavg = kpos.mean()
        if i % 1000 == 0:
            print('第'+str(i)+"次迭代")
    print('变异系数为{s},渗透率序列为{k}，平均值为{a}'.format(s=snow,k=kpos,a=kavg))
    save2csv(kpos,str(swant))

def save2csv(k,name):
    localtime = time.strftime("%d-%H-%M-%S", time.localtime()) 
    with  open(name+"_"+localtime+".csv",'w',newline='') as csvFile:
        writer = csv.writer(csvFile)
        #先写columns_name
        writer.writerow(["k"])
        for i in range(len(k)):
            writer.writerow([k[i]])

if __name__ == "__main__":
    #
    iterator(num=10,swant=1.4,kaverge=1400,converge=0.05)

    


    