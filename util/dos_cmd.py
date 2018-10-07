# -*- coding: utf-8 -*-
import os
#print(os.system('adb devices'))
#print(os.popen('adb devices').readlines())
class DosCmd:
    def excute_cmd_result(self, command):
        result = os.popen(command).readlines()
        result_list = [_.strip() for _ in result if _ != '\n']
        return result_list

    def excute_cmd(self, command):
        os.system(command)

if __name__ == '__main__':
    dc = DosCmd()
    print(dc.excute_cmd_result('adb devices'))
    print(dc.excute_cmd_result('netstat -ano | findstr 8080'))