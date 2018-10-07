# -*- coding: utf-8 -*-

from case.parametrized_testcase import ParametrizedTestCase
import unittest
from case import ftest_appium

class Testffff(ParametrizedTestCase):
    def setUp(self):
        print("test-->setup")
        print(self.param)

    def tearDown(self):
        print("test-->teardown")

    def test_c(self):
        print('test_c')
        print(self.param)

    def test_d(self):
        print('test_d')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(Testffff, param=42))
    #unittest.TextTestRunner(verbosity=2).run(suite)

