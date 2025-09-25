import time
import os
import pytest
from pages.Homepage import HomePage
from Baseclass import BaseClass
from pages.SIdebar import Sidebar
from pages.Contact import Contact
@pytest.mark.usefixtures("setup")
class TestA(BaseClass):
    def test_a(self):
        log = self.getLogger()
        driver = self.driver
        homepage = HomePage(driver)
        sidebar = Sidebar(driver)
        contact = Contact(driver)
        file_to_upload = os.path.abspath("test.png")
        time.sleep(2)
        contact.go_contact_us()
        time.sleep(2)
        contact.click_upload_file(file_to_upload)












        time.sleep(2)
