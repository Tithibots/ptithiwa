__all__ = ["Contact"]

from chatroom import Chatroom
from constants import *
from pwaobject import PWaObject
from selenium.webdriver.common.keys import Keys


class Contact(Chatroom, PWaObject):

    def __init__(self, browser=None):
        super().__init__(browser)

        # self._open_chrome()
        # self._wait_for_an_element_to_be_clickable(SELECTORS.CHROME.MAIN_MENU_OPTIONS).click()
        # self._wait_for_an_element_to_be_clickable(SELECTORS.CHROME.NEW_TAB).click()
        # searchbar = self._wait_for_an_element_to_be_clickable(SELECTORS.CHROME.SEARCH_BAR)
        # searchbar.send_keys('wa.me/919592140593')
        # self.device.press_keycode(66)
        # print("Break")

    # def open_chat_by_number(self, number):
    #     print(f'Opening chatroom to "{number}"', end="... ")
    #     self._search_and_open_chat_by_name(number)
    #     print(f'{STRINGS.CHECK_CHAR} Done')
    #
    def open_chat_by_number_using_url(self, number):
        print(f'Opening chatroom to "{number}"', end="... ")
        self.driver.get('https://wa.me/' + number)
        element, winnerindex = self._race_for_presence_of_two_elements(SELECTORS.OPEN_WITH,
                                                                       SELECTORS.CHATROOM.MESSAGE_INPUT_BOX)
        if winnerindex == 0:
            self._wait_for_an_element_to_be_clickable(SELECTORS.WHATSAPP_NAME).click()
            self._wait_for_presence_of_an_element(SELECTORS.CHATROOM.MESSAGE_INPUT_BOX)
        print(f'{STRINGS.CHECK_CHAR} Done')
    #
    # def open_chat_by_name(self, name):
    #     print(f'Opening chatroom to "{name}"', end="... ")
    #     self._search_and_open_chat_by_name(name)
    #     print(f'{STRINGS.CHECK_CHAR} Done')
    #
    # def send_message_to_number(self, number, message):
    #     print(f'Sending message "{message}" to number "{number}"...', end="... ")
    #     self.open_chat_by_number(number)
    #     self._send_message(message)
    #     print(f'{STRINGS.CHECK_CHAR} Done')


# bot = Contact()
# bot.open_chat_by_number_using_url('919592140593')
