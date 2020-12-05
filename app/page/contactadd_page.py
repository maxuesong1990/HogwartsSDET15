"""

"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def add_contact(self,send_name, send_mobile,send_gender):
        # self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(send_name)
        # self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//*[@text='男']").click()
        # if send_gender == '男':
        #     self.driver.find_element_by_xpath("//*[@text='男']").click()
        # else:
        #     self.driver.find_element_by_xpath("//*[@text='女']").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/../android.widget.EditText").send_keys(send_mobile)
        # self.driver.find_element_by_xpath("//*[@text='保存']").click()
        self.find(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(send_name)
        self.find(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if send_gender == '男':
            self.find(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH,"//*[@text='女']").click()
        self.find(MobileBy.XPATH,"//*[contains(@text,'手机')]/../android.widget.EditText").send_keys(send_mobile)
        self.find(MobileBy.XPATH,"//*[@text='保存']").click()

