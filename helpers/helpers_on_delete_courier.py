import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep

from helpers.helpers_on_check_response import check_user_id
from helpers.helpers_on_create_courier import register_courier


@allure.step('Отправляем API-запрос на удаление курьера')
def delete_courier(user_id):
    request_url = f'{url.SERVER_URL}{ep.DELETE_COURIER}'+str(user_id)
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    return requests.delete(request_url)


#@allure.step('Получаем данные курьера для удаления')
def delete_courier_by_user_data(user_data):
    # регистрируем курьера/получаем его id
    response = register_courier(user_data)
    # получаем user_id
    user_id = check_user_id(response)
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    return delete_courier(user_id)

