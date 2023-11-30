import pytest
import allure

from helpers import helpers_on_delete_courier
from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS
from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_user_id, \
    check_message
from helpers.helpers_on_create_courier import register_courier


@pytest.mark.usefixtures("create_new_courier")
class TestLoginCourier:

    @allure.title('Проверяем, что курьер может авторизоваться')
    def test_login_courier_success(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что курьер создан: код ответа 201, тело ответа {'ok' = True}
        check_status_code(response, code.CREATED)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(user_data)
        # получаем id курьера
        user_id = check_user_id(response)
        # проверяем, что id курьера - число
        assert str(user_id).isdigit(), f'Неверный id курьера: ожидалось число, получен id = {user_id}'


    @allure.title('Проверяем, что если не передано поле логина, запрос возвращает ошибку')
    def test_login_courier_missing_login_error(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что курьер создан: код ответа 201, тело ответа {'ok' = True}
        check_status_code(response, code.CREATED)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)
        # формируем данные для запроса без поля login
        payload = user_data.copy()
        payload.pop(KEYS.LOGIN)
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(payload)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_BAD_REQUEST)


    @allure.title('Проверяем, что если не передано поле пароля, запрос возвращает ошибку')
    def test_login_courier_missing_password_error(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что курьер создан: код ответа 201, тело ответа {'ok' = True}
        check_status_code(response, code.CREATED)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)
        # формируем данные для запроса без поля password
        payload = user_data.copy()
        payload.pop(KEYS.PASSWORD)
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = register_courier(payload)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_BAD_REQUEST)

