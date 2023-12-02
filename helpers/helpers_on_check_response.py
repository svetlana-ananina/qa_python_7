import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS
from data import ORDER_FIELDS as order_fields


from data import _debug as _debug


@allure.step('Проверяем код ответа')
def check_status_code(response, expected_code):
    # проверяем что получен код ответа expected_code
    received_code = response.status_code
    assert received_code == expected_code, f'Неверный код в ответе: ожидался {expected_code}, получен "{received_code}", ответ: "{response.text}"'


@allure.step('Проверяем наличие ключа в ответе')
def check_key_in_body(response, key):
    # проверяем что в ответе есть ключ key
    received_text = response.text
    received_body = response.json()
    assert key in received_body, f'В ответе отсутствует ключ "{key}", получен ответ: "{received_text}"'


@allure.step('Проверяем значение ключа в ответе')
def check_key_and_value_in_body(response, key, value):
    # проверяем тело ответа: {'ok' == True}
    received_text = response.text
    received_body = response.json()
    # проверяем наличие ключа в ответе
    assert key in received_body, f'В ответе отсутствует ключ "{key}", получен ответ: "{received_text}"'
    # проверяем значение ключа в ответе
    assert received_body[key] == value, f'Получено неверное значение ключа: ожидалось: "{key}" = "{value}", текст: "{received_text}"'


@allure.step('Проверяем сообщение в ответе')
def check_message(response, expected_message):
    # проверяем что в ответе есть message
    received_text = response.text
    received_body = response.json()
    assert KEYS.MESSAGE_KEY in received_body, f'В ответе отсутствует ключ "{KEYS.MESSAGE_KEY}", текст: "{received_text}"'
    # проверяем сообщение об ошибке
    received_message = received_body[KEYS.MESSAGE_KEY]
    assert received_message == expected_message, f'Получено неверное сообщение: ожидалось: "{expected_message}", получено: "{received_message}"'


@allure.step('Получаем id курьера из ответа запроса на регистрацию курьера')
def check_user_id(response):
    # проверяем что получен код ответа 200 и в ответе есть id курьера
    check_status_code(response, code.OK)
    check_key_in_body(response, KEYS.ID_KEY)
    return response.json()[KEYS.ID_KEY]


@allure.step('Получаем трек заказа из ответа запроса на создание заказа')
def check_order_track(response):
    # проверяем что получен код ответа 201 и в ответе есть track - номер заказа (число)
    check_status_code(response, code.CREATED)
    check_key_in_body(response, KEYS.TRACK)
    return response.json()[KEYS.TRACK]


@allure.step('Проверяем, что в ответе на запрос списка заказов есть ключ "orders"')
def check_field_order_in_order_list_response(response):
    if _debug:
        print(f'response = "{response}"')
        print(f'response.text = "{response.text}"')
    # Получаем тело ответа в виде json()
    response_body = response.json()
    if _debug:
        print(f'response_body = {response_body}')
        print(f'type(response_body[KEYS.ORDERS]) = {type(response_body[KEYS.ORDERS])}')
    # проверяем, что в теле ответа есть поле "orders"
    assert KEYS.ORDERS in response_body
    # возвращаем содержимое поля "orders"
    return response_body[KEYS.ORDERS]

@allure.step('Проверяем, что поле "orders" содержит список и он не пустой')
def check_order_list_is_not_empty(order_list):
    assert type(order_list) is list
    assert len(order_list) >= 0
    if _debug:
        print(f'order_list[0] = {order_list[0]}')
    return order_list[0]


@allure.step('Проверяем, что заказ содержит все необходимые поля')
def check_order_is_not_empty(order):
    check_field_in_order(order, order_fields.ID)
    check_field_in_order(order, order_fields.COURIER_ID)
    check_field_in_order(order, order_fields.FIRST_NAME)
    check_field_in_order(order, order_fields.LAST_NAME)
    check_field_in_order(order, order_fields.ADDRESS)
    check_field_in_order(order, order_fields.METRO_STATION)
    check_field_in_order(order, order_fields.PHONE)
    check_field_in_order(order, order_fields.RENT_TIME)
    check_field_in_order(order, order_fields.DELIVERY_DATE)
    check_field_in_order(order, order_fields.TRACK)
    check_field_in_order(order, order_fields.COMMENT)
    check_field_in_order(order, order_fields.CREATED_AT)
    check_field_in_order(order, order_fields.UPDATED_AT)
    check_field_in_order(order, order_fields.STATUS)
    return True


def check_field_in_order(order, field):
    if _debug:
        print(f'field "{field}" in order: {field in order}')
    assert field in order
    return True


