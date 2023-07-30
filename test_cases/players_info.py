import os
import unittest

from pages.players_form import DodajGracza
from pages.players_page import PlayersPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestPlayersPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_editing_players_form(self):
        button_click = LoginPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        button_click.wait_for_logo()
        players_click = Dashboard(self.driver)
        players_click.click_Gracze_button()
        players_page = PlayersPage(self.driver)
        players_page.wait_for_icon()
        players_page.click_first_player()
        editing_page = DodajGracza(self.driver)
        editing_page.wait_for_text()
        editing_page.type_in_Imię('zzz')
        editing_page.click_submit_button()
        editing_page.wait_for_notification()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/players_info/successful-player-edit.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/players_info/successful-player-edit.png").show()

    def test_Mecze_button(self):
        button_click = LoginPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        button_click.wait_for_logo()
        players_click = Dashboard(self.driver)
        players_click.click_Gracze_button()
        players_page = PlayersPage(self.driver)
        players_page.click_first_player()
        players_page.click_Mecze_button()
        players_page.wait_for_button()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/players_info/mecze-page.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/players_info/mecze-page.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
