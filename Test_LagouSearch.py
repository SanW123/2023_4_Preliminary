import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLagousearch:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.parametrize("post", ["软件测试", "测试开发"], ids=['Software_testing', 'Test_development'])
    @pytest.mark.parametrize("place", ["北京", "上海", "深圳", "广州"],
                             ids=['BeiJing', 'ShangHai', 'ShenZhen', 'GuangZhou'])
    def test_lagou_search(self, place, post):
        "  post : {post} , place : {place} "
        self.driver.get("https://www.lagou.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'cboxClose').click()
        self.driver.find_element(By.ID, "search_input").click()
        self.driver.find_element(By.ID, "zhaopin").click()
        # 工作地点选择
        if place == '北京':
            job_num = '2'
        elif place == '上海':
            job_num = '3'
        elif place == '深圳':
            job_num = '4'
        elif place == '广州':
            job_num = '5'
        job_place = '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div[' + job_num + ']'
        self.driver.find_element(By.XPATH, job_place).click()
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/div/span')
            )
        )
        self.driver.find_element(By.XPATH,
                                 '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/div/span').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/div/div/ul[2]/li[1]/span')
            )
        )
        self.driver.find_element(By.XPATH,
                                 '//*[@id="jobsContainer"]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/div/div/ul[2]/li[1]/span').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="order"]/div/div[3]')
            )
        )
        self.driver.find_element(By.XPATH, '//*[@id="order"]/div/div[3]').click()

        self.driver.find_element(By.ID, "keyword").send_keys(post)
        self.driver.find_element(By.CLASS_NAME, 'search-btn__1ilgU').click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, 'openWinPostion')
            )
        )
        check_text = self.driver.find_element(By.ID, 'openWinPostion').text
        time.sleep(2)
        assert post in check_text
        time.sleep(3)
