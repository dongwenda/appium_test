# content of conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--userNum", action="store", default="0", help="my option: 0 or 1"
    )

@pytest.fixture
def userNum(request):
    return request.config.getoption("--userNum")