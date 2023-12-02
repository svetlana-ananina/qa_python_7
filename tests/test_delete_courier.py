import pytest
import allure

from helpers.helpers_on_check_response import check_status_code, check_key_and_value_in_body
from helpers.helpers_on_delete_courier import delete_courier
from data import STATUS_CODES as code
from data import RESPONSE_KEYS as KEYS

from data import _debug as _debug


@pytest.mark.usefixtures("register_new_courier")
class TestDeleteCourier:

    @allure.title('Проверяем, что можно удалить курьера')
    def test_delete_courier_success(self, register_new_courier):
        # создаем и регистрируем нового курьера и получаем его данные
        user_id, user_data = register_new_courier
        if _debug:
            print(f'\nНовый курьер: user_id="{user_id}", payload="{user_data}"')
        # удаляем созданного курьера
        response = delete_courier(user_id)
        # проверяем код ответа 200, тело ответа {'ok' = True}
        if _debug:
            print(f'\nresponse="{response}", response.text="{response.text}"')
        check_status_code(response, code.OK)
        check_key_and_value_in_body(response, KEYS.OK_KEY, True)



