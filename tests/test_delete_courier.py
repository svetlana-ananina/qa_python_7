import pytest
import allure

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, \
    print_response
from helpers.helpers_on_delete_courier import delete_courier
from data import RESPONSE_KEYS as KEYS
from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text

from data import _debug as _debug


def print_value(param, user_id):
    pass


@pytest.mark.usefixtures("register_new_courier")
class TestDeleteCourier:

    @allure.title('Проверяем, что можно удалить курьера')
    def test_delete_courier_success(self, register_new_courier):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        if _debug: print_value('user_id', user_id)
        # удаляем созданного курьера
        response = delete_courier(user_id)
        # проверяем код ответа 200, тело ответа {'ok' = True}
        if _debug: print_response(response)
        check_status_code(response, code.OK)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)


    @allure.title('Проверяем, что если отправить запрос без id, запрос вернет код ошибки 400')
    def test_delete_courier_missing_id_error_code(self, register_new_courier):
        # задаем пустой user_id
        user_id = ""
        # направляем запрос на удаление с пустым id
        response = delete_courier(user_id)
        if _debug: print_response(response)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        # check_message(response, text.DELETE_COURIER_BAD_REQUEST)


    @allure.title('Проверяем сообщение об ошибке, если отправить запрос без id')
    def test_delete_courier_missing_id_error_message(self, register_new_courier):
        # задаем пустой user_id
        user_id = ""
        # направляем запрос на удаление с пустым id
        response = delete_courier(user_id)
        if _debug: print_response(response)
        # проверяем что получен код ответа 1xx-4xx
        received_code = response.status_code
        assert received_code < 500, f'Невозможно проверить сообщения об ошибке: получен код {received_code}, ответ сервера "{response.text}"'
        # проверяем сообщение об ошибке
        check_message(response, text.DELETE_COURIER_BAD_REQUEST)


    @allure.title('Проверяем, что если отправить запрос с несуществующим id, запрос вернет код ошибки 400')
    def test_delete_courier_invalid_id_error_code(self, register_new_courier):
        # задаем несуществующий user_id = 0
        user_id = "0"
        # направляем запрос на удаление с id = 0
        response = delete_courier(user_id)
        if _debug: print_response(response)
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        # check_message(response, text.DELETE_COURIER_NOT_FOUND)


    @allure.title('Проверяем сообщение об ошибке, что если отправить запрос с несуществующим id')
    def test_delete_courier_invalid_id_error_message(self, register_new_courier):
        # задаем несуществующий user_id = 0
        user_id = "0"
        # направляем запрос на удаление с id = 0
        response = delete_courier(user_id)
        if _debug: print_response(response)
        # проверяем что получен код ответа 1xx-4xx
        received_code = response.status_code
        assert received_code < 500, f'Невозможно проверить сообщения об ошибке: получен код {received_code}, ответ сервера "{response.text}"'
        # проверяем сообщение об ошибке
        check_message(response, text.DELETE_COURIER_NOT_FOUND)

