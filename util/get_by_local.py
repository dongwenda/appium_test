# -*- coding: utf-8 -*-
from .read_ini import ReadIni

class GetByLocal:
    '''
    根据配置文件信息，返回定位方法
    '''

    def __init__(self, driver):
        self.driver = driver

    def get_element(self,section, option):
        ri = ReadIni
        local = ri.get_value(section, option)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None