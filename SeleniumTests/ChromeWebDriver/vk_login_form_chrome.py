from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from auth_data import vk_mobile_numb, vk_password
import time

# ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0')
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get(url=r'https://vk.com/')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'VkIdForm__signInButton').click()
    time.sleep(2)
    phone_input = driver.find_element(By.CLASS_NAME, 'vkc__TextField__input')
    phone_input.clear()
    phone_input.send_keys(vk_mobile_numb)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'vkc__Button__fluid').click()
    time.sleep(2)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'vkc__Button__title').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
