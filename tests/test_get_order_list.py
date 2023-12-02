import allure

from data import STATUS_CODES as code

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, \
    check_order_track, check_field_order_in_order_list_response, check_order_list_is_not_empty, check_order_is_not_empty
from helpers.helpers_on_create_order import generate_order_data, create_order, get_order_list


class TestGetOrderList:

    @allure.title('Проверяем получение списка заказов')
    def test_get_order_list(self):
        # получаем список заказов
        response = get_order_list()
        # проверяем что получен код ответа 200
        check_status_code(response, code.OK)
        # проверяем, что в ответе получено поле "orders"
        order_list = check_field_order_in_order_list_response(response)
        # проверяем, что в поле "orders" содержится список и он содержит хотя бы один заказ
        order = check_order_list_is_not_empty(order_list)
        # проверяем, что 1-й заказ в списке содержит все необходимые поля
        check_order_is_not_empty(order)

