import time

from pages.base_page import BasePage


class RemindPassword(BasePage):
    send_button_xpath = "//*[text()='Send']"
    remind_pass_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'
    expected_title = 'Remind password'
    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.send_button_xpath)
        assert self.get_page_title(self.remind_pass_url) == self.expected_title
