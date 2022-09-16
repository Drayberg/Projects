from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from Tools.Projects.Shit.storage import vk_login_7660, vk_password_7660
from selenium.webdriver.common.keys import Keys


class Vk:
    def __init__(self, browser: str = 'chrome'):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument ('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise Exception("Unknown Browser")
        self.driver.get('https://www.vk.com')
        self.driver.find_element(By.XPATH, '//*/form/button[1]/span').click()
        self.__login = vk_login_7660
        self.__password = vk_password_7660

    def login_input(self):
        inp_w = Ec.presence_of_element_located((By.XPATH, '//*/input[@name="login"]'))
        WebDriverWait(self.driver, 10).until(inp_w)
        inp = self.driver.find_element(By.XPATH, '//*/input[@name="login"]')
        try:
            inp.send_keys(self.__login)
            inp.send_keys(Keys.ENTER)
        except Exception:
            print('Wrong Login')

    def password_input(self):
        inp_w = Ec.presence_of_element_located((By.XPATH, '//*/input[@name="password"]'))
        WebDriverWait(self.driver, 10).until(inp_w)
        inp = self.driver.find_element(By.XPATH, '//*/input[@name="password"]')
        try:
            inp.send_keys(self.__password)
            inp.send_keys(Keys.ENTER)
        except Exception:
            print('Wrong Password')


vk = Vk()
vk.login_input()
vk.password_input()
