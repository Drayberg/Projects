from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ex
from selenium.webdriver.common.action_chains import ActionChains
from Tools.Projects.Shit.storage import path
from time import sleep


class SouthPark:
    def __init__(self, browser: str = 'chrome'):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument ('--headless')
            # options.add_argument(f"user-data-dir={path}")
            options.add_argument('--disable-blink-features=AutomationControlled')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise Exception("Unknown Browser")
        self.driver.get('https://sp.freehat.cc/episode/rand.php')

    def hover(self):
        southpark = self.driver.find_element(by=By.XPATH, value='//*[@id="header"]/div/div/ul/li[1]/a')
        ActionChains(self.driver).move_to_element(to_element=southpark).perform()

    def fullscreen(self):
        video = self.driver.find_element(By.TAG_NAME, 'video')
        ActionChains(self.driver).move_to_element(to_element=video).key_down(Keys.SHIFT).send_keys('f').perform()
        ActionChains(self.driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()


sp = SouthPark()
sp.hover()
sp.fullscreen()
