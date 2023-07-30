from pages.base_page import BasePage


class DodajGracza(BasePage):
    Add_a_player_button_xpath = "//*[text()='Dodaj gracza']"
    Imię_field_xpath = "//*[@name='name']"
    Nazwisko_field_xpath = "//*[@name='surname']"
    Data_urodzenia_field_xpath = "//*[@name='age']"
    Główna_pozycja_xpath = "//*[@name='mainPosition']"
    Submit_button_xpath = "//*[@type='submit']"
    Strona_główna_button_xpath = "//ul[1]/div[1]/div[2]/span"
    New_player_name_xpath = "//span[text()='Jan Nowak']"
    Player_form_url = "https://scouts-test.futbolkolektyw.pl/pl/players/64c53a78575dd1f94272a969/edit"
    Expected_title = "Edycja gracza Jan Nowak"
    Header_page_xpath = "//form/div[1]/div/span"
    Notification_box_xpath = "//*[@role='alert']"

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.Add_a_player_button_xpath)

    def type_in_Imię(self, imię):
        self.field_send_keys(self.Imię_field_xpath, imię)

    def type_in_Nazwisko(self, nazwisko):
        self.field_send_keys(self.Nazwisko_field_xpath, nazwisko)

    def type_in_Data(self, data):
        self.field_send_keys(self.Data_urodzenia_field_xpath, data)

    def type_in_Pozycja(self, pozycja):
        self.field_send_keys(self.Główna_pozycja_xpath, pozycja)

    def click_submit_button(self):
        self.click_on_the_element(self.Submit_button_xpath)

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.Notification_box_xpath)
        assert self.driver.title == self.Expected_title

    def wait_for_text(self):
        self.wait_for_element_to_be_visible(self.Header_page_xpath)

    def wait_for_notification(self):
        self.wait_for_element_to_be_visible(self.Notification_box_xpath)
