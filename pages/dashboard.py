from pages.base_page import BasePage


class Dashboard(BasePage):
    Logo_Scouts_Panel_xpath = "//div[@title='Logo Scouts Panel']"
    Scouts_panel_header_xpath = "//h6[text()='Scouts Panel']"
    Scouts_panel_header2_xpath = "//h2[text()='Scouts Panel']"
    Scouts_panel_info_xpath = "//p"
    Activity_xpath = "//div[3]/div/div/h2"
    Shortcuts_xpath = "//*[text()='Linki pomocnicze']"
    Created_player_xpath = "//h6[1]"
    Updated_player_xpath = "//h6[2]"
    Created_match_xpath = "//h6[3]"
    Updated_match_xpath = "//h6[4]"
    Updated_report_xpath = "//h6[5]"
    Players_count_xpath = "//div[2]/div[1]/div/div[1]"
    Players_count_number_xpath = "//div[1]/div/div[2]/b"
    Matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    Matches_count_number_xpath = "//div[2]/div/div[2]/b"
    Reports_count_xpath = "//div[2]/div[3]/div/div[1]"
    Reports_count_number_xpath = "//div[3]/div/div[2]/b"
    Events_count_xpath = "//div[2]/div[4]/div/div[1]"
    Events_count_number_xpath = "//div[4]/div/div[2]/b"
    Main_page_button_xpath = "//ul[1]/div[1]"
    Players_button_xpath = "//ul[1]/div[2]"
    English_button_xpath = "//*[text()='English']"
    Polish_button_xpath = "//*[text()='Polski']"
    Sign_out_button_xpath = "//*[text()='Wyloguj']"
    Dev_team_contact_link_xpath = "//a[@tabindex='0']"
    Last_created_player_button_xpath = "//div[3]/div/div/a[1]/button"
    Last_updated_player_button_xpath = "//a[2]/button"
    Last_created_match_button_xpath = "//a[3]/button"
    Last_updated_match_button_xpath = "//a[4]/button"
    Last_updated_report_button_xpath = "//a[5]/button"
    Add_player_button_xpath = "//*[text()='Dodaj gracza']"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    EN_version_url = 'https://scouts-test.futbolkolektyw.pl/en'
    PL_version_url = 'https://scouts-test.futbolkolektyw.pl/pl'

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.Add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_Wyloguj_button(self):
        self.click_on_the_element(self.Sign_out_button_xpath)

    def click_Dev_Team_Contact_button(self):
        self.click_on_the_element(self.Dev_team_contact_link_xpath)

    def click_Gracze_button(self):
        self.click_on_the_element(self.Players_button_xpath)

    def wait_for_logo(self):
        self.wait_for_element_to_be_visible(self.Logo_Scouts_Panel_xpath)

    def change_language_EN(self):
        self.click_on_the_element(self.English_button_xpath)

    def change_language_PL(self):
        self.click_on_the_element(self.Polish_button_xpath)

    def EN_url(self):
        self.wait_for_element_to_be_clicable(self.Add_player_button_xpath)
        assert self.get_page_title(self.EN_version_url) == self.expected_title

    def PL_url(self):
        self.wait_for_element_to_be_clicable(self.Add_player_button_xpath)
        assert self.get_page_title(self.PL_version_url) == self.expected_title
