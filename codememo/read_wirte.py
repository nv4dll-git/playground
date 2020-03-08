#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2020 JIA Haowei WANG Shengyuan 
E-mail contact: nv4dll@outlook.com
'''
import time
def datreader(filename):
	#读取dat文件
	file = open(filename)
	count = 0
	for index, line in enumerate(open(filename,'r')):
		count += 1
	dataslines = file.readlines()
	row = [ [ [] for i in range (5) ] for i in range(count) ]
	for i in range (0,count):
		row[i] = dataslines[i].split()
	return row
io=[]
localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
with open("well"+localtime+".dat","a") as f:  
	for i in range(0,io):
		f.write("\n")