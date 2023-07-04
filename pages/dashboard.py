from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_button_xpath = "/html/body/div/div/div/div/div/ul[1]/div[1]"
    Players_button_xpath = "/html/body/div/div/div/div/div/ul[1]/div[2]"
    Polski_button_xpath = "/html/body/div/div/div/div/div/ul[2]/div[1]"
    Sign_out_button_xpath = "/html/body/div/div/div/div/div/ul[2]/div[2]"
    Dev_team_contact_link_xpath = "//a[@tabindex='0']"
    Add_player_button_xpath = "/html/body/div/div/main/div[3]/div[2]/div/div/a/button"
    Last_created_player_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[1]/button"
    Last_updated_player_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[2]/button"
    Last_created_match_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[3]/button"
    Last_updated_match_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[4]/button"
    Last_updated_report_button_xpath = "/html/body/div/div/main/div[3]/div[3]/div/div/a[5]/button"
    pass