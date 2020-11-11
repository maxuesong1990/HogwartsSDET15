"""
app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
from appium import webdriver

from app.page.base_page import BasePage
from app.page.main_page import MainPage


class APP(BasePage):
    def start(self):
        #启动app
        if self.driver==None:
            desire_cap = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": "launch.WwMainActivity",
                "noReset": "True",
                "automationName": "UiAutomator2"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            # 增加隐士等待
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self)->MainPage:
        # 进入首页
        return MainPage(self.driver)

