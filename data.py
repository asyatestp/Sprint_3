from faker import Faker
import random

class Data:
    '''Данные к тестам авторизации'''

    USER_NAME = Faker().name()
    USER_EMAIL = Faker().email()
    USER_PASSWORD = random.randrange(100000, 10000000)

    user_name = 'Asya'
    user_email = 'asya_efimova_11@yandex.ru'
    user_password = '12345678'

    incorrect_pass = random.randrange(10000, 99999)


