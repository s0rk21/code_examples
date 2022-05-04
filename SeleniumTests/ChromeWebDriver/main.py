from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import time

ua = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument('user-agent=My_user_agent')
options.add_argument(f'user-agent={ua.random}')
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get(url=r'https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    time.sleep(5)
    # driver.refresh()
    # driver.save_screenshot('screen1.png')
    # driver.get(url=r"https://vk.com/")
    # driver.get_screenshot_as_file('screen2.png')
    # time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
