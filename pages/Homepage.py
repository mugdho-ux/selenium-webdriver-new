
import pytest
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_link = (By.XPATH, "//a[normalize-space()='Home']")
        self.signup_login_link = (By.XPATH, "//a[normalize-space()='Signup / Login']")

    def go_to_home(self):
        self.driver.find_element(*self.home_link).click()

    def go_to_signup_login(self):
        self.driver.find_element(*self.signup_login_link).click()
