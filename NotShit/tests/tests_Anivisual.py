from global_enums import GlobalErrors

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Ec
from PageObject import Selenium, webdriver
import pytest
from time import sleep

import os


def test_status(server_code):
    try:
        assert server_code == 200, GlobalErrors.WRONG_STATUS_CODE
    except TimeoutError:
        'Timeout Exception'
    finally:
        if server_code not in range(200, 209):
            return webdriver.Chrome.close()


class TestAnivisual(Selenium):
    def test_logo_click(self):

        assert self.driver.find_element(By.XPATH, '//a[contains(text(), "Anivisual.net")]').click() is None, GlobalErrors.NO_SUCH_ELEMENT

    #     self.driver.switch_to.frame('list')
    #     self.driver.find_element(By.XPATH, "//a[starts-with(@href, '/b/')]").click()
    #     self.driver.switch_to.parent_frame()
    #     self.driver.switch_to.frame('board')
    #     assert self.driver.find_element(By.CLASS_NAME, "adminbar"), GlobalErrors.NO_SUCH_ELEMENT
    #
    # def test_b_first_thread(self):
    #
    #     self.driver.find_element(By.XPATH, '//*/span[1]/a').click()
    #
    #
    # def test_b_first_thread_reply_button(self):
    #     self.driver.back()
    #     self.driver.switch_to.frame('board')
    #     sleep(5)
    #     self.driver.find_element(By.XPATH, "//*/span[2]/a[1]/img").click()
    #     assert self.driver.find_element(By.ID, "replyform")

    # def test_b_first_thread_reply(self):
    #     if test_b_first_thread_reply_button:

    def test_close_driver(self):
        if self.driver:
            sleep(5)
            self.driver.close()


def main():
    test_status()
    TestAnivisual()


if __name__ == '__main__':
    main()
