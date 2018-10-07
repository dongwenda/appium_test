import os
import inspect
from case import ftest_ffff,ftest_appium

def get_case_files():
    cur_path = os.getcwd()
    case_path = os.path.join(cur_path, '..\case')
    case_files = [file.rstrip('.py') for file in os.listdir(case_path) if
                 file.startswith('test') and file.endswith('.py')]
    # print(case_files)
    return case_files

def get_all_testClass():
    case_files = get_case_files()
    print(case_files)
    classNameList = []
    for file in case_files:
        for name, obj in inspect.getmembers(file):
            if inspect.isclass(obj):
                if name.startswith('Test'):
                    classNameList.append(name)
    print(classNameList)


get_all_testClass()