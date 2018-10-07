# -*- coding: utf-8 -*-
import unittest
import time
from util.server import Server
from util.HTMLTestRunner import HTMLTestRunner
import os
import multiprocessing
from util.user_command import ReadUserCommand
from util.dos_cmd import DosCmd
import datetime


# 当前脚本所在文件真实路径 C:\lappuim
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=fp,
                           title='自动化测试报告,测试结果如下：',
                           description='用例执行情况：')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_count():
    read_user_command = ReadUserCommand()
    count = read_user_command.get_user_num()
    return count
# case_path = os.path.join(cur_path, 'case')
# pytest case_path --userNum=0
cmd = DosCmd()
def run_all_case(user_num):
    case_path = os.path.join(cur_path, 'case')
    report_path = os.path.join(cur_path, 'report')
    print(report_path)
    nowTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    print(nowTime)
    #command = 'pytest {} --userNum={} --html={}\\{}.html --self-contained-html'.format(case_path, user_num, report_path, nowTime)
    command = 'pytest {case_path} --userNum={user_num} --html=./report/Phone{user_num}_{nowTime}.html --self-contained-html'.format(
        case_path=case_path, user_num=user_num, nowTime=nowTime)
    print(command)
    cmd.excute_cmd(command)

if __name__ == '__main__':
    server = Server()
    server.main()

    process = []
    for user_num in range(get_count()):
        print(user_num)
        p = multiprocessing.Process(target=run_all_case, args=(user_num,))
        process.append(p)
    for p in process:
        p.start()

    for p in process:
        p.join()

    server.kill_server()


