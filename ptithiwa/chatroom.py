__all__ = ["Chatroom"]

from constants import SELECTORS
from pwaobject import PWaObject
from selenium.webdriver.common.keys import Keys


class Chatroom(PWaObject):
    def __init__(self, browser=None):
        super().__init__(browser)

    # def _open_info(self):
    #     self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM.NAME).click()
    #
    # def _close_chatroom_info(self):
    #     self._wait_for_an_element_to_be_clickable(SELECTORS.CHATROOM.CLOSE_INFO).click()
    #
    # def _send_message(self, message):
    #     self._wait_for_an_element_to_be_clickable(SELECTORS.MESSAGE_INPUT_BOX).send_keys(message + Keys.ENTER)
