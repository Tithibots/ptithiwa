import os
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = '693d887'

desired_caps['appPackage'] = 'com.whatsapp'
desired_caps['appActivity'] = 'com.whatsapp.Main'

desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = 'false'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
element = WebDriverWait(driver, 34).until(
                EC.presence_of_element_located((By.ID, 'com.whatsapp:id/contact_selector'))
            )
element.click()

input("Enter...")