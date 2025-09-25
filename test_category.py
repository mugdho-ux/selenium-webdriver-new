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
        print(sidebar.get_category_sidebar().text)
        assert  sidebar.is_category_sidebar_visible(), "Category sidebar is not visible"
        time.sleep(1)
        sidebar.click_woman()
        time.sleep(1)
        sidebar.click_men()
        time.sleep(1)
        sidebar.click_woman()
        time.sleep(1)
        sidebar.click_woman_tops()
        time.sleep(1)
        assert sidebar.is_tops_visible() == "WOMEN -  TOPS PRODUCTS"

        time.sleep(1)

        sidebar.click_men()
        time.sleep(1)
        sidebar.click_men_tops()
        time.sleep(1)
        log.info(sidebar.is_men_tops_visible())
        assert sidebar.is_men_tops_visible() == "MEN -  TSHIRTS PRODUCTS"
        time.sleep(1)