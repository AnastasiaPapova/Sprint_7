import allure
import requests
from urls import Urls
from generate_new_users import reg_new_courier
from generate_new_users import reg_new_courier_without_login
from generate_new_users import reg_new_courier_without_password


class TestCreateCourier:
    data = reg_new_courier()

    @allure.title("Создание курьера с передачей всех обязательных полей")
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Urls.CREATE_COURIER_URL}',
            TestCreateCourier.data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title("Нельзя создать двух курьеров с одинаковыми логинами")
    def test_courier_was_created(self):
        response = requests.post(
            f'{Urls.CREATE_COURIER_URL}',
            TestCreateCourier.data)
        assert response.status_code == 409 and "Этот логин уже используется" in response.text

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        response = requests.post(
            f'{Urls.CREATE_COURIER_URL}',
            reg_new_courier_without_login())
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.text

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self):
        response = requests.post(
            f'{Urls.CREATE_COURIER_URL}',
            reg_new_courier_without_password())
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.text
