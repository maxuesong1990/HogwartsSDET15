import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact():
    def setup(self):
        desire_cap={
          "platformName": "Android",
          "deviceName": "emulator-5554",
          "appPackage": "com.tencent.wework",
          "appActivity": "launch.WwMainActivity",
          "noReset": "True",
          "automationName": "UiAutomator2"
        }
        self.driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        #增加隐士等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    # def test_wework(self):
    #     self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
    #     # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
    #     #                                                 'scrollable(true).instance(0)).'
    #     #                                                 'scrollIntoView(new UiSelector().text("打开").'
    #     #                                                 'instance(0));').click
    #     self.driver.find_element_by_xpath('//*[@text="打卡"]').click()
    #     self.driver.update_settings({"waitForIdleTimeout": 0})
    #     self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
    #     self.driver.find_element_by_xpath('//*[contains(@text, "次外出")]').click()
    #     WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)


    def test_contact(self):
        """
        1、打开通讯录
        2、打击添加成员
        3、手动输入成员信息，包括：姓名，性别，手机号
        4、点击保存
        5、断言保存成功
        :return:
        """
        send_name='2124333912'
        send_mobile='15556161059'
        send_gender='女'
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(send_name)
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//*[@text='男']").click()
        if send_gender=='男':
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/../android.widget.EditText").send_keys(send_mobile)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        time.sleep(2)
        #使用page_source来处理Toast提示框
        print(self.driver.page_source)
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert  '添加成功'==result