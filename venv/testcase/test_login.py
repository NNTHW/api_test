import requests
import unittest
import json
from rest_client import *


class Test_login(unittest.TestCase):
    def test_login(self):
        username = "529test"
        psw = '12345678t'
        dev = "800A80605365"
        yzm = "1234"
        url = "https://passport.test.goago.cn/crm/login.do"
        data = {"userName":username,"password":psw,"device":dev,"authCode":yzm}
        result = httlUtils ('POST', url, data)
        print (result)
    # def test_login1(self):
    #     username = "529test"
    #     psw = '12345678t'
    #     dev = "800A80605365"
    #     yzm = "1234"

    #     response = self.login(username,psw,dev,yzm)
    #     x= response.text
    #     dict = json.loads(x)
    #     print(dict)
    #     print(dict['body']['shopName'])
    #     # self.assertEqual(12,dict['errorCode'])





if __name__ == "__main__":
    unittest.main()
