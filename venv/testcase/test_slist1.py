import requests
import unittest
import json
from rest_client import *

class SZXP_liebiao(unittest.TestCase):
   def test_liebiao(self):
      token = "misUser1F2QTBG3KNVU050AB2M1081IHE001IS5"
      page = 1
      size = 100
      url = "http://crm.be.test.goago.cn/statistics/shopBillInfoList.do"
      zhanghao = {"token": token,"pageIndex":page,"pageSize":size}
      result = httlUtils ('POST', url, zhanghao)
      a = result["data"]['rows']
      b=a[1]['billFileName']
      print(b)
   #    response = requests.post(url,data = zhanghao)
   #    # print (response.content.decode("utf-8"))
   #    return response
   # def test_liebiao(self):
   #    token = "misUser1F2QTBG3KNVU050AB2M1081IHE001IS5"
   #    page = 1
   #    size = 100
   #    x = self.liebiao(token,page,size)
   #    j=x.text
   #    dict = json.loads (j)
   #    a=dict["data"]['rows']
   #    b=a[1]['billFileName']
   #    print(b)
   #    # name=check_user(b)
   #    # print(name)
   #


if __name__ == "__main__":
    unittest.main()



