import allure

from base.base_action import BaseAction

import page
"""
负责 首页  分类 购物车  我的  业务
"""
class HomePage(BaseAction):
    #初始化函数 动态把driver传入
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击我的')
    def click_my_button(self):
        self.click_element(page.home_my_button)
