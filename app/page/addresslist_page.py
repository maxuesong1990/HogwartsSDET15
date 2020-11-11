"""
通讯录界面
添加成员
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.member_Invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def click_addmember(self):
        #self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)