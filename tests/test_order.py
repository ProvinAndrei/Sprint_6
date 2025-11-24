import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import USER_1, USER_2


class TestScooterOrderFlow:
    """Тестовый класс для проверки процесса заказа самоката"""

    @allure.title("Оформление заказа через верхнюю кнопку - Пользователь_1")
    def test_order_via_header_button_user_1(self, driver):
        """Тестирование заказа через кнопку в хедере с данными USER_1"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открываем главную страницу и переходим через верхнюю кнопку
        main_page.open_main_page()
        main_page.accept_all_cookies()
        main_page.click_header_order_button()

        order_page.complete_scooter_order(USER_1)
        assert order_page.is_order_successfully_created()

    @allure.title("Оформление заказа через основную кнопку - Пользователь_2")
    def test_order_via_main_button_user_2(self, driver):
        """Тестирование заказа через основную кнопку с данными USER_2"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открываем главную страницу и переходим через основную кнопку
        main_page.open_main_page()
        main_page.accept_all_cookies()
        main_page.click_primary_order_button()

        order_page.complete_scooter_order(USER_2)
        assert order_page.is_order_successfully_created()
