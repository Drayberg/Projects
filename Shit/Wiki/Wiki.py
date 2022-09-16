import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions ()
# options.add_argument ('--headless')
options.add_argument ('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome (options=options)
actions = ActionChains (driver)

txt = 'C:\\Users\\Drayberg\\Downloads\\testsss\\'
if not os.path.exists (txt):
    os.makedirs (txt)

try:
    wiki = driver.get ('https://ru.wikipedia.org')
    driver.find_element (By.CLASS_NAME, 'vector-search-box-input').click ()
    inp = input ("Чи ищем: ")
    ActionChains (driver).send_keys (inp).send_keys (Keys.ENTER).perform ()

    # links = driver.find_elements (By.XPATH, '//*/div[3]/div[3]/div[5]/div[1]/p/a')
    # stop = driver.find_element (By.XPATH, '//*/div[3]/div[3]/div[5]/div[1]/div[2]/ul/li[1]/a[contains(text())]')
    links1 = driver.find_elements (By.XPATH, "//div[@class='mw-parser-output']/*")
    # stop = driver.find_elements (By.XPATH, '//*[@id="toc"]/div')
    stop = driver.find_element (By.ID, 'toc')


    links = []
    for el in links1:
        if el.tag_name == 'p':
            links.append (el)
        if el.get_attribute ('id') == 'toc':
            break

    # for h in links:
    #     hs = h.find_elements (By.TAG_NAME, 'a')
    #     for link in hs:
    #         li = link.get_attribute ('href')
    #         name1 = link.get_attribute ('text')
    #         driver.get (li)
    #         ps = driver.find_elements(By.XPATH,"//div[@class='mw-parser-output']/p")
    #         for p in ps:
    #             with open (f'{txt}{name1}.txt', 'w') as f:
    #                 f.write (p.text)
    #                 sleep (2)
    #                 print (name1)
    #             if p.get_attribute ('id') == 'toc':
    #                 break
    #         with open (f'{txt}{name1}.txt', 'wb') as f:
    #             f.write (r.content)
    #             sleep (2)
    #             print (name1)
            # find_elements (By.XPATH, "//*/[@class='mw-parser-output']/p")
            # for o in r:
            #     if r:
            #         o.find_elements (By.XPATH, "//*/[@class='mw-parser-output']/p/a")

    # print(dir(links))

    # for h in links:

    # li = el.get_attribute ('href')
    # print(li)
    # name1 = el.get_attribute ('text')
    # r = requests.get (li)
    # with open (f'{txt}{name1}.txt', 'wb') as f:
    #     save = f.write (r.content)
    #     sleep (2)
    #     print (name1)

    # el_ind_st = 0
    # for ind_st, el in enumerate (stop):
    #     if el == stop:
    #         el_ind_st = ind_st
    #         break
    # stop = stop[:el_ind_st]
    # print(stop)
    # for link in links1:
    #     li = link.get_attribute ('href')
    #     name1 = link.get_attribute ('text')
    #     r = requests.get (li)
    #
    #     with open (f'{txt}{name1}.txt', 'wb') as f:
    #         save = f.write (r.content)
    #         sleep (2)
    #         print (name1)

    # print(ind)



finally:
    sleep (10)
    # print(links)

    # for stop_index in links:
    #     print(stop_index)
    #     if stop in range():
    #         break
    # print(links_mas)

    # print(links_mas)

    # name = driver.find_element (By.CLASS_NAME, 'toc').location
    # stop = links.find_element (By.ID, 'toc')
    # stop = wait (driver, 20).until(driver.implicitly_wait() (By.ID, 'toc'))
    # print(stop)

    # st_inx = 0
    # for ind, el in enumerate(links):
    #     if 'toc' in links:
    #         el_ind = ind
    #         break
    #
    # # links = links[:el_ind]
    # # print(name1)
    # print(ind)

    # for inx, st in enumerate(links):
    #     if st == stop:
    #         st_inx = inx
    #         break
    # # stop = stop[:st_inx]
    # print(inx)
