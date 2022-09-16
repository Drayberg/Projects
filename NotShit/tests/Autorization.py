from PageObject import LOGIN, PASSWORD, Selenium
from selenium.webdriver.common.by import By
from time import sleep


class Auth(Selenium):

    def authorization(self, login=LOGIN, password=PASSWORD):
        self.driver.find_element(By.XPATH, '//a[@href="/index/1"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="user"]').send_keys(login)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//input[@value="Вход"]').click()


def main():
    auth = Auth()
    auth.authorization()


if __name__ == '__main__':
    main()