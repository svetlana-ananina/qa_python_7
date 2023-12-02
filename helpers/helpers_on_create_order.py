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
from helpers.helpers_on_check_response import check_status_code, check_key_in_body, check_order_track


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


@allure.step('Отправляем API-запрос на получение списка заказов')
def get_order_list():
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    if _debug:
        print('\nОтправляем запрос на получение списка заказов')
        print(f'request_url="{request_url}"')
    response = requests.get(f'{request_url}')
    if _debug:
        print(f'response={response}, response.text={response.text}')
    return response


@allure.step('Отправляем API-запрос на получение списка заказов для курьера')
def get_order_list_by_courier_id(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    if _debug:
        print('\nОтправляем запрос на получение списка заказов')
        print(f'request_url="{request_url}"')
    response = requests.get(f'{request_url}')
    if _debug:
        print(f'response={response}, response.text={response.text}')
    return response

