from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Tools.Shit.storage import sp_login, password68
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://anivisual.net/')

driver.find_element(by=By.XPATH, value='/html/body/header/div/div[2]/div/div[2]/ul/li[1]/a').click()
sleep(2)
login = driver.find_element(by=By.NAME, value='user').send_keys(sp_login)
sleep(2)
driver.find_element (by=By.NAME, value='password').click ()
ActionChains(driver).send_keys(password68).send_keys(Keys.ENTER).perform()

