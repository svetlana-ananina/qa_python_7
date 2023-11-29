import requests
import pytest
import allure


from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
import helpers

from data import _debug as _debug


# метод создания нового курьера, возвращает данные нового курьера: логин, пароль и имя
# если создание не успешно, возвращает None
@allure.step('Создаем нового курьера')
@pytest.fixture()
def create_new_courier():
    # собираем тело запроса =данные нового курьера
    user_data = helpers.generate_random_courier_data()

    # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
    #response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    response = helpers.create_courier(user_data)

    # если регистрация прошла успешно (код ответа 201), возвращаем данные нового курьера
    if response.status_code == code.CREATED:
        return user_data
    else:
        return None

# метод создания и регистрации нового курьера, возвращает данные курьера: логин, пароль, имя и id
# если регистрация не удалась, возвращает None
@allure.step('Создаем и регистрируем нового курьера')
@pytest.fixture()
def register_new_courier(create_new_courier):

    # создаем нового курьера и получаем его данные
    #   user_data - словарь с полями login, password, firstName
    user_data = create_new_courier
    if user_data is None:
        return None
    if _debug:
        print(f'user_data = {user_data}')

    # отправляем запрос на регистрацию курьера
    response = helpers.register_courier(user_data)

    # проверяем что регистрация прошла успешно: код ответа 200
    if response.status_code != code.OK:  # 200
        return None
    # получаем id курьера и сохраняем его
    user_id = response.json()['id']
    if _debug:
        print(f'user_id = {user_id}')

    user_data['id'] = user_id
    if _debug:
        print(f'user_data = {user_data}')

    return user_data

