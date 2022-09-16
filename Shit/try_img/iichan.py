from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import uuid
import time


def get_chrome_options():
    options = Options ()
    # options.add_argument ('-headless')
    return options


options = webdriver.ChromeOptions ()
options.add_argument ('--disable-blink-feature=AutomationControlled')
options.add_argument ("user-data-dir=C:\\profile")

driver = webdriver.Chrome (options=get_chrome_options ())
driver.get ('https://iichan.hk/b/')

answer = driver.find_element (By.XPATH, "//form/div[1]/a[contains(text(),'Ответ')][1]")
answer.click ()

element1 = driver.find_elements (by=By.CLASS_NAME, value='imglink')

for el in element1:
    t = el.get_attribute ('href')
    r = requests.get (t)
    FilesList = uuid.uuid4 ()
    # ololo = driver.find_element (By.XPATH, "//a[contains(@href, '.jpg')]")
    if driver.find_element (By.XPATH, "//a[contains(@href, '.jpg') or contains(@href, '.webm') ]"):
        s = f'C:\\Users\\Drayberg\\Downloads\\testsss\\{FilesList}.jpg'
    elif driver.find_element (By.XPATH, "//[contains(@href, '.webm')]"):
            s = f'C:\\Users\\Drayberg\\Downloads\\testsss\\{FilesList}.webm'
    with open (s, 'wb') as f:
        qw = f.write (r.content)
        time.sleep (1)
    print (r)

# r = requests.get(t)
# print('------------' + t)

# fnd_img1 = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "img")))
# # driver.quit ()
# print(fnd_img1)
# r = requests.get (fnd_img)

# with open ('iichan.jpg', 'wb') as f:
#     f.write (r.content)

# req = requests.get ("https://iichan.hk/b/")
# html = BeautifulSoup (req.content, 'html.parser')
#
# for el in html.select ("._blank > .src"):
#     title = el.select ('.caption > a')
#     print (title[0].text)

# grab_img = requests.get(img)
# out = open("C:\\Users\\Drayberg\\Desktop\\egd", "wb")
# out.write(grab_img.content)
# out.close()
