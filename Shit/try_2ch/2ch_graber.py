import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os


options = webdriver.ChromeOptions ()
# options.add_argument ('--headless')
options.add_argument ('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome (options=options)
actions = ActionChains (driver)

try:
    driver.get ('http://2ch.hk/b/')
    driver.implicitly_wait (10)
    driver.refresh ()
    driver.find_element (By.ID, 'plashque-close').click ()
    catalog = driver.find_element (By.XPATH, "//a[contains(@href,'b/catalog.html')]")
    catalog.click ()

    driver.switch_to.window (driver.window_handles[1])
    search = driver.find_element (By.XPATH, '//*[@id="js-csearch"]')
    search.click ()
    search.clear ()
    search.click ()
    sleep (2)

    search.send_keys ('webm')
    sleep (2)
    driver.find_elements (By.CLASS_NAME, 'ctlg__img')[0].click ()

    elements = driver.find_elements (By.XPATH, "//*/figcaption/a[contains(@href, 'b')]")

    webm = 'C:\\Users\\Drayberg\\Downloads\\testsss\\webm\\'
    if not os.path.exists (webm):
        os.makedirs (webm)
    img = 'C:\\Users\\Drayberg\\Downloads\\testsss\\img\\'
    if not os.path.exists (img):
        os.makedirs (img)

    for el in elements:
        name = el.get_attribute('title')
        atr = el.get_attribute ('href')
        r = requests.get (atr)
        if atr.endswith (".mp4") or atr.endswith (".webm"):
            with open (f'{webm}{name.split ("/")[-1]}', 'wb') as f:
                qw = f.write (r.content)
                time.sleep (1)
        if atr.endswith (".jpg") or atr.endswith(".png") or atr.endswith(".gif"):
            with open (f'{img}{name.split ("/")[-1]}', 'wb') as f:
                qw = f.write (r.content)
                time.sleep (1)
        print (atr + ' - ' + name)
except Exception as ex:
    print (ex)
finally:
    sleep (10)
# driver.find_element (By.XPATH, "//[contains(@href, '.mp4')]")
# import uuid
# driver.quit ()
# if driver.find_elements (By.XPATH, "//figure/a[contains(@href, '.webm') and contains(@href, '/')]"):
#     with open (b, 'wb') as k:
#         qw = k.write (r.content)
#         time.sleep (1)
# else:
#     b = f'C:\\Users\\Drayberg\\Downloads\\testsss\\{FilesList}.mp4'
#     with open (b, 'wb') as f:
#         qw = f.write (r.content)
#         time.sleep (1)
# FilesList = uuid.uuid4 ()
# ololo = driver.find_element (By.XPATH, "//a[contains(@href, '.jpg')]")
# if driver.find_element (By.XPATH, "//main//div[1]/div[0]/[contains(@href, '.jpg')]"):
# b = f'C:\\Users\\Drayberg\\Downloads\\testsss\\{FilesList}.webm'
# s = f'C:\\Users\\Drayberg\\Downloads\\testsss\\{FilesList}.mp4'
# driver.find_elements (By.XPATH, "//figure/a[contains(@href, '.mp4') and contains(@href, '/')]")
# list_tags = ['AFG', 'FAP', 'ФАП', 'АФЗ', 'афз', 'фап', 'fap', 'afg']

# with open (f'C:\\Users\\Drayberg\\Downloads\\testsss\\{"-".join (t.split ("/")[-1:])}', 'wb') as f:
# with open ('r'newpath"-".join(t.split("/")[-1:]), 'wb') as f:
