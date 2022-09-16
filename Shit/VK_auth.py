import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Tools.Projects.Shit.storage import vk_login_7660, vk_password_7660

driver = selenium.webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.vk.com/')

#sigh_in
driver.find_element(by=By.XPATH, value= '/html/body/div[10]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/form/button[1]/span').click()

#inputbox
driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input').send_keys(vk_login_7660)


#click_continue
driver.find_element(by=By.XPATH, value= '/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/button/div').click()
time.sleep(2)

#password_try
driver.find_element(by=By.NAME, value = 'password').send_keys(vk_password_7660)

#click_continue
driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div/form/div[2]/button').click()
time.sleep(5)

driver.quit()

