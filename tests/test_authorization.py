from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Data
from urls import Urls


def test_authorization(driver):

    ''' Проверка авторизации по кнопке "Войти в аккаунт" на главной '''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))

    assert driver.find_element(*Locators.PUSH_ORDER).text == 'Оформить заказ'
    driver.quit()

def test_authorization_lk(driver):

    ''' Проверка авторизации через кнопку «Личный кабинет» '''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.find_element(*Locators.LK_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))

    assert driver.find_element(*Locators.PUSH_ORDER).text == 'Оформить заказ'


def test_authorization_reg(driver):

    ''' Проверка авторизации через кнопку в форме регистрации '''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.get(Urls.REGISTRATION)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))

    assert driver.find_element(*Locators.PUSH_ORDER).text == 'Оформить заказ'



def test_authorization_recovery_pass(driver):

    ''' Проверка авторизации через кнопку в форме восстановления пароля '''

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.INTO_ACCOUNT_BUTTON))
    driver.get(Urls.RECOVERY)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.RECOVERY_BUTTON))
    driver.find_element(*Locators.ENTER_BUTTON_REC).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ENTER))
    driver.find_element(*Locators.EMAIL).send_keys(Data.user_email)
    driver.find_element(*Locators.PASSWORD).send_keys(Data.user_password)
    driver.find_element(*Locators.ENTER_BUTTON_A).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PUSH_ORDER))

    assert driver.find_element(*Locators.PUSH_ORDER).text == 'Оформить заказ'
