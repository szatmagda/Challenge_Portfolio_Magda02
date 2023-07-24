import os
import time
import unittest

from pages.Players_form import DodajGracza
from pages.Players_page import PlayersPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestEditForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_editing_players_form(self):
        button_click = LoginPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        time.sleep(2)
        players_click = Dashboard(self.driver)
        players_click.click_Gracze_button()
        time.sleep(4)
        players_page = PlayersPage(self.driver)
        players_page.click_first_player()
        time.sleep(2)
        editing_page = DodajGracza(self.driver)
        editing_page.type_in_Imię('zzz')
        editing_page.click_submit_button()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()


class TestMeczeButton(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Mecze_button(self):
        button_click = LoginPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        time.sleep(2)
        players_click = Dashboard(self.driver)
        players_click.click_Gracze_button()
        time.sleep(4)
        players_page = PlayersPage(self.driver)
        players_page.click_first_player()
        time.sleep(2)
        players_page.click_Mecze_button()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()