import random
import string

import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep

from data import _debug as _debug


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


# генерируем логин, пароль и имя курьера
@allure.step('Генерируем данные нового курьера: login, password, firstName')
def generate_random_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    # собираем тело запроса
    login_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    # возвращаем словарь
    return login_data


@allure.step('Отправляем API-запрос на создание нового курьера')
def create_courier(payload):
    # отправляем запрос на создание курьера и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.CREATE_COURIER}'
    if _debug:
        print(f'\nСоздаем нового курьера: payload="{payload}"')
    response = requests.post(f'{request_url}', data=payload)
    return response


@allure.step('Отправляем API-запрос на регистрацию нового курьера/получение id курьера')
def register_courier(payload):
    request_url = f'{url.SERVER_URL}{ep.LOGIN_COURIER}'
    if _debug:
        print(f'\nРегистрируем нового курьера/получаем его user_id/проверяем, что курьер существует: payload="{payload}"')
    # отправляем запрос на регистрацию курьера в системе и возвращаем ответ
    response = requests.post(f'{request_url}', data=payload)
    return response

