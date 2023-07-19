from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import Urls
from data import Data



def test_registration(driver):

    '''Проверка регистрации на валидных данных'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.get(Urls.REGISTRATION)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
    driver.find_element(*Locators.REG_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*Locators.REG_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*Locators.REG_PASSWORD).send_keys(Data.USER_PASSWORD)
    driver.find_element(*Locators.REG_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))

    assert driver.find_element(*Locators.FORM_ENTER).text == 'Вход'



def test_registration_incorrect_pass(driver):

    '''Проверка сообщения об ошибке при указании некорректного пароля'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.get(Urls.REGISTRATION)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
    driver.find_element(*Locators.REG_NAME).send_keys(Data.USER_NAME)
    driver.find_element(*Locators.REG_EMAIL).send_keys(Data.USER_EMAIL)
    driver.find_element(*Locators.REG_PASSWORD).send_keys(Data.incorrect_pass)
    driver.find_element(*Locators.REG_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INCORRECT_PASS))

    assert driver.find_element(*Locators.INCORRECT_PASS).text == 'Некорректный пароль'









