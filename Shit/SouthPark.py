import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

driver = selenium.webdriver.Chrome()
driver.maximize_window()
driver.get("https://sp.freehat.cc/")


southpark = driver.find_element (by=By.XPATH, value='//*[@id="header"]/div/div/ul/li[1]/a')
ActionChains (driver).move_to_element (to_element=southpark).perform()

#random
driver.find_element (by=By.XPATH, value='//*[@id="header"]/div/div/ul/li[1]/div/ul/li[2]/a').click ()
sleep(5.0)

#play video
driver.find_element(by=By.ID, value='pjsfrrsvideoplayer').click()

# driver.switch_to.window(driver.window_handles[1])



# driver.refresh ()
sleep (5)
# driver.quit ()

# serial = driver.find_element(by=By.XPATH, value='//*[@id="slider-season-12"]').click()

# pickSeason12 = driver.find_element(by=By.XPATH, value='//*[@id="serial-ep"]/li[14]/a').click()
# pickSeason12.click()

# pickSerial5 = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div[3]/table/tbody/tr[4]/td[1]/div')
# pickSerial5.click()

# play1 = driver.find_element(by=By.XPATH, value='//*[@id="oframevideoplayer"]/pjsdiv[1]/video')
# play1.click()

# driver.quit(5)
# switchPage = driver.find_element(by=By.TAG_NAME, value='body')


# driver.find_element(by=By.XPATH, value='//*[@id="close-anons"]').click()


# ActionChains(driver).move_to_element(to_element=videoPlay).click().perform()
