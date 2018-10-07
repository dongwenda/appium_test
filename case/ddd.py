import os
import time
import datetime
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
case_path = os.path.join(cur_path, 'case')
print(case_path)
report_path = os.path.join(cur_path, 'report')
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nowTime)