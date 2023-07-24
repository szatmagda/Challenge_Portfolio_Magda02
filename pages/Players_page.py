from pages.base_page import BasePage


class PlayersPage(BasePage):
    first_player_xpath = "//*[@id='MUIDataTableBodyRow-0']"
    Mecze_button_xpath = "//ul[2]/div[2]/div[2]/span"

    def click_first_player(self):
        self.click_on_the_element(self.first_player_xpath)

    def click_Mecze_button(self):
        self.click_on_the_element(self.Mecze_button_xpath)
