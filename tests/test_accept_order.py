import allure

from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text
from data import RESPONSE_KEYS as KEYS

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body, check_message, \
    check_order_track, check_order_list_in_response, check_order_list_is_not_empty, check_order_is_correct, \
    check_order_id, check_order_in_response
from helpers.helpers_on_create_order import generate_order_data, get_order_list, accept_order, get_order


class TestAcceptOrder:

    @allure.title('Проверяем получение списка заказов')
    def test_accept_order_success(self, register_new_courier, create_order):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем номер заказа
        track = create_order
        # получаем заказ по его треку
        response = get_order(track)
        # проверяем ответ и получаем заказ из ответа
        order = check_order_in_response(response)
        # получаем ID заказа
        order_id = check_order_id(order)

        # направляем запрос принять заказ
        response = accept_order(order_id, user_id)
        # проверяем что получен код ответа 200
        check_status_code(response, code.OK)
        # проверяем тело ответа:   {'ok' = True}
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)

