from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Data
from urls import Urls


def test_authorization_lk(driver):

    '''Переход в личный кабинет по кнопке "Личный кабинет" на главной странице'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))
    driver.find_element(*Locators.LK_BUTTON).click()

    assert  driver.find_element(*Locators.SAVE_BUTTON).text == 'Сохранить'



def test_transition_to_the_constructor(driver):

    '''Переход из личного кабинета в конструктор'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))
    driver.find_element(*Locators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    assert driver.current_url == Urls.MAIN



def test_switching_to_the_logo(driver):

    '''Переход из личного кабинета в конструктор по нажатию на логотип Stellar Burgers'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))
    driver.find_element(*Locators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))
    driver.find_element(*Locators.LOGO_BUTTON).click()

    assert driver.current_url == Urls.MAIN


def test_logout(driver):

    '''Выход из аккаунта по кнопке «Выйти» в личном кабинете'''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))
    driver.find_element(*Locators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON_A))

    assert driver.current_url == Urls.LOGIN


