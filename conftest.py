import pytest
import allure

from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_user_id, check_order_track
from helpers.helpers_on_check_response import check_order_in_response, check_order_id, _print_response_value, _print_info
from helpers.helpers_on_create_courier import generate_random_courier_data, create_courier, register_courier
from helpers.helpers_on_create_order import generate_order_data, create_new_order, get_order
from helpers.helpers_on_delete_courier import delete_courier_by_user_data


# метод создания нового курьера, возвращает данные нового курьера: логин, пароль и имя
@allure.title('Создаем нового курьера')
@pytest.fixture()
def create_new_courier():
    _print_info('\nЗапуск фикстуры "create_new_courier()"...')
    # собираем тело запроса = данные нового курьера
    user_data = generate_random_courier_data()
    # отправляем запрос на создание нового курьера и сохраняем ответ в переменную response
    response = create_courier(user_data)
    # проверяем что получен код ответа 201
    check_status_code(response, code.CREATED)
    # проверяем тело ответа:   {'ok' = True}
    check_key_and_value_in_body(response, KEYS.OK_KEY, True)
    # возвращаем ответ API и данные пользователя
    _print_info('\nОкончание работы фикстуры create_new_courier()"...')
    # yield response, user_data
    yield user_data

    # удаляем данные после окончания теста
    _print_info('\nЗапуск teardown фикстуры "create_new_courier()"...')
    delete_courier_by_user_data(user_data)


# метод создания и регистрации нового курьера, возвращает данные курьера: логин, пароль, имя и id
@allure.title('Создаем и регистрируем нового курьера')
@pytest.fixture()
def register_new_courier(create_new_courier):
    _print_info('\nЗапуск фикстуры "register_new_courier()"...')
    # создаем нового курьера
    user_data = create_new_courier
    # отправляем запрос на регистрацию курьера
    response = register_courier(user_data)
    # получаем id курьера
    user_id = check_user_id(response)
    # возвращаем id курьера
    _print_response_value('user_id', user_id)
    _print_info('\nОкончание работы фикстуры "register_new_courier()"...')
    yield user_id


@allure.title('Создаем новый заказ')
@pytest.fixture()
def create_order():
    _print_info('\nЗапуск фикстуры "create_order()"')
    # генерируем данные заказа
    order_data = generate_order_data()
    # создаем новый заказ
    response = create_new_order(order_data)
    # проверяем что получен код ответа 201
    check_status_code(response, code.CREATED)
    # проверяем тело ответа и получаем трек
    track = check_order_track(response)
    _print_response_value('track', track)
    _print_info('\nОкончание фикстуры "create_order()"...')
    return track


@allure.title('Создаем новый заказ и получаем его id')
@pytest.fixture()
def create_order_and_get_order_id(create_order):
    _print_info('\nЗапуск фикстуры "create_order_and_get_order_id()"')
    track = create_order
    # получаем заказ по его треку
    response = get_order(track)
    # проверяем ответ и получаем заказ из ответа
    order = check_order_in_response(response)
    # получаем ID заказа
    order_id = check_order_id(order)
    _print_response_value('order_id', order_id)
    _print_info('\nОкончание фикстуры "create_order_and_get_order_id()"...')
    return order_id

