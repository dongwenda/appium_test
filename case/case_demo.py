# -*- coding: utf-8 -*-
import unittest
import threading
from util.server import Server
from business.login_business import LoginBusiness

class ParamTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super().__init__(methodName)
        global p
        p = param

class CaseTest(ParamTestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass-->p is',p)

    def setUp(self):
        print('setUp-->p is',p)

    def tearDown(self):
        print('tearDown-->p is',p)

    def test_01(self):
        print('test_01-->p is',p)

    def test_02(self):
        print('test_02-->p is',p)

def get_suite(i):
    print('get_suite ',i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01', param=i))
    suite.addTest(CaseTest('test_02', param=i))
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    threads = []
    for i in range(2):
        print(i)
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()