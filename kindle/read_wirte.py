#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Copyright (C) 2020 JIA Haowei WANG Shengyuan 
E-mail contact: nv4dll@outlook.com
'''
import time
import numpy as np
import csv
import urllib.parse
import http.client
import random
import hashlib
import unicodedata
import time
# 通过在http://ai.youdao.com/ 执行以下操作获取
# 1.注册账号 => 2.创建应用 => 3.创建实例 => 4.应用绑定对象
YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '35640b55cf2ae4dc'
APP_SECRET = 'p8x18zLRzIF45NFH47X36xemzoWy2qPy'
 
# 英译中
def En2Ch(item):
    httpClient = None
    myurl = '/api'
 
    fromLang = 'EN' # 译文主体
    toLang = 'zh-CHS' # 译文客体
 
    salt = random.randint(1, 65536)
    sign = APP_KEY + item + str(salt) + APP_SECRET
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + APP_KEY + '&q=' + urllib.parse.quote(
        item) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    result = ""
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = eval(response.read().decode("utf-8"))['translation']
    except Exception as e:
        print(e)
        print(item)
    finally:
        if httpClient:
            httpClient.close()
    return result

def datreader(filename):
	#读取dat文件
	data = open(filename,encoding='utf-8').readlines()
	return data

def getwords(data):
	
	index = np.arange(3,len(data),5)
	words = []
	count = 0
	for i in index:
		words.append(data[i].rstrip(',\n'))
		count += 1
		words[count-1]=words[count-1].rstrip('.')
		words[count-1]=words[count-1].rstrip('.■')
		words[count-1]=words[count-1].lstrip('“')
		words[count-1]=words[count-1].rstrip('”')
		#print(words[count-1])
	wordsf = list(set(words))
	wordsf.sort(key=words.index)
	return wordsf

def trasnlate(item):
	ch_words =[]
	for i in item:
		result = En2Ch(i)
		try :
			ch_words.append(result[0])
		except IndexError :
			ch_words.append('翻译失败')
		#time.sleep(0.2)
	return ch_words

def wirtedata(io1,io2):
	with open('words.csv','w',newline='',encoding='utf_8_sig') as csvFile:
		writer = csv.writer(csvFile)
		#先写columns_name
		writer.writerow(["EN","CH"])
		for i in range(len(io1)):
			try:
				writer.writerow([io1[i],io2[i]])
			except UnicodeEncodeError:
				writer.writerow([io1[i][:50],''])

if __name__ == "__main__":
	'''
	#debug 使用：
	enwords = ['apple',' ']
	chwords = trasnlate(enwords)
	'''
	data = datreader("My Clippings.txt")
	enwords = getwords(data)
	chwords = trasnlate(enwords)
	wirtedata(enwords,chwords)
