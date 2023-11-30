import random
import string

import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from data import _debug as _debug
from helpers.helpers_on_check_response import check_user_id
from helpers.helpers_on_create_courier import register_courier


@allure.step('Отправляем запрос на удаление курьера с id={user_id}')
def delete_courier(user_id):
    request_url = f'{url.SERVER_URL}{ep.DELETE_COURIER}'+str(user_id)
    if _debug:
        print(f'\nОтправляем запрос на удаление курьера: request_url="{request_url}"')
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    return requests.delete(request_url)


@allure.step('Удаляем курьера без id')
def delete_courier_by_user_data(user_data):
    # регистрируем курьера/получаем его id
    response = register_courier(user_data)
    # получаем user_id
    user_id = check_user_id(response)
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    return delete_courier(user_id)
