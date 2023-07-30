import os
import unittest

from selenium import webdriver
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_Sign_In_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        self.driver.save_screenshot("C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/login_to_the_system/success-login.png")
        Image.open("C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/login_to_the_system/success-login.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
