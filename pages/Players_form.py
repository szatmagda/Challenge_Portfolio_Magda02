from pages.base_page import BasePage


class DodajGracza(BasePage):
    Add_a_player_button_xpath = "//*[text()='Dodaj gracza']"
    Imię_field_xpath = "//*[@name='name']"
    Nazwisko_field_xpath = "//*[@name='surname']"
    Data_urodzenia_field_xpath = "//*[@name='age']"
    Główna_pozycja_xpath = "//*[@name='mainPosition']"
    Submit_button_xpath = "//*[@type='submit']"

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
