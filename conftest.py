import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def setup(request):
    browser = request.param
    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # Auto-manage correct ChromeDriver version
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.automationexercise.com/"
    driver.get(url)
    request.cls.driver = driver

    yield
    driver.quit()
