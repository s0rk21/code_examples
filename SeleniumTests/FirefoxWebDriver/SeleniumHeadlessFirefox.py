from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')

# headless mode
options.headless = True

# driver initial
s = Service(r'C:\Users\s0rk1\PycharmProjects\testing\firefoxdriver\geckodriver.exe')
driver = webdriver.Firefox(service=s, options=options)

try:
    # Переход на youtube.com
    print('Переходим на youtube.com')
    driver.get(r'https://www.youtube.com/channel/UC-kS-XNcFW9FgCMsUQbUPLw')
    time.sleep(2)
    # Открытие видеоролика
    print('Начинается проигрываение видеоролика')
    driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-grid-video-renderer[2]').click()
    time.sleep(10)
    # Закрытие ролика
    print('Заканчивается проигрывание видеоролика')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
