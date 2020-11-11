"""
邀请页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.contactadd_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def add_member_menual(self):
        #self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return  ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result