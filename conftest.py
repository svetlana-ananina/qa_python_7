import pytest
import allure

from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_user_id
from helpers.helpers_on_create_courier import generate_random_courier_data, create_courier, register_courier
from helpers.helpers_on_delete_courier import delete_courier_by_user_data


# метод создания нового курьера, возвращает данные нового курьера: логин, пароль и имя
@allure.step('Создаем нового курьера')
@pytest.fixture()
def create_new_courier():
    # собираем тело запроса = данные нового курьера
    user_data = generate_random_courier_data()
    # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
    response = create_courier(user_data)
    # возвращаем ответ API и данные пользователя
    yield response, user_data

    # удаляем данные после окончания теста
    delete_courier_by_user_data(user_data)


# метод создания и регистрации нового курьера, возвращает данные курьера: логин, пароль, имя и id
@allure.step('Создаем и регистрируем нового курьера')
@pytest.fixture()
def register_new_courier():
    # формируем данные нового курьера
    user_data = generate_random_courier_data()
    # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
    response = create_courier(user_data)
    # проверяем что курьер создан: код ответа 201, тело ответа {'ok' = True}
    check_status_code(response, code.CREATED)
    check_key_and_value_in_body(response, KEYS.OK_KEY, True)
    # отправляем запрос на регистрацию курьера
    response = register_courier(user_data)
    # получаем id курьера
    user_id = check_user_id(response)

    # возвращаем ответ API и данные пользователя
    yield user_id, user_data

    # удаляем данные после окончания теста
    delete_courier_by_user_data(user_data)

