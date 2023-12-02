import pytest
import allure

from data import STATUS_CODES as code
from data import ORDER_FIELDS as order_field

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, check_order_track
from helpers.helpers_on_create_order import generate_order_data, create_order


class TestCreateOrder:

    @allure.title('Проверяем, что можно создать заказ')
    def test_create_order(self):
        # генерируем данные заказа
        order_data = generate_order_data()
        # создаем новый заказ
        response = create_order(order_data)
        # проверяем что получен код ответа 201
        check_status_code(response, code.CREATED)
        # проверяем тело ответа и получаем трек
        track = check_order_track(response)


    @pytest.mark.parametrize('color', [
        [order_field.COLOR_BLACK],
        [order_field.COLOR_GREY],
        [order_field.COLOR_BLACK, order_field.COLOR_GREY],
        []                  ])
    @allure.title('Проверяем, что можно создать заказ с указанием любого цвета')
    def test_create_order_with_color(self, color):
        # генерируем данные заказа
        order_data = generate_order_data()
        order_data[order_field.COLOR] = color
        # создаем новый заказ
        response = create_order(order_data)
        # проверяем что получен код ответа 201
        check_status_code(response, code.CREATED)
        # проверяем тело ответа и получаем трек
        track = check_order_track(response)

