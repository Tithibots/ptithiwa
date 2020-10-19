from selenium.webdriver.common.by import By

DESIRED_CAPS = {
    # 'deviceName': '693d887',
    # 'platformVersion': '8.1.0',
    'platformName': 'Android',
    'appPackage': 'com.whatsapp',
    'appActivity': 'com.whatsapp.Main',
    'noReset': 'true',
    'fullReset': 'false'
}

class SELECTORS(object):
    DP = (By.ID, 'com.whatsapp:id/contact_photo')

