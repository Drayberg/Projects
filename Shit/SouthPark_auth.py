from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from Tools.Shit.storage import sp_login, sp_password
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://google.com")
driver.get ("https://sp.freehat.cc/")
try:
    # driver.maximize_window ()

# auth
#     driver.find_element (by=By.NAME, value='USER_LOGIN').send_keys (sp_login)
#     driver.find_element (by=By.NAME, value='USER_PASSWORD').send_keys (sp_password)
#     driver.find_element (by=By.CLASS_NAME, value='auth-btn').click ()

# hover_cursor
    southpark = driver.find_element (by=By.XPATH, value='//*[@id="header"]/div/div/ul/li[1]/a')
    ActionChains (driver).move_to_element (to_element=southpark).perform ()

# random
    driver.find_element(by=By.XPATH, value='//*[@id="header"]/div/div/ul/li[1]/div/ul/li[2]/a').click()
    driver.switch_to.window(driver.window_handles[0])
    # driver.close()
    sleep(5)
    # driver.find_element(by=By.XPATH, value='//*[@id="oframevideoplayer"]/pjsdiv[1]/video').click()
    video = driver.find_element(by=By.TAG_NAME, value='video')
    ActionChains(driver).move_to_element(to_element=video).key_down(Keys.SHIFT).send_keys('f').perform()
    ActionChains(driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
except Exception as ex:
    print()
finally:
    sleep(10)
    # driver.quit()

# elems = driver.find_elements(by=By.XPATH, value='//a[@href]')
# elems = driver.find_elements(by=By.XPATH, value='//video[@src]')
# for elem in elems:
#     print(elem.get_attribute('src'))
# for elem in elems:
#     print (elem.get_attribute('href'))
# driver.find_element(by=By.id, value='close-anons').click()

# url = driver.current_url
# video_try = driver.find_element(by=By.XPATH, value='//*[@src]')
# print(video_try)
#

# wait = WebDriverWait(driver, 3)
# presence = EC.presence_of_element_located()
# visible = EC.visibility_of_element_located()
# driver.get(url.format(str()))
#
# wait.until(visible((By)))

#


# play_video


# ActionChains (driver)..perform()


# items = driver.find_element(by=By.TAG_NAME, value='blob:https://sp.freehat.cc/916e93a9-4dda-4e6a-adfb-952aff4ac685').click()

# WebDriverWait (driver, 15).until(EC.element_to_be_clickable (
#     (By.XPATH, '//*[@id="oframevideoplayer"]/pjsdiv[6]/pjsdiv[4]'))).click ()
# video = driver.findElement(By=ID, value="")  # Use the id of the video to find it.
# video.click ()


# driver.switch_to.window(driver.window_handles[0])
#     driver.find_element(by=By.ID, value='pjsfrrsvideoplayer').click()

# #play video

#
# sleep (5)

# driver.switch_to.window(driver.window_handles[1])
# driver.refresh ()
