from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_header_xpath ="//*[@id='__next'/form/div/div[1]/h5"
    login_field_xpath ="//*[@id='login']"
    password_field_xpath ="//*[@id='__next']/form/div/div[1]/div[2]/div[1]//input"
    sign_in_button_xpath ="//*[@id='__next']/form/div/div[2]/button//span"
    remind_password_hyperlink_xpath ="//*[@id='__next']/form/div/div[1]/a"
    language_listbox_xpath ="//*[@id='__next']/form/div/div[2]/div[1]//div"

    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/login"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get_page_title() == self.expected_title
