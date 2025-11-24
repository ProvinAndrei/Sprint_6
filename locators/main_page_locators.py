from selenium.webdriver.common.by import By


class MainPageLocators:  # Локаторы главной страницы
    # Кнопка "Заказать" в шапке сайта
    ORDER_BUTTON_HEAD = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")

    # Кнопка "Заказать" по середине страницы
    ORDER_BUTTON_HOME = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Текст "Вопросы о важном"
    QUESTION_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Логотип в шапке сайта
    LOGO_YANDEX = (By.XPATH, "//a[contains(@href, 'yandex.ru')]")
    LOGO_SCOOTER = (By.XPATH, "//a[.//img[@alt='Scooter']]")

    # Вопросы о важном
    FAQ_1 = (By.CSS_SELECTOR, "[id*='accordion__heading-0']")
    FAQ_2 = (By.CSS_SELECTOR, "[id*='accordion__heading-1']")
    FAQ_3 = (By.CSS_SELECTOR, "[id*='accordion__heading-2']")
    FAQ_4 = (By.CSS_SELECTOR, "[id*='accordion__heading-3']")
    FAQ_5 = (By.CSS_SELECTOR, "[id*='accordion__heading-4']")
    FAQ_6 = (By.CSS_SELECTOR, "[id*='accordion__heading-5']")
    FAQ_7 = (By.CSS_SELECTOR, "[id*='accordion__heading-6']")
    FAQ_8 = (By.CSS_SELECTOR, "[id*='accordion__heading-7']")

    # Ответы на вопросы
    ANSWER_FAQ_1 = (By.XPATH, "//*[@id='accordion__panel-0']//p")
    ANSWER_FAQ_2 = (By.XPATH, "//*[@id='accordion__panel-1']//p")
    ANSWER_FAQ_3 = (By.XPATH, "//*[@id='accordion__panel-2']//p")
    ANSWER_FAQ_4 = (By.XPATH, "//*[@id='accordion__panel-3']//p")
    ANSWER_FAQ_5 = (By.XPATH, "//*[@id='accordion__panel-4']//p")
    ANSWER_FAQ_6 = (By.XPATH, "//*[@id='accordion__panel-5']//p")
    ANSWER_FAQ_7 = (By.XPATH, "//*[@id='accordion__panel-6']//p")
    ANSWER_FAQ_8 = (By.XPATH, "//*[@id='accordion__panel-7']//p")

    # Кнопка куки
    COOKIE_BUTTON = (By.CSS_SELECTOR, "[id*='rcc-confirm-button']")
