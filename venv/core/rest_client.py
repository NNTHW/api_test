import  requests
import json
import unittest

def send_get(url, params):
    try:
        res1 = requests.get(url=url, params=params)
        res2 = json.loads(res1.text)  # loads 将字符串转换为字典格式
        res = json.dumps(res2, sort_keys=True, indent=4, ensure_ascii=False)  # 将字典格式json格式输出
        return res2
    except Exception as e:
        print("get请求错误，错误原因：%s" % e)


def send_post(url, params):
    try:
        res1 = requests.post(url=url, data=params)
        res2 = json.loads(res1.text)
        res = json.dumps(res2, sort_keys=True, indent=4, ensure_ascii=False)  # 将字典json格式输出
        return res2
    except Exception as e:
        print("post请求错误，错误原因：%s" % e)


def httlUtils(method, url=None, data=None):
    """
    功能：判断请求是GET还是POST
    :return: url请求结果
    """
    if method == 'POST':
        result = send_post(url, data)
    elif method == 'GET':
        result = send_get(url, data)
    else:
        print("method值错误！！！")
    return result

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    result = httlUtils('POST', url, payload)
    print(result)

