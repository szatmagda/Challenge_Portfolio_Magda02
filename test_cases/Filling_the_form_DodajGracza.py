import os
import time
import unittest

from pages.add_a_player import PlayerPage
from pages.players_form import DodajGracza
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestDodajGarczaForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_filling_the_form_DodajGracza(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        button_click.wait_for_logo()
        button_click.click_on_the_add_player_button()
        button_click.wait_for_header()
        add_a_player = DodajGracza(self.driver)
        add_a_player.type_in_Imię('Jan')
        add_a_player.type_in_Nazwisko('Nowak')
        add_a_player.type_in_Data('2142002')
        add_a_player.type_in_Pozycja('Napastnik')
        add_a_player.click_submit_button()
        self.driver.implicitly_wait(5)
        add_a_player.click_strona_główna_button()
        add_a_player.visible_new_player()

    @classmethod
    def tearDown(self):
        self.driver.quit()

