import pytest
from selenium import webdriver
from faker import Faker
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def fake():
    faker = Faker()
    return faker