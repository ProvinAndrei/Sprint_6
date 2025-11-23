import allure
from pages.order_page import OrderPage
from data import USER_1, USER_2
import time
import curl


class TestScooterOrderFlow:
    """Тестовый класс для проверки процесса заказа самоката"""

    @allure.title("Оформление заказа через верхнюю кнопку - Пользователь_1")
    def test_order_via_header_button_user_1(self, driver):
        """Тестирование заказа через кнопку в хедере с данными USER_1"""
        order_page = OrderPage(driver)

        # ПЕРЕХОДИМ НАПРЯМУЮ НА СТРАНИЦУ ЗАКАЗА
        driver.get(curl.order_page)
        time.sleep(3)

        order_page.complete_scooter_order(USER_1)
        assert order_page.is_order_successfully_created()

    @allure.title("Оформление заказа через основную кнопку - Пользователь_2")
    def test_order_via_main_button_user_2(self, driver):
        """Тестирование заказа через основную кнопку с данными USER_2"""
        order_page = OrderPage(driver)

        # ПЕРЕХОДИМ НАПРЯМУЮ НА СТРАНИЦУ ЗАКАЗА
        driver.get(curl.order_page)
        time.sleep(3)

        order_page.complete_scooter_order(USER_2)
        assert order_page.is_order_successfully_created()
