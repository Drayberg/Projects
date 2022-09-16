from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import TimeoutException
import os


class Wiki:
    def __init__(self, browser: str = 'chrome'):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument ('--headless')
            options.add_argument ('--disable-blink-features=AutomationControlled')
            self.driver = webdriver.Chrome (options=options)
        else:
            raise Exception ("Unknown Webdriver")

        self.driver.get ('https://ru.wikipedia.org')
        self.TIMEOUT = 5
        self.links = []
        self.path = 'C:/Users/Drayberg/Downloads/testsss'

    def close_driver(self):
        print ("Closing driver")
        if self.driver:
            self.driver.close ()

    def search(self, keyword: str):
        inp_field = self.driver.find_element (By.CLASS_NAME, 'vector-search-box-input')
        inp_field.click()
        inp_field.send_keys(keyword)
        try:
            suggestions = Ec.presence_of_all_elements_located ((By.XPATH, "//div[@class='suggestions-results']/a"))
            Wait (self.driver, timeout=self.TIMEOUT).until (suggestions)
            inp_field.send_keys (Keys.ENTER)
        except TimeoutException:
            self.close_driver ()
            raise TimeoutException ("No results")

    def parse(self, save_links: bool = False):
        ps_elements = []

        ps = self.driver.find_elements (By.XPATH, "//div[@class='mw-parser-output']/*")
        for p in ps:
            if p.tag_name == 'p':
                ps_elements.append (p)
            if p.get_attribute ('id') == 'toc':
                break

        if save_links:
            for p in ps_elements:
                links = p.find_elements (By.XPATH, './a')
                for link in links:
                    li = link.get_attribute ('href')
                    if li:
                        self.links.append (li)
        for p in ps_elements:
            self.write_to_file (name=self.driver.title, text=p.text)

        print (self.driver.title, 'saved')

    def write_to_file(self, text: str, name: str):
        if not os.path.exists (self.path):
            os.makedirs (self.path)
        with open (f"{os.path.join (self.path, name)}.txt", "a", encoding='utf-8') as f:
            f.write (text)

    def save_links(self):
        for el in self.links:
            self.driver.get (el)
            self.parse ()


def main():
    word = input ("Чи ищем: ")
    wiki = Wiki ()
    wiki.search (word)
    wiki.parse (save_links=True)
    wiki.save_links ()
    wiki.close_driver ()


if __name__ == '__main__':
    main ()
#ololo
