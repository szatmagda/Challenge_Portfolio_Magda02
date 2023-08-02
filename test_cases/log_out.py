import os
import unittest

from pages.add_a_player import PlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestWyloguj(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Wyloguj_button(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        log_out = Dashboard(self.driver)
        log_out.wait_for_logo()
        log_out.click_on_Wyloguj_button()
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/log_out/log-in-page.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/log_out/log-in-page.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
