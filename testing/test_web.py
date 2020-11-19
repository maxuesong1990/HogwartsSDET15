from selenium import webdriver

class TestDate:
    def test_data(self):
        driver= webdriver.Chrome()
        driver.get("https://home.testing-studio.com")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
