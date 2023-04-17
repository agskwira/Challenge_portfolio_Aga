import time

from pages.base_page import BasePage


class Add_player(BasePage):
    expected_title = "Add player"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    def title_of_page(self):
        time.sleep(2)
        assert self.get_page_title(self.add_player_url) == self.expected_title
