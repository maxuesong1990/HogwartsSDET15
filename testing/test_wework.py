from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWework():
    def setup(self):
        desire_cap={
          "platformName": "Android",
          "deviceName": "emulator-5554",
          "appPackage": "com.tencent.wework",
          "appActivity": "launch.WwMainActivity",
          "noReset": "True"
        }
        self.driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        #增加隐士等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_wework(self):
        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("打开").'
        #                                                 'instance(0));').click
        self.driver.find_element_by_xpath('//*[@text="打卡"]').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text, "次外出")]').click()
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)



