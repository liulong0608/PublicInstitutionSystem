"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
**    @fileName         yb_approved_routine_performance.py
**    @version          v0.1
**    @author           Echo
**    @Warehouse        https://gitee.com/liu-long068/
**    @EditTime         2023/8/17
"""
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from selenium import webdriver


class ApprovedRoutinePerformance:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'http://192.168.2.194/console/login'

    def login(self, username, password):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'captcha').send_keys('ASDF')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button').click()
        self.driver.implicitly_wait(30)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.ant-card:nth-child(4) .home_auto_btn__LBhkK:nth-child(2)').click()

    def approved_regular_performance_level(self):
        # hover_loc = By.XPATH, '/html/body/admin-app/admin-main/div/div/lib-aside/aside/lib-nav/div/ul/li[4]/div'
        # click_loc = By.CSS_SELECTOR, '.cdk-overlay-pane > div > ul > li.ng-star-inserted.menu-item-selected.menu-item-hover > div'
        # self.hover_and_click(hover_loc, click_loc)
        # self.driver.find_element(By.LINK_TEXT, '核定常规绩效水平').click()
        # self.driver.implicitly_wait(30)
        self.driver.implicitly_wait(30)
        self.driver.get('http://192.168.2.194/yb_admin/performance/approved-basic-performance-levels')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/admin-app/admin-main/div/div/div/div/admin-approved-basic'
                                           '-performance-levels/div/nz-tabset/div/div/div['
                                           '1]/admin-levels/nz-space/nz-space-item['
                                           '2]/nz-table/nz-spin/div/div/nz-table-title-footer['
                                           '1]/nz-space/nz-space-item[1]/button').click()
        time.sleep(5)
        time_input = 'nz-form-control:nth-child(1) lib-date-input input'
        self.clear_type(time_input, '2023')
        self.driver.find_element(By.CSS_SELECTOR, '.ant-modal-footer > .ant-btn-primary > .ng-star-inserted').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'lib-transfer > div > div.transfer__action.ant-col > button:nth-child(8)').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.standalone-button-group > .ant-btn-primary > .ng-star-inserted').click()
        # 获取所有input输入框

    def hover_and_click(self, hover_loc, click_loc):
        self.driver.implicitly_wait(30)
        el = self.driver.find_element(By.XPATH, hover_loc)
        ActionChains(self.driver).move_to_element(el).perform()
        el = self.driver.find_element(By.XPATH, click_loc)
        el.click()

    def clear_type(self, loc, value):
        """
        输入框清除并且输入值
        :param loc:
        :param value:
        :return:
        """
        el = self.driver.find_element(By.CSS_SELECTOR, loc)
        self.driver.implicitly_wait(10)
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(value)
        el.send_keys(Keys.TAB)

    def run(self):
        self.login('3men0011', 'Aa123456')
        self.approved_regular_performance_level()
        self.quit()

    def quit(self):
        time.sleep(30)
        self.driver.quit()


if __name__ == '__main__':
    arp = ApprovedRoutinePerformance()
    arp.run()
