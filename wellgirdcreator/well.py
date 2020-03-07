#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Copyright (C) 2020 JIA Haowei WANG Shengyuan 
E-mail contact: nv4dll@outlook.com
'''
import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np 
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
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
#TODO merge this into wellgird


class gridconstucter():
		
	"""
	读取已有网格并画图
	"""

	def __init__(self,dat):

		self.findgird(dat)
		self.drawgrid()

	def findgird(self,dat):
		#TODO 添加读取角点网格
		#寻找网格定义关键字
		for i in range(0,len(dat)):
			#i.index("VARI")
			try:
				dat[i].index("VARI")
			except ValueError :
				i += 1
			else:
				self.gridx = int(dat[i][2])
				self.gridy = int(dat[i][3])
				self.gridz = int(dat[i][4])

		#寻找di dj 
		for i in range(0,len(dat)):	
			try:	
				dat[i].index("DI")
			except ValueError :
				i += 1
			else:
				if dat[i][1] == "IVAR" or dat[i][1] == "ALL":

					a = dat[i+1]
					a = a[0].split('*', maxsplit=-1)
					if  len(a) == 1 :
						self.di = float(a[0])
					else : 
						self.di = float(a[1])

				elif dat[i][1] == "CON":

					self.di = float(dat[i][2])
		for i in range(0,len(dat)):	

			try:	
				dat[i].index("DJ")
			except ValueError :
				i += 1
			else:
				if dat[i][1] == "JVAR" or dat[i][1] == "ALL":

					a = dat[i+1]
					a = a[0].split('*', maxsplit=-1)
					if  len(a) == 1 :
						self.dj = float(a[0])
					else : 
						self.dj = float(a[1])

				elif dat[i][1] == "CON":

					self.dj = float(dat[i][2])
					
		for i in range(0,len(dat)):	

			try:	
				dat[i].index("DK")
			except ValueError :
				i += 1
			else:
				if dat[i][1] == "KVAR" or dat[i][1] == "ALL":
					
					a = dat[i+1]
					a = a[0].split('*', maxsplit=-1)

					if  len(a) == 1 :
						self.dk = float(a[0])
					else : 
						self.dk = float(a[1])

				elif dat[i][1] == "CON":

					self.dk = float(dat[i][2])
	
	def drawgrid(self):
		#画网格
		#网格起点、终点、数量
		#vlines1 = np.linspace(0, self.di*self.gridx, self.gridx+1)
		#hlines1 = np.linspace(0, self.dj*self.gridy, self.gridy+1)
		vlines2 = np.linspace(0+self.di/2, self.di*(self.gridx)+self.di/2, self.gridx+1)
		hlines2 = np.linspace(0+self.dj/2, self.dj*(self.gridy)+self.di/2, self.gridy+1)
		#plt.hlines(hlines1, min(vlines1), max(vlines1), colors='.25', linewidth=.75) 
		#plt.vlines(vlines1, min(hlines1), max(hlines1), colors='.25', linewidth=.75) 
		plt.hlines(hlines2, min(vlines2), max(vlines2), colors='.25', linewidth=.75) 
		plt.vlines(vlines2, min(hlines2), max(hlines2), colors='.25', linewidth=.75) 
		
		#网格编号部分 
		#xs, ys = np.meshgrid(vlines[1:], hlines[:-1])
		#for i, (x, y) in enumerate(zip(xs.flatten(), ys.flatten())):
		#	plt.text(x, y, int(i+1), horizontalalignment='right', verticalalignment='bottom')
		#plt.axis('off')
		 	
		#plt.show()

class wellgrid():
	"""
	构造井网\n
	grid：暂时没用。\n
	wellgridtype：井网类型，包括："line"、"fourpoint"、"reversedfourpoint"、"fivepoint"、"reversedfivepoint"、"ninepoint"。\n
	x = [x方向起点，x方向终点，步长]（网格单位，并非实际长度）。\n
	y = [y方向起点，y方向终点，步长]（网格单位，并非实际长度）。\n
	STGP:生产井定产。\n
	BHPP:生产井定压。\n
	STWI:注水井定注入量。\n
	BHPI:注水井定压。\n
	INCOMP:注入成分（注水井为"WATER",生产井不需要）。\n
	"""
	#todo 排除已有井网
	def __init__(self,grid,wellgirdtype,x,y,STGP,BHPP,STWI,BHPI,INCOMP):
		
		self.line = False
		#四点
		self.fourpoint = False
		#反四点
		self.reversedfourpoint = False	
		#五点
		self.fivepoint = False
		#反五点
		self.reversedfivepoint = False
		#九点
		self.ninepoint = False
		self.check(grid,x,y)
		self.wellplan(grid,wellgirdtype,x,y,STGP,BHPP,STWI,BHPI,INCOMP)

	def check(self,grid,x,y):
		if x[1] > grid.gridx :
			raise Exception("x方向上限超过了网格上限！")
		elif y[1] > grid.gridy:
			raise Exception("y方向上限超过了网格上限！")
		elif x[0] < 0 or y[0]  < 0 or x[1]  < 0  or y[1]  < 0 :
			raise Exception("x、y方向起始点均应大于0！")
		elif x[1] < x[0] or y[1]  < y[0] :
			raise Exception("x、y方向起点应小于终点！")

	def wellplan(self,grid,wellgirdtype,x,y,STGP,BHPP,STWI,BHPI,INCOMP):

		if wellgirdtype == "line":
			self.line = True
		elif wellgirdtype == "fourpoint":
			self.fourpoint = True
		elif wellgirdtype == "reversedfourpoint":
			self.reversedfourpoint = True
		elif wellgirdtype == "fivepoint":
			self.fivepoint = True
		elif wellgirdtype == "reversedfivepoint":
			self.reversedfivepoint = True
		elif wellgirdtype == "ninepoint":
			self.ninepoint = True
		else:
			raise ValueError("应给出正确的井网类型!") 

		#井网x起点
		xstart = x[0]
		xend = x[1]
		deltax = x[2]
		#井网y起点
		ystart = y[0]
		yend = y[1]
		deltay = y[2]
		#九点法x、y方向井排数应为奇数
		xcount =  (xend - xstart)//deltax
		ycount = (yend - ystart)//deltay
		xstart2 = xstart+deltax//2
		xend2 = xend-deltax//2

		ystart2 = ystart+deltay//2
		yend2 =  yend-deltay//2

		self.xcoord = []
		self.ycoord = []
		self.zcoord = []
		#1为生产井，0为注入井
		self.welltype = []
		self.operatetype =[[] for i in range(2)]
		self.incomp = []

		if self.fourpoint == True:
			n = 0 
			for i in range (xstart,xend+1,deltax):
				for j  in range (ystart,yend+1,deltay):
					if n == 0 or  n % 2 == 0:
						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(1)
						self.operatetype[0].append (STGP)
						self.operatetype[1].append (BHPP)
						self.incomp.append("N/A")
					else:
						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(0)
						self.operatetype[0].append (STWI)
						self.operatetype[1].append (BHPI)
						self.incomp.append("WATER")
					n += 1
				n += 1

		if self.reversedfourpoint == True:

			n = 0 
			for i in range (xstart,xend+1,deltax):
				for j  in range (ystart,yend+1,deltay):
					if  n % 2 != 0:
						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(1)
						self.operatetype[0].append (STGP)
						self.operatetype[1].append (BHPP)
						self.incomp.append("N/A")
					else:

						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(0)
						self.operatetype[0].append (STWI)
						self.operatetype[1].append (BHPI)
						self.incomp.append("WATER")
					n += 1
				n += 1

		if self.line == True :

			n = 0
			for i in range (xstart,xend+1,deltax):
				for j  in range (ystart,yend+1,deltay):
					self.xcoord.append(i)
					self.ycoord.append(j)
					self.zcoord.append(1)
					if n==0 :
						self.welltype.append(1)
						self.operatetype[0].append (STGP)
						self.operatetype[1].append (BHPP)
						self.incomp.append("N/A")
						n += 1 
					else :
						self.welltype.append(0)
						self.operatetype[0].append (STWI)
						self.operatetype[1].append (BHPI)
						self.incomp.append("WATER")
						n=0

		if self.fivepoint == True:

			for i in range (xstart,xend+1,deltax):
				for j  in range (ystart,yend+1,deltay):
					self.xcoord.append(i)
					self.ycoord.append(j)
					self.zcoord.append(1)
					self.welltype.append(1)
					self.operatetype[0].append (STGP)
					self.operatetype[1].append (BHPP)
					self.incomp.append("N/A")
			for i in range (xstart2,xend2+1,deltax):
				for j  in range (ystart2,yend2+1,deltay):
					self.xcoord.append(i)
					self.ycoord.append(j)
					self.zcoord.append(1)
					self.welltype.append(0)
					self.incomp.append("WATER")
					self.operatetype[0].append (STWI)
					self.operatetype[1].append (BHPI)	

		if self.reversedfivepoint == True:

			for i in range (xstart,xend+1,deltax):
				for j  in range (ystart,yend+1,deltay):
					self.xcoord.append(i)
					self.ycoord.append(j)
					self.zcoord.append(1)
					self.welltype.append(0)
					self.operatetype[0].append (STWI)
					self.operatetype[1].append (BHPI)	
					self.incomp.append("WATER")
			for i in range (xstart2,xend2+1,deltax):
				for j  in range (ystart2,yend2+1,deltay):
					self.xcoord.append(i)
					self.ycoord.append(j)
					self.zcoord.append(1)
					self.welltype.append(1)	
					self.operatetype[0].append (STGP)
					self.operatetype[1].append (BHPP)
					self.incomp.append("N/A")

		if self.ninepoint == True:

			if xcount % 2 == 0 or ycount % 2 == 0 :
				raise ValueError("9点法井排数应为奇数!") 
			#i方向第几排
			i2 = 0
			#j方向第几排
			j2 = 0  
			for i in range (xstart,xend,deltax):
				for j  in range (ystart,yend,deltay):
					if  i2 % 2 == 0 :
						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(0)
						self.operatetype[0].append (STWI)
						self.operatetype[1].append (BHPI)
						self.incomp.append("WATER")
					elif i2 % 2 != 0 and j2%2 == 0:
						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(1)
						self.operatetype[0].append (STGP)
						self.operatetype[1].append (BHPP)	
						self.incomp.append("N/A")
					else:

						self.xcoord.append(i)
						self.ycoord.append(j)
						self.zcoord.append(1)
						self.welltype.append(0)
						self.operatetype[0].append (STWI)
						self.operatetype[1].append (BHPI)
						self.incomp.append("WATER")
					j2 += 1
				i2 += 1

		#井总数	
		self.wellcount = len(self.xcoord)
		#画图红色生产井 蓝色注水井
		for i in range (0,len(self.xcoord)):

			if self.welltype[i] == 1 :

				plt.scatter(self.xcoord[i]*grid.di,self.ycoord[i]*grid.dj,color="w",linewidths=1,s=50,edgecolors='red')

			else:

				plt.scatter(self.xcoord[i]*grid.di,self.ycoord[i]*grid.dj,color="w",linewidths=1,s=50,edgecolors='blue')

	def datwirter(self):

		#写入dat文件
		self.wellname = []
		localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
		with open("well"+localtime+".dat","a") as f:  
			for i in range(0,self.wellcount):
				if self.welltype[i] == 1:
					self.welltype.append("PRODUCER")
					self.wellname.append("PRODUCER"+str(i+1))
				elif self.welltype[i] == 0 :
					self.welltype.append("INJECTOR")
					self.wellname.append("INJECTOR"+str(i+1))

			for i in range(0,self.wellcount):

				f.write("WELL    "+"'Well "+str(self.wellname[i])+"'"+"\n")
				
				if self.welltype[i] == 1 :
					f.write("PRODUCER"+" 'Well "+str(self.wellname[i])+"'"+"\n")
					f.write("OPERATE  MAX  STG " + str(self.operatetype[0][i])+" CONT"+"\n")
					f.write("OPERATE  MIN  BHP " + str(self.operatetype[1][i])+" CONT"+"\n") 
				elif self.welltype[i] == 0 :
					f.write("INJECTOR"+" 'Well "+str(self.wellname[i])+"'"+"\n")
					f.write("INCOMP  "+self.incomp[i]+"\n")
					f.write("OPERATE  MAX  STW " + str(self.operatetype[0][i])+ " CONT"+"\n")
					f.write("OPERATE  MAX  BHP " + str(self.operatetype[1][i])+" CONT"+"\n") 

				f.write("**          rad  geofac  wfrac  skin"+"\n")
				f.write("GEOMETRY  K  0.0762  0.37  1.0  0.0"+"\n")
				f.write("      PERF      GEOA  "+"'Well "+str(self.wellname[i])+"'"+"\n")
				f.write("** UBA               ff          Status  Connection"+"\n")  
				
				f.write(str(self.xcoord[i])+" "+str(self.ycoord[i])+" "+str(self.zcoord[i])+"         ")
				if self.welltype[i] == 1 :
					f.write("1.0  OPEN    FLOW-TO  'SURFACE'"+"\n")
				elif self.welltype[i] == 0 :
					f.write("1.0  OPEN    FLOW-FROM  'SURFACE'"+"\n")
				f.write("\n")


def main():
	#一下两步不是完全需要
	dat = datreader("Ji2-25.dat")		
	gird = gridconstucter(dat)
	#x、y方向起点、终点、步长：网格单位
	x=[2,10,2]
	y=[2,10,2]

	STGP=0.5
	BHPP=100.
	STWI=0.1
	BHPI=10000
	INCOMP = "WATER"

	wellgrid1 = wellgrid(gird,"fourpoint",x,y,STGP,BHPP,STWI,BHPI,INCOMP)
	wellgrid1.datwirter()
	
	#显示图
	plt.show()

if __name__ == '__main__':
	
	main()