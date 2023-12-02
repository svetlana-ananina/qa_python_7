import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import ORDER_DATA


@allure.step('Генерируем данные для заказа')
def generate_order_data():
    order_data = ORDER_DATA.copy()
    # возвращаем словарь
    return order_data


@allure.step('Отправляем API-запрос на создание заказа')
def create_order(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.CREATE_ORDER}'
    response = requests.post(f'{request_url}', data=payload)
    return response


@allure.step('Отправляем API-запрос на получение списка заказов')
def get_order_list():
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    response = requests.get(f'{request_url}')
    return response


@allure.step('Отправляем API-запрос на получение списка заказов для курьера')
def get_order_list_by_courier_id(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    response = requests.get(f'{request_url}')
    return response

