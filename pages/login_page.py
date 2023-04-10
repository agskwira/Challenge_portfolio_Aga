from pages.base_page import BasePage


class LoginPage(BasePage):
    Scouts_Panel_header_xpath="//*[@id="__next"]/form/div/div[1]/h5"
    login_field_xpath ="//*[@id='login']"
    password_field_xpath ="//*[@id="__next"]/form/div/div[1]/div[2]/div[1]//input"
    sign_in_button_xpath ="//*[@id="__next"]/form/div/div[2]/button//span"
    remind_password_hyperlink_xpath ="//*[@id="__next"]/form/div/div[1]/a"
    language_listbox_xpath="//*[@id="__next"]/form/div/div[2]/div[1]//div"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
