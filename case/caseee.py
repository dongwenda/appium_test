import unittest
from handle.handle_driver import HandleDriver
import warnings

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后的方法")

    def setUp(self):
        print("test-->setup")
        warnings.simplefilter("ignore", ResourceWarning)
        self.handle = HandleDriver()

    def tearDown(self):
        print("test-->teardown")

    def test_01(self):
        print("第一个测试方法")
        #self.assertEqual(1,2,'搓搓错')
        self.handle.do('OverviewPage','dqjdqj','click')
        self.handle.do('MoneyManagementPage', 'fh', 'click')

if __name__ == '__main__':
    print(type(TestMethod))
    if isinstance(TestMethod, unittest.TestCase):
        print("yyy")