import os
import time
import unittest

from selenium import webdriver

from pages.Add_a_Player import PlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_click_Add_a_player_button(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        time.sleep(3)
        button_click.click_on_the_add_player_button()
        button_click.title_of_page()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()