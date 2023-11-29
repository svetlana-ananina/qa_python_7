import requests
import pytest
import allure

import helpers
from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text

from data import _debug as _debug


@pytest.mark.usefixtures("create_new_courier")
class TestLoginCourier:

    def test_login_courier_success(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        #   user_data - словарь с полями login, password, firstName
        user_data = create_new_courier
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = helpers.register_courier(user_data)

        # проверяем что регистрация прошла успешно: код ответа 200
        assert response.status_code == code.OK      # 200
        # получаем id курьера в системе и сохраняем его
        user_id = response.json()['id']

        if _debug:
            print(f'user_id = {user_id}')

