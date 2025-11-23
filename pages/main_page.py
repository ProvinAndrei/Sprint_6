import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
import curl


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = curl.main_site

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        """Открыть главную страницу Яндекс.Самокат"""
        self.open_url(self.url)

    @allure.step("Принять cookies")
    def accept_all_cookies(self):
        """Принять соглашение о cookies"""
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            # Если баннер с куки не появился - продолжаем
            pass

    @allure.step("Нажать кнопку 'Заказать' в хедере")
    def click_header_order_button(self):
        """Кликнуть на кнопку заказа в верхней части страницы"""
        self.click_element(MainPageLocators.ORDER_BUTTON_HEAD)

    @allure.step("Нажать основную кнопку 'Заказать'")
    def click_primary_order_button(self):
        """Кликнуть на основную кнопку заказа внизу страницы"""
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HOME)
        self.click_element(MainPageLocators.ORDER_BUTTON_HOME)

    @allure.step("Нажать на вопрос FAQ №{question_number}")
    def expand_faq_question(self, question_number):
        """Раскрыть вопрос в разделе FAQ по номеру (0-7)"""
        questions = [
            MainPageLocators.FAQ_1,
            MainPageLocators.FAQ_2,
            MainPageLocators.FAQ_3,
            MainPageLocators.FAQ_4,
            MainPageLocators.FAQ_5,
            MainPageLocators.FAQ_6,
            MainPageLocators.FAQ_7,
            MainPageLocators.FAQ_8
        ]
        self.scroll_to_element(questions[question_number])
        self.wait.until(EC.element_to_be_clickable(questions[question_number]))
        self.wait_for_element_clickable(questions[question_number])
        self.click_element(questions[question_number])

    @allure.step("Получить текст ответа FAQ №{answer_number}")
    def get_faq_answer_text(self, answer_number):
        """Получить текст ответа на вопрос FAQ по номеру (0-7)"""
        answers = [
            MainPageLocators.ANSWER_FAQ_1,
            MainPageLocators.ANSWER_FAQ_2,
            MainPageLocators.ANSWER_FAQ_3,
            MainPageLocators.ANSWER_FAQ_4,
            MainPageLocators.ANSWER_FAQ_5,
            MainPageLocators.ANSWER_FAQ_6,
            MainPageLocators.ANSWER_FAQ_7,
            MainPageLocators.ANSWER_FAQ_8
        ]
        return self.get_element_text(answers[answer_number])

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        """Кликнуть на логотип Яндекс.Самокат"""
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекс"""
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверить редирект на Дзен")
    def check_dzen_redirect(self):
        """
        Проверить переход на Дзен после клика на логотип Яндекс
        Возвращает исходную вкладку для последующего переключения
        """
        original_tab = self.switch_to_new_tab()
        dzen_url = self.get_current_url()
        self.switch_to_tab(original_tab)
        return curl.yandex_redirect in dzen_url

    @allure.step("Проверить что на главной странице Самоката")
    def is_on_scooter_main_page(self):
        """Проверить что текущая страница - главная Яндекс.Самокат"""
        return curl.main_site in self.get_current_url()
