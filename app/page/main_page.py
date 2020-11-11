#跳转主页
from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressListPage
from app.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def goto_message(self):
        """
        进入消息页面
        :return:
        """
        pass

    def goto_adress(self):
        #self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)



