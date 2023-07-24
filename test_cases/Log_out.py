import os
import time
import unittest

from pages.Add_a_Player import PlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestWyloguj(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Wyloguj_button(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        time.sleep(2)
        log_out = Dashboard(self.driver)
        log_out.click_on_Wyloguj_button()
        time.sleep(2)
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()
