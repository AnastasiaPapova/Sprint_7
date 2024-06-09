import json
import allure
import pytest
import requests
from test_data import Orders
from urls import Urls


class TestCreateOrder:

    @pytest.mark.parametrize("order_data",
                             [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    @allure.title("Создание заказа, в теле ответа возвращается поле 'track'")
    def test_create_order(self, order_data):
        Orders.order_data.update(order_data)
        order_data = json.dumps(Orders.order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Urls.CREATE_ORDER_URL}', data=order_data, headers=headers)
        assert response.status_code == 201 and "track" in response.text
