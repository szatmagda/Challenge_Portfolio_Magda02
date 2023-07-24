from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    language_list_xpath = "//*[@role='button']"
    Polski_button_xpath = "//li[@tabindex='0']"
    English_button_xpath = "//li[@tabindex='-1']"
    expected_title = "Scouts panel - zaloguj"
    login_url = 'https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_Sign_In_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def select_language(self, language):
        self.click_on_the_element(self.language_list_xpath)
        time.sleep(1)
        if language == "English":
            self.click_on_the_element(self.English_button_xpath)
        else:
            self.click_on_the_element(self.Polski_button_xpath)