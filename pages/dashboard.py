
from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_button_xpath = "/html/body/div/div/div/div/div/ul[1]/div[1]"
    Players_button_xpath = "//ul[1]/div[2]"
    Polski_button_xpath = "/html/body/div/div/div/div/div/ul[2]/div[1]"
    Sign_out_button_xpath = "//*[text()='Wyloguj']"
    Dev_team_contact_link_xpath = "//a[@tabindex='0']"
    Last_created_player_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[1]/button"
    Last_updated_player_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[2]/button"
    Last_created_match_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[3]/button"
    Last_updated_match_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[4]/button"
    Last_updated_report_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[5]/button"
    Add_player_button_xpath = "//*[text()='Dodaj gracza']"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'


    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.Add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_Wyloguj_button(self):
        self.click_on_the_element(self.Sign_out_button_xpath)

    def click_Dev_Team_Contact_button(self):
        self.click_on_the_element(self.Dev_team_contact_link_xpath)

    def click_Gracze_button(self):
        self.click_on_the_element(self.Players_button_xpath)