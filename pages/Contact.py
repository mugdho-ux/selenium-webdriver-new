
import pytest
from selenium.webdriver.common.by import By

class Contact:
    def __init__(self, driver):
        self.driver = driver
        self.home_link = (By.XPATH, "//a[normalize-space()='Home']")
        self.contact = (By.XPATH, "//a[normalize-space()='Contact us']")
        self.up = (By.NAME, "upload_file")


    def go_to_home(self):
        self.driver.find_element(*self.home_link).click()
    def go_contact_us(self):
        self.driver.find_element(*self.contact).click()
    # def click_upload(self):
    #     self.driver.find_element(*self.up).click()
    def click_upload_file(self,filepath):
        self.driver.find_element(*self.up).send_keys(filepath)





