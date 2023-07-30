import os
import unittest

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestTranslations(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_page_translation(self):
        login = LoginPage(self.driver)
        login.type_in_email('user02@getnada.com')
        login.type_in_password('Test-1234')
        login.click_on_the_Sign_In_button()
        login.wait_for_logo()
        language = Dashboard(self.driver)
        language.change_language_EN()
        language.EN_url()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/page_translation/english-language.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/page_translation/english-language.png").show()
        language.change_language_PL()
        language.PL_url()
        self.driver.save_screenshot(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/page_translation/polish-language.png")
        Image.open(
            "C:/Users/Magda/Documents/GitHub/Challenge_Portfolio_Magda02/test_cases/Screenshots/page_translation/polish-language.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
