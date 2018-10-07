# -*- coding: utf-8 -*-
import sys
sys.path.append("C:\lappuim")
import unittest
from util import HTMLTestRunner

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后的方法")

    def setUp(self):
        print("test-->setup")

    def tearDown(self):
        print("test-->teardown")

    def test_01(self):
        print("第一个测试方法")
        self.assertEqual(1,2,'搓搓错')

    def test_02(self):
        print("第二个测试方法")
        self.assertEqual(1,1,'oook~')

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    #unittest.TextTestRunner().run(suite)
    htmlFile = 'C:/lappuim/report/report.html'
    with open(htmlFile, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='自动化测试报告,测试结果如下：',
                                               description='用例执行情况：')
        runner.run(suite)