# -*- coding: utf-8 -*-
from util.dos_cmd import DosCmd

class Port:
    def port_is_used(self,port_num):
        '''
        判断端口是否被占用
        :param port_num int
        :return: True被占用、False没有被占用
        '''

        self.dos = DosCmd()
        command = 'netstat -ano | findstr ' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result)>0:
            return True
        else:
            return False

    def create_port_list(self, start_port, device_list):
        '''
        生成可用端口
        :param start_port:int
        :param device_list: list
        :return: port_list
        '''

        if device_list != None:
            port_list = []
            port = start_port
            while len(port_list) != len(device_list):
                if self.port_is_used(port) != True:
                    port_list.append(port)
                port += 1
            return port_list
        else:
            print('==端口生成失败==')
            return None


if __name__ == '__main__':
    p = Port()
    print(p.port_is_used(8080))

    l = [1,2,3,4]
    print(p.create_port_list(4722,l))