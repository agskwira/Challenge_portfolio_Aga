from lib2to3.pgen2 import driver

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    scouts_panel_header_xpath = "//*[@id='__next'/form/div/div[1]/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='__next']/form/div/div[1]/div[2]/div[1]//input"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button//span"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_listbox_xpath = "//*[@id='__next']/form/div/div[2]/div[1]//div"
    invalid_pass_or_login_xpath = "//*[text()='Identifier or password invalid.']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    # message_url ="https://scouts-test.futbolkolektyw.pl/en/login"
    expected_message = "Identifier or password invalid."
    expected_text = "Identifier or password invalid."
    screenshot_url = "https://scouts-test.futbolkolektyw.pl/en/login?redirected=true"
    screenshot_name = "login.png"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_remind_password_hyperlink(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    #
    #def invalid_username_password(self):
        #assert self.get_field_message(self.invalid_pass_or_login_xpath).text == self.expected_message

    def message_invalid_password_username(self):
        time.sleep(2)
        self.assert_element_text(self.driver, self.invalid_pass_or_login_xpath, self.expected_text)

    def save_screenshot(self):
        self.screenshot(self.driver, self.screenshot_url,self.screenshot_name)





