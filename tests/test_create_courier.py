import requests
import pytest
import allure

import helpers
from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text

from data import _debug as _debug


class TestCreateCourier:

    @allure.title('Проверяем, что можно создать нового курьера')
    #@allure.description('Отправляем запрос на создание нового курьера и проверяем полученный код и тело ответа')
    def test_create_courier_success(self):
        # получаем данные для нового курьера и собираем тело запроса
        user_data = helpers.generate_random_courier_data()
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
        response = helpers.create_courier(user_data)

        # проверяем что регистрация прошла успешно: получен код ответа 201, тело ответа {'ok' = True}
        assert response.status_code == code.CREATED     # 201
        assert response.json()[text.OK_TEXT]            # 'ok' == True

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_courier_double_courier_not_created(self):
        # получаем данные для нового курьера и собираем тело запроса
        user_data = helpers.generate_random_courier_data()
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
        # response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=user_data)
        response = helpers.create_courier(user_data)

        # проверяем что регистрация прошла успешно: код ответа 201, тело ответа  {'ok' = True }
        # assert response.status_code == 201 and response.json()['ok'] # == True
        assert response.status_code == code.CREATED and response.json()[text.OK_TEXT]   # == True

        # делаем повторную попытку зарегистрировать курьера с теми же данными
        response = helpers.create_courier(user_data)

        # проверяем что получен код ответа 409 и сообщение об ошибке
        assert response.status_code == code.CONFLICT
        assert response.json()[text.MESSAGE_TEXT] == text.LOGIN_ALREADY_USED_TEXT

    @allure.title('Проверяем, что нельзя создать двух курьеров с одинаковым логином')
    def test_create_courier_double_login_not_created(self):
        # получаем данные для нового курьера и собираем тело запроса
        user_data = helpers.generate_random_courier_data()
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на создание нового курьера и получаем ответ в переменную response
        response = helpers.create_courier(user_data)

        # проверяем что регистрация прошла успешно: код ответа 201, тело ответа  {'ok' = True }
        # assert response.status_code == 201 and response.json()['ok'] # == True
        assert response.status_code == code.CREATED and response.json()[text.OK_TEXT]   # == True

        # делаем повторную попытку зарегистрировать курьера с тем же логином
        # генерируем новые данные для создания курьера
        new_user_data = helpers.generate_random_courier_data()
        # сохраняем старый логин
        new_user_data['login'] = user_data['login']
        if _debug:
            print(f'new_user_data = {new_user_data}')

        # отправляем запрос на создание нового курьера и получаем ответ в переменную response
        response = helpers.create_courier(new_user_data)

        # проверяем что получен код ответа 409 и сообщение об ошибке
        assert response.status_code == code.CONFLICT
        assert response.json()[text.MESSAGE_TEXT] == text.LOGIN_ALREADY_USED_TEXT

    @allure.title('Проверяем, что если не передано поле логина, то запрос возвращает ошибку')
    def test_create_courier_missing_login_error(self):
        # получаем данные для нового курьера и собираем тело запроса
        user_data = helpers.generate_random_courier_data()
        user_data['login'] = ""
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на создание нового курьера
        response = helpers.create_courier(user_data)

        # проверяем что получен код ответа 400 и сообщение об ошибке
        assert response.status_code == code.BAD_REQUEST
        assert response.json()[text.MESSAGE_TEXT] == text.NOT_ALL_DATA_RECEIVED_TEXT

    @allure.title('Проверяем, что если не передано поле пароля, то запрос возвращает ошибку')
    def test_create_courier_missing_password_error(self):
        # получаем данные для нового курьера и собираем тело запроса
        user_data = helpers.generate_random_courier_data()
        user_data['password'] = ""
        if _debug:
            print(f'user_data = {user_data}')

        # отправляем запрос на создание нового курьера
        response = helpers.create_courier(user_data)

        # проверяем что получен код ответа 400 и сообщение об ошибке
        assert response.status_code == code.BAD_REQUEST
        assert response.json()[text.MESSAGE_TEXT] == text.NOT_ALL_DATA_RECEIVED_TEXT

    # @allure.title('Проверяем, что если не передано поле имени, то запрос возвращает ошибку')
    # def test_create_courier_missing_user_name_error(self):
    #    # получаем данные для нового курьера и собираем тело запроса
    #    user_data = helpers.generate_random_courier_data()
    #    user_data['firstName'] = ""
    #    if _debug:
    #        print(f'user_data = {user_data}')
    #
    #    # отправляем запрос на создание нового курьера
    #    response = helpers.create_courier(user_data)
    #
    #    # проверяем что получен код ответа 400 и сообщение об ошибке
    #    assert response.status_code == code.BAD_REQUEST
    #    assert response.json()[text.MESSAGE_TEXT] == text.NOT_ALL_DATA_RECEIVED_TEXT

