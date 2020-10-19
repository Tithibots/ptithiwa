from selenium.webdriver.common.by import By

DESIRED_CAPS_WHATSAPP = {
    # 'deviceName': '693d887',
    # 'platformVersion': '8.1.0',
    'platformName': 'Android',
    'appPackage': 'com.whatsapp',
    'appActivity': 'com.whatsapp.Main',
    'noReset': 'true',
    'fullReset': 'false',
    'newCommandTimeout': 600000
}


class SELECTORS(object):
    DP = (By.ID, 'com.whatsapp:id/contact_photo')
    OPEN_WITH = (By.ID, 'vivo:id/alertTitle')
    WHATSAPP_NAME = (By.XPATH, "//android.widget.TextView[@text='Ⅱ·WhatsApp']")

    class CHATROOM(object):
        MESSAGE_INPUT_BOX = (By.ID, 'com.whatsapp:id/entry')

    # class CHROME(object):
    #     MAIN_MENU_OPTIONS = (By.ID, 'com.android.chrome:id/menu_button')
    #     NEW_TAB = (By.ID, 'com.android.chrome:id/menu_item_text')
    #     SEARCH_BAR = (By.ID, 'com.android.chrome:id/search_box_text')
    #     CONTINUE_TO_CHAT = (By.ID, 'action-button')
    # action-button

class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'
