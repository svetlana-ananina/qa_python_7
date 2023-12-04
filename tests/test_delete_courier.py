import pytest
import allure

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, _print_response
from helpers.helpers_on_delete_courier import delete_courier
from data import RESPONSE_KEYS as KEYS
from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text


@pytest.mark.usefixtures("register_new_courier")
class TestDeleteCourier:

    @allure.title('Проверяем, что можно удалить курьера')
    def test_delete_courier_success(self, register_new_courier):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        # направляем запрос на удаление курьера
        response = delete_courier(user_id)
        # проверяем код ответа 200, тело ответа {'ok' = True}
        check_status_code(response, code.OK)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)


    @allure.title('Если отправить запрос на удаление курьера без id, запрос вернет код ошибки 400')
    def test_delete_courier_missing_id_error_code(self, register_new_courier):
        # задаем пустой user_id
        user_id = ""
        # направляем запрос на удаление курьера с пустым id
        response = delete_courier(user_id)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        # check_message(response, text.DELETE_COURIER_BAD_REQUEST)


    @allure.title('Если отправить запрос на удаление курьера без id, запрос вернет правильное сообщение об ошибке')
    def test_delete_courier_missing_id_error_message(self, register_new_courier):
        # задаем пустой user_id
        user_id = ""
        # направляем запрос на удаление курьера с пустым id
        response = delete_courier(user_id)
        _print_response(response)
        # проверяем что получен код ответа 1xx-4xx
        received_code = response.status_code
        assert received_code < 500, f'Невозможно проверить сообщения об ошибке: получен код {received_code}, ответ сервера "{response.text}"'
        # проверяем сообщение об ошибке
        check_message(response, text.DELETE_COURIER_BAD_REQUEST)


    @allure.title('Если отправить запрос на удаление курьера с несуществующим id, запрос вернет код ошибки 400')
    def test_delete_courier_invalid_id_error_code(self, register_new_courier):
        # задаем несуществующий user_id = 0
        user_id = "0"
        # направляем запрос на удаление курьера с id = 0
        response = delete_courier(user_id)
        _print_response(response)
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        # check_message(response, text.DELETE_COURIER_NOT_FOUND)


    @allure.title('Если отправить запрос на удаление курьера с несуществующим id, запрос вернет правильное сообщение об ошибке')
    def test_delete_courier_invalid_id_error_message(self, register_new_courier):
        # задаем несуществующий user_id = 0
        user_id = "0"
        # направляем запрос на удаление курьера с id = 0
        response = delete_courier(user_id)
        _print_response(response)
        # проверяем что получен код ответа 1xx-4xx
        received_code = response.status_code
        assert received_code < 500, f'Невозможно проверить сообщения об ошибке: получен код {received_code}, ответ сервера "{response.text}"'
        # проверяем сообщение об ошибке
        check_message(response, text.DELETE_COURIER_NOT_FOUND)

