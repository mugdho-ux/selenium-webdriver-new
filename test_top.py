import time

import pytest
from pages.Homepage import HomePage
from Baseclass import BaseClass
from pages.SIdebar import Sidebar

@pytest.mark.usefixtures("setup")
class TestA(BaseClass):
    def test_a(self):
        log = self.getLogger()
        driver = self.driver
        homepage = HomePage(driver)
        sidebar = Sidebar(driver)

        time.sleep(2)
        sidebar.click_woman()
        time.sleep(2)
        sidebar.click_men()
        time.sleep(2)
        sidebar.click_woman()
        time.sleep(2)
        sidebar.click_woman_tops()
        time.sleep(2)
        sidebar.click_men()
        time.sleep(2)
        sidebar.click_men_tops()
        time.sleep(2)
        log.info(sidebar.is_men_tops_visible())












        time.sleep(2)
