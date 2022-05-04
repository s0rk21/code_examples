from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from auth_data import vk_mobile_numb, vk_password
import time

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    'user-agent=Mozilla/5.0 (Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0')

# disable webdriver mode
# for ChromeDriver version 79.0.3945.16 or over
options.add_argument('--disable-blink-features=AutomationControlled')

# headless mode
options.headless = True
# options.add_argument('--headdless')

# driver initial
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

try:
    # going to vk.com
    print('Переходим на страницу вк')
    driver.get(url=r'https://vk.com/')
    time.sleep(1)
    # authorization
    print('Проходим авторизацию вк')
    driver.find_element(By.CLASS_NAME, 'VkIdForm__signInButton').click()
    time.sleep(1)
    phone_input = driver.find_element(By.CLASS_NAME, 'vkc__TextField__input')
    phone_input.clear()
    phone_input.send_keys(vk_mobile_numb)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'vkc__Button__fluid').click()
    time.sleep(1)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'vkc__Button__title').click()
    time.sleep(4)
    # going to main page
    print('Переходим на страницу профиля вк')
    driver.find_element(By.ID, 'l_pr').click()
    time.sleep(5)
    # start video
    print('Запускаем произведение видео')
    driver.find_element(By.CLASS_NAME, 'page_video_play_icon').click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
