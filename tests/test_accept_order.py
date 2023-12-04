import allure

from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message
from helpers.helpers_on_create_order import  accept_order, accept_order_by_order_id, accept_order_by_courier_id


class TestAcceptOrder:

    @allure.title('Проверяем API-запрос "Принять заказ"')
    def test_accept_order_success(self, register_new_courier, create_order_and_get_order_id):
        # создаем и регистрируем нового курьера и получаем его данные
        courier_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем ID заказа
        order_id = create_order_and_get_order_id
        # направляем запрос принять заказ
        response = accept_order(order_id, courier_id)
        # проверяем что получен код ответа 200
        check_status_code(response, code.OK)
        # проверяем тело ответа:   {'ok' = True}
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)


    # @pytest.mark.parametrize('courier_id', ['', '0'])
    @allure.title('Проверяем API-запрос "Принять заказ": если не передать id заказа, запрос вернёт ошибку')
    def test_accept_order_missing_order_id_error(self, register_new_courier, create_order_and_get_order_id):
        # создаем и регистрируем нового курьера и получаем его данные
        courier_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем ID заказа
        # id заказа не передается в запросе
        order_id = create_order_and_get_order_id
        # направляем запрос принять заказ без id заказа
        response = accept_order_by_courier_id(courier_id)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.ACCEPT_BAD_REQUEST)


    @allure.title('Проверяем API-запрос "Принять заказ": если не передать id курьера, запрос вернёт ошибку')
    def test_accept_order_missing_courier_id_error(self, register_new_courier, create_order_and_get_order_id):
        # создаем и регистрируем нового курьера и получаем его данные
        courier_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем ID заказа
        order_id = create_order_and_get_order_id
        # направляем запрос принять заказ без id курьера
        response = accept_order_by_order_id(order_id)
        # проверяем что получен код ответа 400
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.ACCEPT_BAD_REQUEST)


    @allure.title('Проверяем API-запрос "Принять заказ": если передать несуществующий id заказа, запрос вернёт ошибку')
    def test_accept_order_invalid_order_id_error(self, register_new_courier, create_order_and_get_order_id):
        # создаем и регистрируем нового курьера и получаем его данные
        courier_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем ID заказа
        order_id = create_order_and_get_order_id
        order_id = "0"
        # направляем запрос принять заказ с несуществующим id
        response = accept_order(order_id, courier_id)
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        check_message(response, text.ACCEPT_ORDER_ID_NOT_FOUND)


    @allure.title('Проверяем API-запрос "Принять заказ": если передать несуществующий id курьера, запрос вернёт ошибку')
    def test_accept_order_invalid_courier_id_error(self, register_new_courier, create_order_and_get_order_id):
        # создаем и регистрируем нового курьера и получаем его данные
        courier_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем ID заказа
        order_id = create_order_and_get_order_id
        courier_id = "0"
        # направляем запрос принять заказ с несуществующим id курьера
        response = accept_order(order_id, courier_id)
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        check_message(response, text.ACCEPT_COURIER_ID_NOT_FOUND)



