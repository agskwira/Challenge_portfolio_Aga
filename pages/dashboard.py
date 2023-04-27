import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_hyperlink_xpath = "//*[text()='Main page']"
    players_page_hyperlink_xpath = "//*[text()='Players']"
    language_button_xpath = "//*[@class='jss59']/ul[2]/div[1]/div[2]/span[1]"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_panel_title_xpath = "//*[text()='Players count']"
    players_count_panel_counter_xpath = "//*[@class='jss4']/main/div[2]/div[1]/div[1]/div[2]/b"
    matches_count_panel_title_xpath = "//*[text()='Matches count']"
    reports_count_panel_title_xpath = "//*[text()='Reports count']"
    events_count_panel_title_xpath = "//*[text()='Events count']"
    scouts_panel_logo_xpath = "//*[@title='Logo Scouts Panel']"
    scouts_panel_title_xpath = "//*[text()='Scouts Panel']"
    scouts_panel_text_xpath = "//*[@class='jss4']/main/div[3]/div[1]/div[1]/div[2]/p"
    dev_team_contact_hyperlink_xpath = "//*[@class='jss4']/main/div[2]/div[1]/div[1]/div[2]/b"
    title_of_page = "//*[text()='Scouts Panel']"
    add_player_button_xpath ="//*[text()='Add player']"

    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_on_add_player_button(self):
         self.click_on_the_element(self.add_player_button_xpath)