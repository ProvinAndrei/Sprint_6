import pytest
import allure
from pages.main_page import MainPage
from data import FAQ


class TestFAQ:
    @allure.title('Проверка раздела "Вопросы о важном" - вопрос {question_index}')
    @allure.description('При нажатии на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_questions(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_all_cookies()
        main_page.expand_faq_question(question_index)
        answer = main_page.get_faq_answer_text(question_index)
        assert FAQ.QUESTION_DATA[question_index] == answer
