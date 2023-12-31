import allure
import requests

from data import URLS as url
from data import ENDPOINTS as ep
from data import ORDER_DATA

from helpers.helpers_on_check_response import _print_info, _print_response


@allure.step('Генерируем данные для заказа')
def generate_order_data():
    order_data = ORDER_DATA.copy()
    # возвращаем словарь
    return order_data


@allure.step('Отправляем API-запрос на создание заказа')
def create_new_order(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.CREATE_ORDER}'
    _print_info(f'\nСоздаем новый заказ: POST url="{request_url}", payload="{payload}"')
    response = requests.post(f'{request_url}', data=payload)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение списка заказов')
def get_order_list():
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    _print_info(f'\nПолучаем список заказов: GET url="{request_url}"')
    response = requests.get(f'{request_url}')
    _print_response(response)
    return response


def get_order(track):
    # трек задан
    param = f'{ep.BY_TRACK}' + str(track)
    response = get_order_by_param(param)
    return response


@allure.step('Отправляем API-запрос на получение заказа по его трек-номеру')
def get_order_by_param(param):
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER}' + str(param)        # url + '/api/v1/orders/track' + 'param'
    _print_info(f'\nОтправляем API-запрос на получение заказа по его трек-номеру: GET url="{request_url}"')
    response = requests.get(f'{request_url}')
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос принять заказ с разными query-параметрами')
def accept_order_by_param(param):
    request_url = f'{url.SERVER_URL}{ep.ACCEPT_ORDER}' + str(param)
    _print_info(f'\nОтправляем запрос принять заказ: PUT url="{request_url}", param="{param}"')
    response = requests.put(f'{request_url}')
    _print_response(response)
    return response


def accept_order(id, courier_id):
    param = str(id) + f'{ep.BY_COURIER_ID}' + str(courier_id)
    return accept_order_by_param(param)


def accept_order_by_order_id(id):
    param = str(id)
    return accept_order_by_param(param)


def accept_order_by_courier_id(courier_id):
    param = f'{ep.BY_COURIER_ID}' + str(courier_id)
    return accept_order_by_param(param)


