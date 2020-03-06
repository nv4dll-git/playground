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
logout_url = "http://xg.swpu.edu.cn/SPCP/Web/Account/Logout"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.34 Safari/537.36',
    'Referer': 'http://xg.swpu.edu.cn/SPCP/Web/'
}

s1 = requests.Session()
s2 = requests.Session()
s3 = requests.Session()
s4 = requests.Session()
s5 = requests.Session()
s6 = requests.Session()

data1jhw = {
    'StuLoginMode': '1',
    'txtUid': '201821000713',
    'txtPwd': '19041x'
    #'codeInput': '9fmx'
    }

data2jhw={
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
    'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至非湖北地区","SelectId":"ee6648b4-3da8-41ae-b769-04a8d29519e1","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"无","SelectId":"2ff4ae72-0d80-4428-a919-68e04e9891b9","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"否","SelectId":"a41b9a56-788a-493b-8d20-df94f8983af0","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
  }

data1mmy = {
    'StuLoginMode': '1',
    'txtUid': '201821000685',
    'txtPwd': '04822x'
    #'codeInput': '9fmx'
    }
#todo 改区域编码
data2mmy={
    'StudentId': '201821000685',
    'Name': '马珉玥',
    'MoveTel': '13281870079',
    'Province': '130000',
    'City':'130900',
    'County':'130984',
    'ComeWhere': '华北油田华苑东区d区',
    'FaProvince': '130000',
    'FaCity': '130900',
    'FaCounty': '130984',
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
    'IdCard': '13098219951104822X',
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

data1mkf = {
  'StuLoginMode': '1',
  'txtUid': '201821000632',
  'txtPwd': '101631'
  #'codeInput': '9fmx'
}
#todo 改区域编码
data2mkf={
    'StudentId': '201821000632',
    'Name': '穆轲帆',
    'MoveTel': '18117833981',
    'Province': '510000',
    'City':'511500',
    'County':'511504',
    'ComeWhere': '中央培根小镇18楼1号',
    'FaProvince': '510000',
    'FaCity': '511500',
    'FaCounty': '511504',
    'FaComeWhere': '中央培根小镇18楼1号',
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
    'Other': ' ',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'Sex': '男',
    'IdCard': '511502199503101631',
    'SpeType': 'S',
    'CollegeNo': '000001',
    'SpeGrade': '2018',
    'SpecialtyName': '油气田开发工程',
    'ClassName': '油气田开发工程专业硕2018级03班',
    'ProvinceName': '四川省',
    'CityName': '宜宾市',
    'CountyName': '叙州区',
    'FaProvinceName': '四川省',
    'FaCityName': '宜宾市',
    'FaCountyName': '叙州区',
    'radioCount': '11',
    'checkboxCount': '0',
    'blackCount': '0',
    'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至非湖北地区","SelectId":"ee6648b4-3da8-41ae-b769-04a8d29519e1","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"无","SelectId":"2ff4ae72-0d80-4428-a919-68e04e9891b9","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"否","SelectId":"a41b9a56-788a-493b-8d20-df94f8983af0","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
}

data1qn = {
    'StuLoginMode': '1',
    'txtUid': '201821000715',
    'txtPwd': '03003x'
    #'codeInput': '9fmx'
}

data2qn={
    'StudentId': '201821000715',
    'Name': '秦楠',
    'MoveTel': '17764989562',
    'Province': '620000',
    'City':'621000',
    'County':'621002',
    'ComeWhere': '科教新村',
    'FaProvince': '620000',
    'FaCity': '621000',
    'FaCounty': '621002',
    'FaComeWhere': '科教新村',
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
    'Other': ' ',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'Sex': '男',
    'IdCard': '62282719960103003X',
    'SpeType': 'S',
    'CollegeNo': '000001',
    'SpeGrade': '2018',
    'SpecialtyName': '油气田开发工程',
    'ClassName': '油气田开发工程专业硕2018级05班',
    'ProvinceName': '甘肃省',
    'CityName': '庆阳市',
    'CountyName': '西峰区',
    'FaProvinceName': '甘肃省',
    'FaCityName': '庆阳市',
    'FaCountyName': '西峰区',
    'radioCount': '11',
    'checkboxCount': '0',
    'blackCount': '0',
    'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至湖北其他地区(除武汉)","SelectId":"33775f86-44af-4d84-acbe-ddc5f884a48b","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"有","SelectId":"6545bf6d-6b84-4efc-950c-8e79a3eb5b90","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"是","SelectId":"795abbb5-aed9-4fc6-8c0c-7519bf4b632f","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
}

data1fj = {
    'StuLoginMode': '1',
    'txtUid': '201821000734',
    'txtPwd': '290031'
    #'codeInput': '9fmx'
}

data2fj={
    'StudentId': '201821000734',
    'Name': '付健',
    'MoveTel': '18672111825',
    'Province': '420000',
    'City':'421000',
    'County':'421087',
    'ComeWhere': '二环路自来水公司家属区2栋202',
    'FaProvince': '420000',
    'FaCity': '421000',
    'FaCounty': '421087',
    'FaComeWhere': '二环路自来水公司家属区2栋202',
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
    'Other': ' ',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'Sex': '男',
    'IdCard': '421087199608290031',
    'SpeType': 'S',
    'CollegeNo': '000001',
    'SpeGrade': '2018',
    'SpecialtyName': '油气田开发工程',
    'ClassName': '油气田开发工程专业硕2018级05班',
    'ProvinceName': '湖北省',
    'CityName': '荆州市',
    'CountyName': '松滋市',
    'FaProvinceName': '湖北省',
    'FaCityName': '荆州市',
    'FaCountyName': '松滋市',
    'radioCount': '11',
    'checkboxCount': '0',
    'blackCount': '0',
    'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至湖北其他地区(除武汉)","SelectId":"33775f86-44af-4d84-acbe-ddc5f884a48b","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"有","SelectId":"6545bf6d-6b84-4efc-950c-8e79a3eb5b90","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"是","SelectId":"795abbb5-aed9-4fc6-8c0c-7519bf4b632f","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
}

data1wc = {
    'StuLoginMode': '1',
    'txtUid': '201821000743',
    'txtPwd': '154555'
    #'codeInput': '9fmx'
}

data2wc={
    'StudentId': '201821000743',
    'Name': '文超',
    'MoveTel': '18328070592',
    'Province': '510000',
    'City':'510100',
    'County':'510185',
    'ComeWhere': '禾丰镇香乐村6组',
    'FaProvince': '510000',
    'FaCity': '510100',
    'FaCounty': '510185',
    'FaComeWhere': '禾丰镇香乐村6组',
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
    'Other': ' ',
    'GetAreaUrl': '/SPCP/Web/Report/GetArea',
    'Sex': '男',
    'IdCard': '513902199703154555',
    'SpeType': 'S',
    'CollegeNo': '000001',
    'SpeGrade': '2018',
    'SpecialtyName': '油气田开发工程',
    'ClassName': '油气田开发工程专业硕2018级05班',
    'ProvinceName': '四川省',
    'CityName': '成都市',
    'CountyName': '简阳市',
    'FaProvinceName': '四川省',
    'FaCityName': '成都市',
    'FaCountyName': '简阳市',
    'radioCount': '11',
    'checkboxCount': '0',
    'blackCount': '0',
    'PZData': '[{"OptionName":"假期离校回家，目前尚未返校","SelectId":"2e856fa0-5b66-4ba5-97a9-177b4b77e2b3","TitleId":"6564c529-c9ce-4c9c-8158-fcbf53b7ef9a","OptionType":"0"},{"OptionName":"返乡至非湖北地区","SelectId":"ee6648b4-3da8-41ae-b769-04a8d29519e1","TitleId":"0f9eba15-972e-47ce-aff7-691f0c802b78","OptionType":"0"},{"OptionName":"无","SelectId":"d4b03707-0619-4dfb-82c3-c1f2af3bfb53","TitleId":"35eec330-3122-4054-a4ac-fe8ac95135df","OptionType":"0"},{"OptionName":"无","SelectId":"2ff4ae72-0d80-4428-a919-68e04e9891b9","TitleId":"bd1fef27-db0a-4898-8963-8b8e34714dfc","OptionType":"0"},{"OptionName":"无","SelectId":"24d314e6-d37d-448d-897e-1910b30f8da1","TitleId":"df379fe2-3722-4707-93fd-56d41a7b0940","OptionType":"0"},{"OptionName":"否","SelectId":"6ea8bb17-c725-4ed2-853f-29627f94b4bc","TitleId":"1a3bbc99-c818-46e4-a138-a250f014846b","OptionType":"0"},{"OptionName":"否","SelectId":"a41b9a56-788a-493b-8d20-df94f8983af0","TitleId":"24b30350-ac77-4afa-abda-41d0e88822da","OptionType":"0"},{"OptionName":"否，未接触过","SelectId":"04570d7e-0b63-44d4-b8a2-edce144ee5bd","TitleId":"8bdb0d2b-649c-4798-9d95-9c2b06a0c7c1","OptionType":"0"},{"OptionName":"否","SelectId":"5712563d-eb34-4fd1-a9fe-1b68f57e7e38","TitleId":"be0ed244-91e5-4dbd-a4ab-9c5967145bf3","OptionType":"0"},{"OptionName":"身体状况良好，无异常症状","SelectId":"dd238366-45d4-42e9-abab-40f957c4991e","TitleId":"9e8df714-3e64-4052-9200-766680883e81","OptionType":"0"},{"OptionName":"否","SelectId":"46b00678-b1b5-47e0-b404-00ed9f1a5291","TitleId":"6c4db0fd-bb34-46a1-9f88-4a0315283398","OptionType":"0"}]'
}

def login(log,s,login_url,data,user):

    response = s.post(url=login_url,data=data,headers=headers)
    #print(response)
    #print(response.text)

    # 若返回数据里有 首页 字眼，代表登录成功
    if "首页" in response.text:
        print(user+":1. 登录成功")
        log.append(user+":登录成功")
    else:
        print(user+":1. 登录失败")
        print((response.text).encode('utf-8'))
        log.append(user+":登录失败")

def getIndex(log,s,index_url,logout_url,data,user):
  
    headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Account/ChooseSys'
    response = s.get(url=index_url,headers=headers)

    if "当前采集日期已登记！" in response.text:
        print(user+":2. 已登记！")
        log.append(user+":已登记")
        response = s.get(url=logout_url,headers=headers)
        print(user+":3. 退出登录！")
        log.append(user+":退出登录")
    else:
        print(user+"2. 发送登记请求！")
        
        headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Report/Index'
        response = s.post(url=index_url,data=data,headers=headers)
        # 若返回数据里有 已登记 字眼，代表已登记
        if "提交成功！" in response.text:
            print(user+":3. 提交成功！")
            log.append(user+":提交成功")
            headers['Referer'] = 'http://xg.swpu.edu.cn/SPCP/Web/Account/ChooseSys'
            response = s.get(url=logout_url,headers=headers)
            print(user+":3. 退出登录！")
            log.append(user+":退出登录")
        else:
            print(user+":3. 提交失败！")
            log.append(user+":提交失败")
            print((response.text).encode('utf-8'))
            response = s.get(url=logout_url,headers=headers)
            print(user+":3. 退出登录！")
            log.append(user+":提交失败")

def wirtelog(log):
    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
    #change in linux
    with open("C:\\Users\\Ashley\\Desktop\\"+"autosubmit"+localtime+".log","a") as f:                                  #写入log文件
        for i in range(len(log)):                                                         
            for j in range(len(log[i])): 
                f.write(str(log[i][j]))  
            f.write("\n")

def main():

    log = []
    login(log,s1,login_url,data1jhw,"贾昊卫")
    getIndex(log,s1,index_url,logout_url,data2jhw,"贾昊卫")

    time.sleep(2)

    login(log,s2,login_url,data1mmy,"马珉玥")
    getIndex(log,s2,index_url,logout_url,data2mmy,"马珉玥")

    time.sleep(2)

    login(log,s3,login_url,data1mkf,"穆轲帆")
    getIndex(log,s3,index_url,logout_url,data2mkf,"穆轲帆")

    time.sleep(2)
    
    login(log,s4,login_url,data1qn,"秦楠")
    getIndex(log,s4,index_url,logout_url,data2qn,"秦楠")

    time.sleep(2)
    
    login(log,s5,login_url,data1fj,"付健")
    getIndex(log,s5,index_url,logout_url,data2fj,"付健")
    
    time.sleep(2)

    login(log,s6,login_url,data1wc,"文超")
    getIndex(log,s6,index_url,logout_url,data2wc,"文超")
    wirtelog(log)

if __name__ == "__main__":
    main()