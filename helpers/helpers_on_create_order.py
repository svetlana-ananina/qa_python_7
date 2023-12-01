import random
import string

import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
#from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS
from data import ORDER_FIELDS
from data import ORDER_DATA


from data import _debug as _debug


@allure.step('Генерируем данные для заказа')
def generate_order_data():
    order_data = ORDER_DATA.copy()
    # возвращаем словарь
    return order_data


@allure.step('Отправляем API-запрос на создание заказа')
def create_order(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.CREATE_ORDER}'
    if _debug:
        print('\nОтправляем запрос на создание заказа')
        print(f'request_url="{request_url}", \npayload={payload}')
    response = requests.post(f'{request_url}', data=payload)
    if _debug:
        print(f'response={response}, response.text={response.text}')
    return response


