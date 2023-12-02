import pytest
import allure

from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS
from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message
from helpers.helpers_on_create_courier import generate_random_courier_data, create_courier


@pytest.mark.usefixtures("create_new_courier")
class TestCreateCourier:

    @allure.title('Проверяем, что можно создать нового курьера')
    # @allure.description('Отправляем запрос на создание нового курьера и проверяем полученный код и тело ответа')
    def test_create_courier_success(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что получен код ответа 201
        check_status_code(response, code.CREATED)
        # проверяем тело ответа:   {'ok' = True}
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)


    @pytest.mark.parametrize('field', [KEYS.LOGIN, KEYS.PASSWORD])
    @allure.title('Проверяем, что если не передано поле логина или пароля, то запрос возвращает код ошибки 400')
    def test_create_courier_missing_field_error(self, field):
        # получаем данные для нового курьера и собираем тело запроса без логина
        user_data = generate_random_courier_data()
        payload = user_data
        payload.pop(field)
        # отправляем запрос на создание нового курьера
        response = create_courier(payload)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.CREATE_BAD_REQUEST)


    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров и запрос возвращает код ошибки 409')
    def test_create_courier_double_courier_not_created(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что регистрация прошла успешно: код ответа 201, тело ответа {'ok' = True}
        check_status_code(response, code.CREATED)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)
        # делаем повторную попытку зарегистрировать курьера с теми же данными
        response = create_courier(user_data)
        # проверяем что получен код ответа 409
        check_status_code(response, code.CONFLICT)
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_ALREADY_USED_TEXT)


    @allure.title('Проверяем, что нельзя создать двух курьеров с одинаковым логином и запрос возвращает код ошибки 409')
    def test_create_courier_double_login_not_created(self, create_new_courier):
        # создаем нового курьера и получаем его данные
        response, user_data = create_new_courier
        # проверяем что регистрация прошла успешно: код ответа 201, тело ответа {'ok' = True}
        check_status_code(response, code.CREATED)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)
        # делаем повторную попытку зарегистрировать курьера с тем же логином
        # генерируем новые данные для создания курьера
        new_user_data = generate_random_courier_data()
        # сохраняем старый логин
        new_user_data[KEYS.LOGIN] = user_data[KEYS.LOGIN]
        # отправляем запрос на создание нового курьера и получаем ответ в переменную response
        response = create_courier(new_user_data)
        # проверяем что получен код ответа 409
        check_status_code(response, code.CONFLICT)
        # проверяем что в ответе есть message
        # проверяем сообщение об ошибке
        check_message(response, text.LOGIN_ALREADY_USED_TEXT)

