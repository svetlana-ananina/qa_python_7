import allure

from data import STATUS_CODES as code
from data import RESPONSE_MESSAGES as text

from helpers.helpers_on_check_response import check_status_code, check_message, check_order_in_response, check_track_in_order
from helpers.helpers_on_create_order import get_order, get_order_by_param


class TestGetOrder:

    @allure.title('Проверяем получение заказа по его трек-номеру')
    def test_get_order_success(self, register_new_courier, create_order):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем номер заказа
        track = create_order
        # направляем запрос получить заказ по его треку (номеру)
        response = get_order(track)
        # проверяем ответ и получаем заказ из ответа
        order = check_order_in_response(response)
        # проверяем, что заказ содержит все необходимые поля
        # check_order_is_correct(order)
        track_in_order = check_track_in_order(order)
        assert track_in_order == track


    @allure.title('Проверяем получение заказа по его трек-номеру: запрос без номера заказа возвращает ошибку')
    def test_get_order_missing_track(self, register_new_courier, create_order):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем номер заказа
        track = create_order
        # направляем запрос получить заказ по его треку (номеру) без номера
        response = get_order_by_param("")
        # проверяем что получен код ответа 404
        check_status_code(response, code.BAD_REQUEST)
        # проверяем сообщение об ошибке
        check_message(response, text.GET_ORDER_BAD_REQUEST)


    @allure.title('Проверяем получение заказа по его трек-номеру: запрос с несуществующим номером заказа возвращает ошибку')
    def test_get_order_invalid_track(self, register_new_courier, create_order):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id = register_new_courier
        # создаем новый заказ, проверяем код ответа и получаем номер заказа
        track = create_order
        # направляем запрос получить заказ по его треку (номеру) с несуществующим номером трека "0"
        response = get_order_by_param("0")
        # проверяем что получен код ответа 404
        check_status_code(response, code.NOT_FOUND)
        # проверяем сообщение об ошибке
        check_message(response, text.GET_ORDER_NOT_FOUND)


