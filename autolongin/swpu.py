'''
Copyright (C) 2020 nv4dll
E-mail contact: nv4dll@outlook.com
'''
import time
import requests
import sys
import json

login_url = "http://xg.swpu.edu.cn/SPCP/Web/"
index_url = "http://xg.swpu.edu.cn/SPCP/Web/Report/Index"

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.34 Safari/537.36',
            'Referer': 'http://xg.swpu.edu.cn/SPCP/Web/'
        }

s = requests.Session()

def login(login_url):

    data = {
            'StuLoginMode': '1',
            'txtUid': '201821000713',
            'txtPwd': '19041x'
            #'codeInput': '9fmx'
    }

    response = s.post(url=login_url,data=data,headers=headers)
    #print(response)
    #print(response.text)

    # 若返回数据里有 首页 字眼，代表登录成功
    if "首页" in response.text:
        print("1. 登录成功")
    else:
        print("1. 登录失败")
        print((response.text).encode('utf-8'))
        sys.exit(1)

def getIndex(index_url):
    headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Account/ChooseSys'
    response = s.get(url=index_url,headers=headers)
    #print(response)
    #print(response.text)

    # 若返回数据里有 已登记 字眼，代表已登记
    if "当前采集日期已登记！" in response.text:
        print("2. 已登记！")
    else:
        print("2. 已登记！")
        print((response.text).encode('utf-8'))
        sys.exit(1)

def main():
    login(login_url)
    getIndex(index_url)


if __name__ == "__main__":
    main()
