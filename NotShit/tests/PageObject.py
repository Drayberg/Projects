from selenium import webdriver
from dotenv import load_dotenv
from os import getenv

load_dotenv()
LOGIN = getenv('LOGIN')
PASSWORD = getenv('PASSWORD')
BASE_URL = getenv('SERVICE_URL')


class Selenium:
    def __init__(self):
        browser = 'chrome'
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument ('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(BASE_URL)


