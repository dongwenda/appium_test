# -*- coding: utf-8 -*-
from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.user_command import WriteUserCommand

class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.appium_port_list = self.create_port_list(4700)
        self.bootstrap_port_list = self.create_port_list(4900)
        self.command_list = self.create_command_list()
        self.wuc = WriteUserCommand()

    def get_devices(self):
        '''
        获取设备信息
        :return:
        '''
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list)>=2:
            devices_list = [i.split('\t')[0] for i in result_list if (not i.startswith('List') and i.split('\t')[1] == 'device')]
            return devices_list
        else:
            return None

    def create_port_list(self,start_port):
        '''
        创建可用端口
        :param start_port:
        :return: port_list
        '''
        port = Port()
        port_list = port.create_port_list(start_port,self.device_list)
        return port_list

    def create_command_list(self):
        #appium -p 4700 -bp 4800 -U 127.0.0.1:21503 --no-reset --session-override --log C:/log.log

        print(self.appium_port_list,self.bootstrap_port_list,self.device_list)

        command_list = ['appium -p {0} -bp {1} -U {2} --no-reset --session-override --log ./log/Phone{3}.log'.format(
            self.appium_port_list[i],self.bootstrap_port_list[i],self.device_list[i], i) \
                        for i in range(len(self.device_list))]
        return command_list

    def start_server(self,i):
        '''
        启动appium服务
        :param i: command_list[i]
        :return:
        '''
        self.dos.excute_cmd(self.command_list[i])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def write_user_command(self):
        i = 0
        for port,bp,deviceName in zip(self.appium_port_list,self.bootstrap_port_list,self.device_list):
            self.wuc.write_data(i,port,bp,deviceName)
            i+=1

    def main(self):
        self.kill_server()
        self.wuc.clear_data()
        self.write_user_command()
        for i in range(len(self.command_list)):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()

if __name__ == '__main__':
    server = Server()
    print(server.get_devices())
    print(server.create_command_list())
    server.main()