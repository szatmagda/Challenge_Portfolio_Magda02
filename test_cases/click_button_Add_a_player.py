import os
import unittest

from selenium import webdriver

from pages.add_a_player import PlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_click_Add_a_player_button(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        button_click.wait_for_logo()
        button_click.click_on_the_add_player_button()
        button_click.title_of_page()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/click_button_Add_a_player/Add-a-player-form.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/click_button_Add_a_player/Add-a-player-form.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
