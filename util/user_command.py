# -*- coding: utf-8 -*-
import yaml
import os
# 当前脚本所在文件真实路径 C:\lappuim
cur_path = os.path.dirname(os.path.realpath(__file__))
user_ = os.path.join(cur_path, '..\config\\userconfig.yaml')

class ReadUserCommand:

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        '''
        加载yaml数据
        :return: data
        '''
        with open(user_) as fr:
            data = yaml.load(fr)
        return data

    def get_value(self,user,key):
        '''
        获取value
        :param user:
        :param key:
        :return:
        '''
        value = self.data[user][key]
        return value

    def get_user_num(self):
        return len(self.data)

class WriteUserCommand:

    def write_data(self,i,port,bp,deviceName):
        '''
        写入数据
        :param i:
        :param device:
        :param port:
        :param bp:
        :return:
        '''
        data = self.join_data(i,port,bp,deviceName)
        with open(user_,"a") as fr:
            yaml.dump(data,fr)

    def join_data(self,i,port,bp,deviceName):
        data = {
            "user_info_"+str(i): {
                "port": str(port),
                "bp": str(bp),
                "deviceName": str(deviceName)
            }
        }
        return data

    def clear_data(self):
        with open(user_,"w") as fr:
            fr.truncate()
        fr.close()


if __name__ == '__main__':
    usercommand = ReadUserCommand()
    print(usercommand.get_value('user_info_2','bp'))