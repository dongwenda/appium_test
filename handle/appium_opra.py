from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AppiumOperation:

    def find_element(self,driver, location):
        location_info = location.split(';')
        if location_info[0] == 'xpath':
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location_info[1])))
            return element

    def operation(self, element, opra):
        if opra == 'click':
            self.click(element)

    def click(self, element):
        element.click()

