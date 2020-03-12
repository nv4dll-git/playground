import csv
import numpy as np

#读取CSV
with open('1.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    result = list(reader)
    nplist = np.asarray(result[1:][:])
    print(nplist[:,0])
    print(nplist[:,1])
    #print(result[0][:])

#写入CSV
a = np.zeros(10)
b = np.ones(10)

with  open('test.csv','w',newline='') as csvFile:
    writer = csv.writer(csvFile)
    #先写columns_name
    writer.writerow(["a_name","b_name"])
    for i in range(len(a)):
        writer.writerow([a[i],b[i]])
    #写入多行用writerows
    writer.writerows([[1,2],[3,4]])