import os
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from constants import *

class PWaObject:
    def __init__(self, device=None):
        self.device = device
        self.device = self._open_device_if_not_opened()

    def quit(self):
        self.device.quit()

    def _open_device_if_not_opened(self):
        if self.device == None:
            self.device = webdriver.Remote('http://localhost:4723/wd/hub', DESIRED_CAPS)
            return self.device

    def _wait_for_whatsapp_to_load(self):
        self._wait_for_an_presence_of_element(SELECTORS.DP)

    def _wait_for_an_presence_of_element(self, selector):
        element = None
        try:
            element = WebDriverWait(self.device, 34).until(
                EC.presence_of_element_located(selector)
            )
        except:
            pass
        finally:
            return element

    def _wait_for_presence_of_an_element_in_other_element(self, selector, element):
        relement = None
        while True:
            try:
                relement = element.find_element(selector[0], selector[1])
            except:
                pass
            finally:
                return relement

    def _wait_for_an_element_to_be_clickable(self, selector):
        element = None
        try:
            element = WebDriverWait(self.device, 10).until(
                EC.element_to_be_clickable(selector)
            )
        except:
            pass
        finally:
            return element

    def _wait_for_an_element_to_deattached(self, element):
        while True:
            try:
                element.is_displayed()
            except:
                break
            finally:
                pass

    # def _search_and_open_chat_by_name(self, name):
    #     isfound = False
    #     self._search_and_wait_for_complete(name)
    #     preactive = None
    #     curractive = self.device.switch_to.active_element
    #     while True:
    #         curractive.send_keys(Keys.ARROW_DOWN)
    #         curractive = self.device.switch_to.active_element
    #         if curractive == preactive:
    #             break
    #         name = curractive.find_element(By.CSS_SELECTOR, SELECTORS.GROUPS.CONTACTS_SEARCH_NAME).get_attribute(
    #             'innerText')
    #         if name == name:
    #             isfound = True
    #             break
    #         preactive = curractive
    #     self._wait_for_chat_to_open(name)
    #     return isfound
    #
    # def _search_and_open_chat_by_number(self, number):
    #     self._search_and_wait_for_complete(number)
    #     self.device.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
    #     self.device.switch_to.active_element.click()
    #
    # def _wait_for_chat_to_open(self, name):
    #     nameofchat = ''
    #     while True:
    #         try:
    #             nameofchat = self._wait_for_an_presence_of_element(SELECTORS.CHATROOM.NAME).get_attribute(
    #                 'innerText')
    #         except:
    #             pass
    #         if nameofchat == name:
    #             break
    #
    # def _search_and_wait_for_complete(self, nameornumber):
    #     self._wait_for_an_element_to_be_clickable(SELECTORS.MAIN_SEARCH_BAR_SEARCH_ICON).click()
    #     self.device.switch_to.active_element.send_keys(nameornumber)
    #     self._wait_for_an_presence_of_element(SELECTORS.MAIN_SEARCH_BAR_DONE)


# pwaobjectbot = PWaObject()
# pwaobjectbot._wait_for_an_element_to_be_clickable(SELECTORS.DP).click()
#
# input("Enter...")
