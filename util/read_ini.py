# -*- coding: utf-8 -*-
import configparser


class ReadIni():
    '''
    读取配置文件.ini
    '''

    def __init__(self, filePath=None):
        if filePath == None:
            self.filePath = './../config/LocalElement.ini'
        else:
            self.filePath = filePath

        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.filePath)
        return read_ini

    def get_value(self,section, option):
        try:
            return self.data.get(section=section, option=option)
        except:
            return None


if __name__ == '__main__':
    ri = ReadIni()
    print(ri.get_value('login_element', 'nameIsssnput'))
