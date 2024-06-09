import allure
import requests
import pytest
from urls import Urls
from test_data import Users


class TestLoginCourier:

    @allure.title("Курьер может авторизоваться, передавая все обязательные поля. Успешный запрос возвращает 'id'")
    def test_courier_log_in(self):
        response = requests.post(
            f'{Urls.LOGIN_COURIER_URL}',
            data=Users.positive_user_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title("Ошибка при авторизации под несуществующим пользователем")
    def test_courier_log_negative(self):
        response = requests.post(
            f'{Urls.LOGIN_COURIER_URL}',
            data=Users.negative_user_data)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.text

    @pytest.mark.parametrize("data_without_login_or_password", [Users.without_login_user_data,
                                                                Users.without_password_user_data])
    @allure.title("Ошибка при авторизации если поля 'login' или 'password' пустые")
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        response = requests.post(
            f'{Urls.LOGIN_COURIER_URL}',
            data=data_without_login_or_password)
        assert response.status_code == 400 and "Недостаточно данных для входа" in response.text