from selenium.webdriver.common.by import By
class Sidebar:
    def __init__(self,driver):
        self.driver = driver
        self.category_sidebar = (By.XPATH,"//h2[normalize-space()='Category']")

    def is_category_sidebar_visible(self):
        return self.driver.find_element(*self.category_sidebar).is_displayed()

    def get_category_sidebar(self):
        return self.driver.find_element(By.XPATH,"//h2[normalize-space()='Category']")

    def click_woman(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Women']").click()

    def click_men(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Men']").click()
    def click_woman_tops(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[href='/category_products/2']").click()
    def is_tops_visible(self):
        return self.driver.find_element(By.CSS_SELECTOR,".title.text-center").text
    def click_men_tops(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Tshirts']").click()
    def is_men_tops_visible(self):
        return self.driver.find_element(By.CSS_SELECTOR,".title.text-center").text

