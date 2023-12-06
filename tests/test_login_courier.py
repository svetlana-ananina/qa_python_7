import pytest
import allure

from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS
from helpers.helpers_on_check_response import check_status_code, check_user_id, check_message
from helpers.helpers_on_create_courier import register_courier


@pytest.mark.usefixtures("create_new_courier")
class TestLoginCourier:

    @allure.title('Проверяем, что курьер может авторизоваться')
    def test_login_courier_success(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        user_data = create_new_courier
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(user_data)
        # получаем id курьера
        user_id = check_user_id(response)
        # проверяем, что id курьера - число
        assert str(user_id).isdigit(), f'Неверный id курьера: ожидалось число, получен id = {user_id}'


    @pytest.mark.parametrize('key', [KEYS.LOGIN, KEYS.PASSWORD])
    @allure.title('Проверяем, что если не передано поле логина или пароля, запрос возвращает ошибку 400')
    def test_login_courier_missing_field_error(self, create_new_courier, key):
        # создаем нового курьера и получаем его данные
        user_data = create_new_courier
        # формируем данные для запроса без поля key
        payload = user_data.copy()
        payload.pop(key)
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(payload)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_BAD_REQUEST)


    # @pytest.mark.usefixtures("create_new_courier")
    @pytest.mark.parametrize('field_key, field_value', [(KEYS.LOGIN, ''), (KEYS.PASSWORD, '')])
    @allure.title('Проверяем, что если передано пустое поле логина или пароля, запрос возвращает ошибку 400')
    def test_login_courier_empty_field_error(self, create_new_courier, field_key, field_value):
        # создаем нового курьера и получаем его данные
        user_data = create_new_courier
        # формируем данные для запроса с пустым полем key
        payload = user_data.copy()
        payload[field_key] = field_value
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(payload)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_BAD_REQUEST)


    @pytest.mark.parametrize('field_key, field_value', [(KEYS.LOGIN, '12345'), (KEYS.PASSWORD, '12345')])
    @allure.title('Проверяем, что если если неправильно указать логин или пароль, запрос возвращает ошибку 404')
    def test_login_courier_invalid_login_error(self, create_new_courier, field_key, field_value):
        # создаем нового курьера и получаем его данные
        user_data = create_new_courier
        # формируем данные для запроса с неправильным полем field_key
        payload = user_data.copy()
        payload[field_key] = field_value
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(payload)
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_NOT_FOUND)

