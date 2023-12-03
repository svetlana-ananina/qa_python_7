import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import ORDER_DATA

from data import _debug as _debug
from helpers.helpers_on_check_response import print_response


@allure.step('Генерируем данные для заказа')
def generate_order_data():
    order_data = ORDER_DATA.copy()
    # возвращаем словарь
    return order_data


@allure.step('Отправляем API-запрос на создание заказа')
def create_new_order(payload):
    # отправляем запрос на создание заказа и возвращаем ответ
    request_url = f'{url.SERVER_URL}{ep.CREATE_ORDER}'
    if _debug: print(f'\nСоздаем новый заказ: POST url="{request_url}", payload="{payload}"')
    response = requests.post(f'{request_url}', data=payload)
    if _debug: print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение списка заказов')
def get_order_list():
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}'
    if _debug: print(f'\nПолучаем список заказов: GET url="{request_url}"')
    response = requests.get(f'{request_url}')
    if _debug: print_response(response)
    return response


@allure.step('Отправляем API-запрос принять заказ с параметрами: id - номер заказа, courierId - id курьера')
def accept_order(id, courier_id):
    request_url = f'{url.SERVER_URL}{ep.ACCEPT_ORDER}' + str(id) + f'{ep.BY_COURIER_ID}' + str(courier_id)
    if _debug: print(f'\nОтправляем запрос принять заказ: PUT url="{request_url}", id="{id}", courier_id="{courier_id}"')
    response = requests.put(f'{request_url}')
    if _debug: print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение заказа по его треку')
def get_order(track):
    request_url = f'{url.SERVER_URL}{ep.GET_ORDER_LIST}{ep.BY_TRACK}' + str(track)
    if _debug: print(f'\nОтправляем API-запрос на получение заказа по его треку: GET url="{request_url}", track="{track}"')
    response = requests.get(f'{request_url}')
    if _debug: print_response(response)
    return response


