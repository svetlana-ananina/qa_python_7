import allure

from data import STATUS_CODES as code

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, \
    check_order_track, check_order_list_in_response, check_order_list_is_not_empty, check_order_is_correct, \
    check_order_id
from helpers.helpers_on_create_order import generate_order_data, get_order_list


class TestGetOrderList:

    @allure.title('Проверяем получение списка заказов')
    def test_get_order_list(self, create_order):
        # создаем новый заказ и проверяем код ответа

        # получаем список заказов
        response = get_order_list()
        # проверяем что получен код ответа 200
        check_status_code(response, code.OK)
        # проверяем, что в ответе получено поле "orders"
        order_list = check_order_list_in_response(response)
        # проверяем, что поле "orders" содержит непустой список и получаем первый заказ из списка
        order = check_order_list_is_not_empty(order_list)
        # проверяем, что в заказе есть поле id
        check_order_id(order)

