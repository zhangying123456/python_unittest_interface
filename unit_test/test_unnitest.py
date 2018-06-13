#coding:utf-8
import unittest
from util.test_get_post import Runmain

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("类执行之前的方法")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("类执行之后的方法")
        pass

    #每次方法前执行
    def setUp(self):
        self.run = Runmain()

    #每次方法后执行
    def tearDown(self):
        pass

    def test_01(self):
        url = 'xxx'
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        res = self.run.run_main(url,None,None,headers,'POST')
        print(res)
        self.assertEqual(res['code'], '200', '返回状态错误，不为200')
        self.assertEqual(res.get("code"), '200', '返回状态错误，不为200')
        self.assertEqual(res['value']['name'],'so')
        print("这是第一个测试方法")

    @unittest.skip("无条件跳过此用例")
    def test_02(self):
        url = 'xxx'
        params = {"bizName":"globalSearchClient","sign":"8c8bc3ee9d6c4b7b8a390ae298cb6db5","timeMills":"1524906299999"}
        res = self.run.run_main(url,params,None,None,'GET')
        print(res)
        self.assertEqual(res['code'], '200', '返回状态错误，不为200')
        print("这是第二个测试方法")



