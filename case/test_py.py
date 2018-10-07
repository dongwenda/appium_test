import pytest
from handle.handle_driver import HandleDriver

class TestPy:
    def setup_class(self):
        print("setup_class")
        userNum = pytest.config.getoption("--userNum")
        self.handle = HandleDriver(userNum)

    def teardown_class(self):
        print("teardown_class")

    def test_py(self):
        userNum = pytest.config.getoption("--userNum")
        print(userNum)
        a = 1/0

    def test_app(self):
        self.handle.do('OverviewPage', 'dqjdqj', 'click')
        self.handle.do('MoneyManagementPage', 'fh', 'click')

if __name__ == '__main__':
    pytest.main(["-s","test_py.py","--cmdopt=tttt"])


