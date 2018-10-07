# -*- coding: utf-8 -*-

from case.parametrized_testcase import ParametrizedTestCase

class TestAppium(ParametrizedTestCase):
    def setUp(self):
        print("test-->setup")

    def tearDown(self):
        print("test-->teardown")

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

