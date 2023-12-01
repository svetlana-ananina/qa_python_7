import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from data import _debug as _debug


@allure.step('Проверяем код ответа')
def check_status_code(response, expected_code):
    # проверяем что получен код ответа expected_code
    received_code = response.status_code
    assert received_code == expected_code, f'Неверный код в ответе: ожидался {expected_code}, получен код "{received_code}", текст: "{response.text}"'


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

