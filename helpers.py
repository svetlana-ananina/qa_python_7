import requests
import random
import string

from data import URLS as url
from data import ENDPOINTS as ep

from data import _debug as _debug


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


# генерируем логин, пароль и имя курьера
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

def create_courier(user_data):
    # отправляем запрос на создание курьера и сохраняем ответ в переменную response
    if _debug:
        print(f'requests.post("{url.SERVER_URL}{ep.CREATE_COURIER}", data={user_data})')

    # response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=user_data)
    response = requests.post(f'{url.SERVER_URL}{ep.CREATE_COURIER}', data=user_data)

    if _debug:
        print(f'response.status_code = {response.status_code}')
        print(f'response.text = {response.text}')
        print(f'response.json() = {response.json()}')

    return response

def register_courier(user_data):
    # отправляем запрос на регистрацию курьера в системе и сохраняем ответ
    # формируем данные для запроса: логин и пароль курьера
    payload = {
        "login": user_data["login"],
        "password": user_data["password"]
    }

    if _debug:
        print(f'requests.post("{url.SERVER_URL}{ep.LOGIN_COURIER}", payload={payload})')

    # response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    response = requests.post(f'{url.SERVER_URL}{ep.LOGIN_COURIER}', data=payload)

    if _debug:
        print(f'response.status_code = {response.status_code}')
        print(f'response.text = {response.text}')
        print(f'response.json() = {response.json()}')

    return response

def delete_courier(user_id):
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    # return response
    pass

