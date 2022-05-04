from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')

# disable webdriver mode
# for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument('--disable-blink-features=AutomationControlled')
# initial driver
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get(r'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
