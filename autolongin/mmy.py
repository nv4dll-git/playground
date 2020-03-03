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
            'txtUid': '201821000685',
            'txtPwd': '04822x'
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

    if "当前采集日期已登记！" in response.text:
        print("2. 已登记！")
    else:
        print("2. 发送登记请求！")
        data={
          'StudentId': '201821000685',
          'Name': '马珉玥',
          'MoveTel': '13281870079',
          'Province': '300000',
          'City':'061000',
          'County':'062450',
          'ComeWhere': '华北油田华苑东区d区',
          'FaProvince': '300000',
          'FaCity': '061000',
          'FaCounty': '062450',
          'FaComeWhere': '华北油田华苑东区d区',
          'radio_1': '2e856fa0-5b66-4ba5-97a9-177b4b77e2b3',
          'radio_2': 'ee6648b4-3da8-41ae-b769-04a8d29519e1',
          'radio_3': 'd4b03707-0619-4dfb-82c3-c1f2af3bfb53',
          'radio_4': '2ff4ae72-0d80-4428-a919-68e04e9891b9',
          'radio_5': '24d314e6-d37d-448d-897e-1910b30f8da1',
          'radio_6': '6ea8bb17-c725-4ed2-853f-29627f94b4bc',
          'radio_7':'a41b9a56-788a-493b-8d20-df94f8983af0',
          'radio_8': '04570d7e-0b63-44d4-b8a2-edce144ee5bd',
          'radio_9': '5712563d-eb34-4fd1-a9fe-1b68f57e7e38',
          'radio_10': 'dd238366-45d4-42e9-abab-40f957c4991e',
          'radio_11': '46b00678-b1b5-47e0-b404-00ed9f1a5291',
          'Other': '',
          'GetAreaUrl': '/SPCP/Web/Report/GetArea',
          'Sex': '女',
          'IdCard': '13098219951104822x',
          'SpeType': 'S',
          'CollegeNo': '000001',
          'SpeGrade': '2018',
          'SpecialtyName': '油气田开发工程',
          'ClassName': '油气田开发工程专业硕2018级04班',
          'ProvinceName': '河北省',
          'CityName': '沧州市',
          'CountyName': '河间市',
          'FaProvinceName': '河北省',
          'FaCityName': '沧州市',
          'FaCountyName': '河间市',
          'radioCount': '11',
          'checkboxCount': '0',
          'blackCount': '0',
          'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至非湖北地区","SelectId":"ee6648b4-3da8-41ae-b769-04a8d29519e1","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"无","SelectId":"2ff4ae72-0d80-4428-a919-68e04e9891b9","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"否","SelectId":"a41b9a56-788a-493b-8d20-df94f8983af0","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
          }
        headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Report/Index'
        response = s.post(url=index_url,data=data,headers=headers)
        # 若返回数据里有 已登记 字眼，代表已登记
        if "提交成功！" in response.text:
            print("3. 提交成功！")
        else:
            print("3. 提交失败！")
            print((response.text).encode('utf-8'))
            sys.exit(1)

def main():
    login(login_url)
    getIndex(index_url)


if __name__ == "__main__":
    main()
