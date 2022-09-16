from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException
import requests
import argparse


class Graber:
    parser = argparse.ArgumentParser(description='Selecting threads')
    parser.add_argument('-f', '--full', action='store_true', help='if True then downloads all threads')
    args = parser.parse_args()

    def __init__(self, browser: str = 'chrome'):
        self.HOSTNAME = "http://2ch.hk"
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument('--disable-blink-features=AutomationControlled')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise Exception("Unknown Webdriver")
        self.driver.get(self.HOSTNAME + '/b/')
        self.TIMEOUT = 30
        self.links = []
        self.video = 'C:/Users/Drayberg/Downloads/testsss/video/'
        self.img = 'C:/Users/Drayberg/Downloads/testsss/img/'
        self.web_el = []

    def quit_driver(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()

    def catolog(self):
        c = Ec.presence_of_all_elements_located((By.CLASS_NAME, 'desktop'))
        WebDriverWait(self.driver, timeout=self.TIMEOUT).until(c)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[1]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def search(self, keyword: str):
        field = Ec.presence_of_element_located((By.XPATH, '//*[@class="ctlg__thread"]'))
        WebDriverWait(self.driver, timeout=self.TIMEOUT).until(field)
        search = self.driver.find_element(By.XPATH, '//*[@id="js-csearch"]')
        search.send_keys(keyword)
        try:
            search.send_keys(Keys.ENTER)
        except TimeoutException:
            raise TimeoutException("No results")

    def selected_threads(self):
        w = Ec.visibility_of_all_elements_located((By.XPATH, "//*[@class='ctlg__thread']"))
        WebDriverWait(self.driver, timeout=self.TIMEOUT).until(w)
        thread_el = self.driver.find_elements(By.XPATH, "//*[contains(@href,'b/res/')]")
        for th in thread_el:
            if th:
                self.web_el.append(th)

        for link in thread_el:
            li = link.get_attribute('href')
            if li:
                self.links.append(li)

    def open(self, full):
        for link in self.links:
            if full:
                if self.driver.get(link):
                    self.driver.switch_to.new_window()
                self.write_to_file()
            else:
                self.driver.get(link)
                self.write_to_file()

    def write_to_file(self):
        elements = self.driver.find_elements(By.XPATH, "//*/figcaption/a[contains(@href, 'b')]")
        for attribute in elements:
            atr = attribute.get_attribute('href')
            name = attribute.get_attribute('text')
            r = requests.get(atr)
            if atr.endswith(".mp4") or atr.endswith(".webm"):
                with open(f'{self.video}{name.split("/")[-1]}', 'wb') as f:
                    f.write(r.content)
            if atr.endswith(".jpg") or atr.endswith(".png") or atr.endswith(".gif"):
                with open(f'{self.img}{name.split("/")[-1]}', 'wb') as f:
                    f.write(r.content)
            print(atr + ' - ' + name)


def main():
    word = input("Тред: ")
    grab = Graber()
    grab.catolog()
    grab.search(word)
    grab.selected_threads()
    grab.open(grab.args.full)
    grab.write_to_file()
    grab.quit_driver()


if __name__ == '__main__':
    main()
