from pages.base_page import BasePage


class PlayerPage(BasePage):
    Add_a_player_button_xpath = "//*[text()='Dodaj gracza']"
    expected_title = "Dodaj gracza"
    Player_form_url = "https://dareit.futbolkolektyw.pl/pl/players/add"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    Scouts_panel_logo_xpath = "//div[@title='Logo Scouts Panel']"
    Header_xpath = "//form/div[1]/div/span"

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.Add_a_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.Player_form_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_Sign_In_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def wait_for_logo(self):
        self.wait_for_element_to_be_visible(self.Scouts_panel_logo_xpath)

    def wait_for_header(self):
        self.wait_for_element_to_be_visible(self.Header_xpath)
