import allure
from pages.main_page import MainPage


class TestLogos:
    """Тесты на логотипы"""

    @allure.title("Проверка логотипа Самоката")
    def test_scooter_logo_redirect(self, driver):
        """Проверяем что логотип Самоката ведет на главную страницу"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_all_cookies()

        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()

        # Проверяем что остались на главной странице Самоката
        assert main_page.is_on_scooter_main_page()

    @allure.title("Проверка логотипа Яндекс")
    def test_yandex_logo_redirect(self, driver):
        """Проверяем что логотип Яндекс открывает Дзен в новой вкладке"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_all_cookies()

        # Кликаем на логотип Яндекс
        main_page.click_yandex_logo()
        # Сохраняем исходную вкладку через Page Object
        original_tab = main_page.switch_to_new_tab()

        # Ждем загрузки Дзена через Page Object
        main_page.wait_for_url_contains("dzen.ru")
        current_url = main_page.get_current_url()

        # Закрываем вкладку и возвращаемся через Page Object
        main_page.close_current_tab()
        main_page.switch_to_tab(original_tab)

        # Проверяем что мы были на Дзене
        assert "dzen.ru" in current_url
