import allure

from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS
from data import ORDER_FIELDS as order_fields

from data import _debug as _debug


@allure.step('Проверяем код ответа')
def check_status_code(response, expected_code):
    # проверяем что получен код ответа expected_code
    received_code = response.status_code
    assert received_code == expected_code, f'Неверный код в ответе: ожидался {expected_code}, получен "{received_code}", ответ: "{response.text}"'


@allure.step('Проверяем сообщение в ответе')
def check_message(response, expected_message):
    # проверяем что в ответе есть message
    received_text = response.text
    received_body = response.json()
    assert KEYS.MESSAGE_KEY in received_body, f'В ответе отсутствует ключ "{KEYS.MESSAGE_KEY}", текст: "{received_text}"'
    # проверяем сообщение об ошибке
    received_message = received_body[KEYS.MESSAGE_KEY]
    assert received_message == expected_message, f'Получено неверное сообщение: ожидалось: "{expected_message}", получено: "{received_message}"'


@allure.step('Проверяем наличие ключа в ответе')
def check_key_in_body(response, key):
    # проверяем что в ответе есть ключ key
    received_text = response.text
    assert key in response.json(), f'В ответе отсутствует ключ "{key}", получен ответ: "{received_text}"'
    return response.json()[key]


@allure.step('Проверяем значение ключа в ответе')
def check_key_and_value_in_body(response, key, value):
    # проверяем тело ответа: {'ok' == True}
    received_text = response.text
    received_body = response.json()
    # проверяем наличие ключа в ответе
    assert key in received_body, f'В ответе отсутствует ключ "{key}", получен ответ: "{received_text}"'
    # проверяем значение ключа в ответе
    assert received_body[key] == value, f'Получено неверное значение ключа: ожидалось: "{key}" = "{value}", текст: "{received_text}"'


@allure.step('Получаем id курьера из ответа запроса на регистрацию курьера')
def check_user_id(response):
    # проверяем что получен код ответа 200 и в ответе есть id курьера
    check_status_code(response, code.OK)
    # check_key_in_body(response, KEYS.ID_KEY)
    # return response.json()[KEYS.ID_KEY]
    return check_key_in_body(response, KEYS.ID_KEY)


@allure.step('Получаем трек заказа из ответа запроса на создание заказа')
def check_order_track(response):
    # проверяем что получен код ответа 201 и в ответе есть track - номер заказа (число)
    check_status_code(response, code.CREATED)
    # check_key_in_body(response, KEYS.TRACK)
    # Возвращаем трек (номер) заказа
    # return response.json()[KEYS.TRACK]
    # Возвращаем трек (номер) заказа
    return check_key_in_body(response, KEYS.TRACK)


@allure.step('Проверяем, что в ответе есть ключ "orders"')
def check_order_list_in_response(response):
    # Получаем тело ответа в виде json()
    response_body = response.json()
    # проверяем, что в теле ответа есть поле "orders"
    assert KEYS.ORDERS in response_body, f'Ошибка: в ответе нет поля "{KEYS.ORDERS}"'
    # возвращаем содержимое поля "orders"
    return response_body[KEYS.ORDERS]


@allure.step('Проверяем, что поле "orders" содержит список и он не пустой')
def check_order_list_is_not_empty(order_list):
    assert type(order_list) is list, f'Ошибка: в ответе не получен тип список заказов'
    assert len(order_list) > 0, f'Ошибка: список заказов пуст'
    return order_list[0]


@allure.step('Проверяем, что заказ содержит поле {field}')
def check_field_in_order(order, field):
    if _debug: print(f'Проверяем поле "{field}" в заказе ...')
    assert field in order, f'Ошибка: в заказе отсутствует поле {field}'
    # return True
    return order[field]


@allure.step('Получаем id заказа из ответа запроса на получение заказа по его треку')
def check_order_id(order):
    # проверяем что в заказе есть поле (ключ) ID
    # получаем ID заказа
    return check_field_in_order(order, order_fields.ID)


@allure.step('Проверяем track-номер в заказе')
def check_track_in_order(order):
    # проверяем что в заказе есть поле (ключ) track и получаем его значение
    return check_field_in_order(order, order_fields.TRACK)


@allure.step('Получаем заказ из ответа запроса на получение заказа по его треку')
def check_order_in_response(response):
    # проверяем что получен код ответа 200
    check_status_code(response, code.OK)
    # проверяем, что в теле ответа есть поле (ключ) "order"
    # получаем заказ в ответе
    return check_key_in_body(response, KEYS.ORDER)


# Отладочная печать - вывод в <stdout>
def print_response(response):
    if _debug:
        print(f'response="{response}", response.text="{response.text}"')


def print_response_value(name, value):
    if _debug:
        print(f'{name}="{value}"')

