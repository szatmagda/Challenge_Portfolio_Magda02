import os
import time
import unittest

from pages.Add_a_Player import PlayerPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestDevTeamContact(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Dev_Team_button(self):
        button_click = PlayerPage(self.driver)
        button_click.type_in_email('user02@getnada.com')
        button_click.type_in_password('Test-1234')
        button_click.click_on_the_Sign_In_button()
        time.sleep(2)
        dev_team = Dashboard(self.driver)
        dev_team.click_Dev_Team_Contact_button()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()
