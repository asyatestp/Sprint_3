from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators



def test_constructor_topping(driver):

    '''Открытие начинок'''

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.TOPPING_BUTTON)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.DIV_TOPPING)) != None

def test_constructor_sauce(driver):

    '''Открытие соусов'''

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.SOUCE_BUTTON)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.DIV_SOUCE)) != None

def test_constructor_roll(driver):

    '''Открытие булок'''
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.TOPPING_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.DIV_TOPPING))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ROLL_BAKERY)).click()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.DIV_BAKERY)) != None