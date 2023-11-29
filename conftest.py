import requests
import pytest
import allure


from data import URLS as url
from data import ENDPOINTS as ep
import helpers

from data import _debug as _debug


# метод регистрации нового курьера возвращает данные нового курьера: логин, пароль и имя
# если регистрация не удалась, возвращает None
@pytest.fixture()
def register_new_courier():
    # собираем тело запроса =данные нового курьера
    payload = helpers.generate_random_courier_data()

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    #response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    response = helpers.register_courier(payload)

    # если регистрация прошла успешно (код ответа 201), возвращаем данные нового курьера
    if response.status_code == 201:
        return payload
    else:
        return None
