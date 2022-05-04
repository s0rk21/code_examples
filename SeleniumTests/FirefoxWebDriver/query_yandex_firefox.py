from selenium import webdriver
from selenium.webdriver.firefox.service import Service
# from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

import time

# ua = UserAgent()
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')
# url = 'https://yandex.ru/'
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\firefoxdriver\geckodriver.exe')
driver = webdriver.Firefox(service=s, options=options)

try:
    driver.get(url=r'https://yandex.ru/')
    time.sleep(2)
    query_input = driver.find_element(By.NAME, 'text')
    query_input.clear()
    query_input.send_keys('Котики')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'mini-suggest__button').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'UniSearchHeader-Title').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
