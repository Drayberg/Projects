from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions ()
# options.add_argument(f"--user-agent")
# options.add_argument("user-data-dir=C:\\profile")
# options.add_argument ("--proxy-server=173.165.102.210:8080")
options.add_argument ('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome (options=options)
actions = ActionChains (driver)

try:
    driver.get ('http://2ch.hk/b/')
    # driver.get("https://2ip.ru/")
    # driver.get("https://whoer.net/ru")
    driver.implicitly_wait (10)
    driver.refresh ()
    driver.find_element (By.ID, 'plashque-close').click ()
    # search = driver.find_element(By.CLASS_NAME, "desktop")
    catalog = driver.find_element (By.XPATH, "//a[contains(@href,'b/catalog.html')]")
    # print(catalog)
    catalog.click ()
    # driver.get()

    driver.switch_to.window (driver.window_handles[1])

    search = driver.find_element (By.XPATH, '//*[@id="js-csearch"]')
    search.click ()
    search.clear ()
    search.click ()
    sleep (2)
    list_tags = ['AFG', 'FAP', 'ФАП', 'АФЗ', 'афз', 'фап', 'fap', 'afg']
    # search.send_keys ('afg')

    # def fapp():

    # for fap in find_fap:
    #     fap = find_fap.send_keys('')
except Exception as ex:
    print (ex)
finally:
    sleep (10)
    # driver.quit ()
