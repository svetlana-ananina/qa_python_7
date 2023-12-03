import requests
import allure

from data import URLS as url
from data import ENDPOINTS as ep
from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS
from helpers.helpers_on_create_courier import register_courier

from data import _debug as _debug


@allure.step('Отправляем API-запрос на удаление курьера')
def delete_courier(user_id):
    # превращаем полученный user_id в строку
    user_id = str(user_id)
    request_url = f'{url.SERVER_URL}{ep.DELETE_COURIER}'+user_id
    if _debug: print(f'\nНаправляем запрос на удаление курьера user_id="{user_id}": DELETE url="request_url"')
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    return requests.delete(request_url)


# функция для удаления данных после теста в фикстурах
@allure.step('Удаляем курьера после выполнения теста')
def delete_courier_by_user_data(user_data):
    # регистрируем курьера/получаем его id
    response = register_courier(user_data)
    # получаем user_id если такой курьер есть
    user_id = get_user_id_if_exist(response)
    # отправляем запрос на регистрацию курьера
    if user_id:
        delete_courier(user_id)


@allure.step('Получаем id курьера')
def get_user_id_if_exist(response):
    # проверяем что получен код ответа 200 и в ответе есть id курьера
    if response.status_code == code.OK and KEYS.ID_KEY in response.json():
        return response.json()[KEYS.ID_KEY]
    else:
        return None


