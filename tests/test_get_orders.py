import allure
import requests
from urls import Urls


class TestReturnOrderList:
    @allure.title("В теле ответа вернулся список заказов при запросе списка заказов")
    def test_list_order(self):
        response = requests.get(f'{Urls.CREATE_ORDER_URL}')
        assert response.status_code == 200 and "orders" in response.json()
