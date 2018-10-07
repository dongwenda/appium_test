from handle.base_driver import BaseDriver
from handle.appium_opra import AppiumOperation
from page import current_deposit_page, depositlist_page, fund_page, gold_page
from page import login_guide_page, money_management_page, overview_page

class HandleDriver(BaseDriver, AppiumOperation):
    def __init__(self, phone_num):
        self.driver = self.android_driver(phone_num)

    def get_location(self, page=None, element=None):
        if page == 'OverviewPage':
            return overview_page.OverviewPage.elements[element]
        elif page == 'MoneyManagementPage':
            return money_management_page.MoneyManagementPage.elements[element]



    def do(self, page=None, element=None, opra=None):
        location = self.get_location(page, element)
        element_ = self.find_element(self.driver, location)
        self.operation(element_,opra)



