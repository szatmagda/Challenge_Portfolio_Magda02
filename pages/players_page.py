from pages.base_page import BasePage


class PlayersPage(BasePage):
    first_player_xpath = "//*[@id='MUIDataTableBodyRow-0']"
    Mecze_button_xpath = "//ul[2]/div[2]/div[2]/span"
    Download_CSV_xpath = "//div[2]/div/div/div[1]/div[2]/button"
    Dodaj_mecz_button_xpath = "//*[@class='MuiButton-label']"

    def click_first_player(self):
        self.click_on_the_element(self.first_player_xpath)

    def click_Mecze_button(self):
        self.click_on_the_element(self.Mecze_button_xpath)

    def wait_for_icon(self):
        self.wait_for_element_to_be_clicable(self.Download_CSV_xpath)

    def wait_for_button(self):
        self.wait_for_element_to_be_clicable(self.Dodaj_mecz_button_xpath)

