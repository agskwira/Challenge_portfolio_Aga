import time

from pages.base_page import BasePage



class Add_player(BasePage):
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    expected_title = "Add player"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    def title_of_page(self):
        time.sleep(2)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
            self.field_send_keys(self.surname_xpath, surname)