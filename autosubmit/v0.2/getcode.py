'''
Copyright (C) 2020 nv4dll
E-mail contact: nv4dll@outlook.com
'''
import time
import requests
import sys
import json
from multiprocessing import Pool
import os
from PIL import Image

code_url = "http://xg.swpu.edu.cn/SPCP/Web/Account/GetLoginVCode?dt=1590809209871"
login_url = "http://xg.swpu.edu.cn/SPCP/Web/"
index_url = "http://xg.swpu.edu.cn/SPCP/Web/Report/Index"
logout_url = "http://xg.swpu.edu.cn/SPCP/Web/Account/Logout"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.34 Safari/537.36',
    'Referer': 'http://xg.swpu.edu.cn/SPCP/Web/'
}

logindatajhw = {
    'ReSubmiteFlag': '0a270cde-be35-471e-94dc-13649a81dc4d',
    'StuLoginMode': '1',
    'txtUid': '201821000713',
    'txtPwd': '19041x',
    'code': 'qhze'
    }

submitdatajhw={
    'StudentId': '201821000713',
    'Name': '贾昊卫',
    'MoveTel': '18591796262',
    'Province': '610000',
    'City':'610100',
    'County':'610117',
    'ComeWhere': '长庆龙凤园九区',
    'FaProvince': '610000',
    'FaCity': '610100',
    'FaCounty': '610117',
    'FaComeWhere': '长庆龙凤园九区',
    'radio_1': '4f47091a-f92f-455a-9a95-19c1dd74b60d',
    'radio_2': '2e856fa0-5b66-4ba5-97a9-177b4b77e2b3',
    'radio_3': 'ee6648b4-3da8-41ae-b769-04a8d29519e1',
    'radio_4': 'd4b03707-0619-4dfb-82c3-c1f2af3bfb53',
    'radio_5': '2ff4ae72-0d80-4428-a919-68e04e9891b9',
    'radio_6': '24d314e6-d37d-448d-897e-1910b30f8da1',
    'radio_7': '6ea8bb17-c725-4ed2-853f-29627f94b4bc',
    'radio_8': 'a41b9a56-788a-493b-8d20-df94f8983af0',
    'radio_9': '04570d7e-0b63-44d4-b8a2-edce144ee5bd',
    'radio_10': '5712563d-eb34-4fd1-a9fe-1b68f57e7e38',
    'radio_11':'dd238366-45d4-42e9-abab-40f957c4991e',
    'radio_12': '46b00678-b1b5-47e0-b404-00ed9f1a5291',
    'radio_13': '0aa7f224-b011-4dda-99d4-392ec010b36e',
    'text_1':'',
    'radio_14':'2dce9072-29b6-44bd-8e99-af1bef745692',
    'text_2': '',
    'radio_15': '382f639a-4966-4afb-b6ee-4011a76b28a4',
    'Other': ' ',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'Sex': '男',
    'IdCard': '62282119960419041X',
    'SpeType': 'S',
    'CollegeNo': '000001',
    'SpeGrade': '2018',
    'SpecialtyName': '油气田开发工程',
    'ClassName': '油气田开发工程专业硕2018级05班',
    'ProvinceName': '陕西省',
    'CityName': '西安市',
    'CountyName': '高陵区',
    'FaProvinceName': '陕西省',
    'FaCityName': '西安市',
    'FaCountyName': '高陵区',
    'radioCount': '11',
    'checkboxCount': '0',
    'blackCount': '0',
    'PZData': ' [{"OptionName":"低风险地区","SelectId":"4f47091a-f92f-455a-9a95-19c1dd74b60d","TitleId":"1cf60e4e-d77a-439a-bb88-dd6b10304b10","OptionType":"0"},{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至非湖北地区","SelectId":"ee6648b4-3da8-41ae-b769-04a8d29519e1","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"无","SelectId":"2ff4ae72-0d80-4428-a919-68e04e9891b9","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"否","SelectId":"a41b9a56-788a-493b-8d20-df94f8983af0","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"},{"OptionName":"无","SelectId":"0aa7f224-b011-4dda-99d4-392ec010b36e","TitleId":"563d4739-5a0e-479e-b0aa-c6527fd5e522","OptionType":"0"},{"OptionName":"无","SelectId":"2dce9072-29b6-44bd-8e99-af1bef745692","TitleId":"22b30d38-3396-40d7-ba49-03beccc7eef4","OptionType":"0"},{"OptionName":"已获得，防疫健康码为绿色","SelectId":"382f639a-4966-4afb-b6ee-4011a76b28a4","TitleId":"046ab087-cc66-4d31-9420-76a8b9a40d6d","OptionType":"0"}]',
    'ReSubmiteFlag': 'dd1d6b87-9e55-4ca4-bf9f-cfb2afb4e395'  
}

def download_image(s):
    # resp = requests.get(url, stream=True)
    # from contextlib import closing
    # with closing(requests.get(url, stream=True)) as resp:
    with s.get(url=code_url, stream=True) as resp:
        with open('tmp.jpg', 'wb') as fd:
            for chunk in resp.iter_content():
                fd.write(chunk)
    # print(resp.text)
    # print(resp.request.headers)
    # print(resp.status_code)

from aip import AipOcr
import re  # 用于正则

config = {
    'appId': '20141005',
    'apiKey': '0UXx2DelVprXxPYug9dIubGA',
    'secretKey': 'Q1Q1yimrpaPfZ7SyDHCwKaqSU6WCL5dP'
}

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    client = AipOcr(**config)
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])

def codeocr(session):
    download_image(session)
    time.sleep(2)
    result = img_to_str('tmp.jpg')
    resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
    result_four = resultj[0:4]  # 只获取前4个字符
    if len(result_four) < 4:
        print("less than 4 character, get a new code!")
        return codeocr(session)
    elif result_four.isalpha()==False:
        print("containing numbers, get a new code!")
        return codeocr(session)
    else:
        print(result_four)
        return result_four

def wirtelog(log):
    print(log+'\n')
    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
    #change in linux
    with open("C:\\Users\\nv4dll\\Desktop\\autosubmit"+".log","a") as f:                                  #写入log文件
        f.write(localtime+" : ")
        f.write(log)  
        f.write("\n")

def login(usr,session,login_url,logindata,headers):
    logindata['code'] = codeocr(session)
    response = session.post(url=login_url,data=logindata,headers=headers)
    if "首页" in response.text:
        wirtelog(usr+"1.登录成功")
    elif "验证码错误" in response.text:
        print("Wrong captcha, get a new code! ")
        logindata['code'] = codeocr(session)
        return login(usr,session,login_url,logindata,headers)
    else:
        print((response.text))

def submit(session,usr,logindata,submitdata):
    
    response = session.get(url=login_url)
    login(usr,session,login_url,logindata,headers)

    headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Account/ChooseSys'
    response = session.get(url=index_url,headers=headers)

    if "当前采集日期已登记！" in response.text:
        wirtelog(usr+"2.已登记！")
        response = session.get(url=logout_url,headers=headers)
    else:
        print("发送登记请求！")
        headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Report/Index'
        response = session.post(url=index_url,data=submitdata,headers=headers)
        # 若返回数据里有 提交成功 字眼，代表提交成功
        if "提交成功！" in response.text:
            headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Account/ChooseSys'
            response = session.get(url=logout_url,headers=headers)
            wirtelog(usr+"2.提交成功！")
        else:
            print((response.text))
            response = session.get(url=logout_url,headers=headers)
   

if __name__ == "__main__":

    wirtelog("============开始提交=============")
    session = requests.Session()
    submit(session,"jhw",logindatajhw,submitdatajhw)
    wirtelog("============提交结束=============")




