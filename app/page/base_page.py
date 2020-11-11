"""
base_page.py 基类模块，主要用来初始化driver，定位find，常用的最基本的方法

"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver= driver


    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def find_by_scroll(self,text):
        #滑动
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                        f'new UiScrollable(new UiSelector()\
                                                        .scrollable(true).instance(0))\
                                                        .scrollIntoView(new UiSelector()\
                                                        .text("{text}").instance(0));')


    def get_toast_text(self):
        return self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text