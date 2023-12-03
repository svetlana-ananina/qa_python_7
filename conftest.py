import pytest
import allure

from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_user_id, \
    check_order_track, print_response_value
from helpers.helpers_on_create_courier import generate_random_courier_data, create_courier, register_courier
from helpers.helpers_on_create_order import generate_order_data, create_new_order
from helpers.helpers_on_delete_courier import delete_courier_by_user_data

from data import _debug as _debug


# метод создания нового курьера, возвращает данные нового курьера: логин, пароль и имя
@allure.step('Создаем нового курьера')
@pytest.fixture()
def create_new_courier():
    if _debug: print('\nЗапуск фикстуры "create_new_courier()"...')
    # собираем тело запроса = данные нового курьера
    user_data = generate_random_courier_data()
    # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
    response = create_courier(user_data)
    # возвращаем ответ API и данные пользователя
    if _debug: print('\nОкончание работы фикстуры create_new_courier()"...')
    yield response, user_data

    # удаляем данные после окончания теста
    if _debug: print('\nЗапуск teardown фикстуры "create_new_courier()"...')
    delete_courier_by_user_data(user_data)


# метод создания и регистрации нового курьера, возвращает данные курьера: логин, пароль, имя и id
@allure.step('Создаем и регистрируем нового курьера')
@pytest.fixture()
def register_new_courier():
    if _debug: print('\nЗапуск фикстуры "register_new_courier()"...')
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
    # возвращаем id курьера
    if _debug: print('\nОкончание работы фикстуры "register_new_courier()"...')
    yield user_id

    # удаляем данные после окончания теста
    if _debug: print('\nЗапуск teardown фикстуры "register_new_courier()"...')
    delete_courier_by_user_data(user_data)


@allure.title('Создаем новый заказ')
@pytest.fixture()
def create_order():
    if _debug: print('\nЗапуск фикстуры "create_order()"')
    # генерируем данные заказа
    order_data = generate_order_data()
    # создаем новый заказ
    response = create_new_order(order_data)
    # проверяем что получен код ответа 201
    check_status_code(response, code.CREATED)
    # проверяем тело ответа и получаем трек
    track = check_order_track(response)
    if _debug: print_response_value('track', track)
    if _debug: print('\nОкончание фикстуры "create_order()"...')
    return track

