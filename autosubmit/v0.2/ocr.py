from aip import AipOcr
import re  # 用于正则

config = {
    'appId': '20141005',
    'apiKey': '0UXx2DelVprXxPYug9dIubGA',
    'secretKey': 'Q1Q1yimrpaPfZ7SyDHCwKaqSU6WCL5dP'
}

client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])

result = img_to_str("GetLoginVCode (1).jpg")
print(result)
resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
result_four = resultj[0:4]  # 只获取前4个字符
print(result_four)