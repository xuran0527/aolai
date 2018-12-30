import time
import allure
from selenium.webdriver.common.by import By

class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc):
        time.sleep(1)
        return self.driver.find_element(loc[0],loc[1])
    def click_element(self,loc):
        self.find_element(loc).click()
    def send_element_content(self, loc, content):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)
    def swipe_screen(self, tag):
        time.sleep(1)
        #获取当前手机窗口的大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width") #获取手机宽
        height = screen_size.get("height")#获取手机的高
        if tag == 1:  # 向上滚动 两点之间滑动  x轴不变
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    @allure.step('获取吐司')
    def get_toast_message(self, message):
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_message = self.find_element((By.XPATH, toast_xpath)).text
        return toast_message

    #.截图
    def get_screen(self):
        #截图名称
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)
        with open(png_name,"rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)