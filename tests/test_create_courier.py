import requests
import pytest
import allure

import helpers
from data import URLS as url
from data import ENDPOINTS as ep

from data import _debug as _debug


class TestCreateCourier:

    def test_create_courier_success(self):
        # собираем тело запроса
        payload = helpers.generate_random_courier_data()
        if _debug:
            print(f'payload = {payload}')

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        # response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        # response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        # response = requests.post(f'{url.SERVER_URL}{ep.CREATE_COURIER}', data=payload)
        response = helpers.register_courier(payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        assert response.status_code == 201
        assert response.json()['ok'] # == True

