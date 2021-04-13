import requests
import unittest
import json
from config import *


class Test_login(unittest.TestCase):
    def login(self,username,psw,dev,yzm):
        url = "https://passport.test.goago.cn/crm/login.do"
        zhanghao = {"userName":username,"password":psw,"device":dev,"authCode":yzm}
        response = requests.post(url,data= zhanghao)
        print(response.content)
        return response
    def test_login1(self):
        username = "529test"
        psw = '12345678t'
        dev = "800A80605365"
        yzm = "1234"
        response = self.login(username,psw,dev,yzm)
        x= response.text
        dict = json.loads(x)
        logging.info(dict)
        logging.info(dict['body']['shopName'])
        # self.assertEqual(12,dict['errorCode'])





if __name__ == "__main__":
    unittest.main()
