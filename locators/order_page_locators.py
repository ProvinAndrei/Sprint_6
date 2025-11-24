from selenium.webdriver.common.by import By


class OrderPageLocators:  # Локаторы страницы заказа
    # Локатор поля для ввода имени
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")

    # Локатор поля для ввода фамилии
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Локатор поля для ввода адреса
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Локатор поля для ввода станции метро
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")

    METRO_STATION_1 = (By.XPATH, '//div[text() = "Сокольники"]')
    METRO_STATION_2 = (By.XPATH, '//div[text() = "Лубянка"]')

    # Локатор номера телефона
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Локатор кнопки "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локатор ошибок при заполнении полей
    ERROR_NAME = (By.XPATH, "//div[contains(text(), 'Введите корректное имя')]")
    ERROR_SURNAME = (By.XPATH, "//div[contains(text(), 'Введите корректную фамилию')]")
    ERROR_METRO = (By.XPATH, "//div[contains(text(), 'Выберите станцию')]")
    ERROR_PHONE = (By.XPATH, "//div[contains(text(), 'Введите корректный номер')]")

    # Локатор поля для выбора даты
    DATE_SCOOTER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECTED_DATE = (By.XPATH, '//div[@aria-label="Choose среда, 26-е ноября 2025 г."]')
    SELECTED_DATE_2 = (By.XPATH, '//div[@aria-label="Choose четверг, 27-е ноября 2025 г."]')

    # Локатор поля срок аренды
    RENTAL_PERIOD = (By.CSS_SELECTOR, "div.Dropdown-placeholder")
    RENTAL_PERIOD_1_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_2_DAYS = (By.XPATH, "//div[text()='двое суток']")
    RENTAL_PERIOD_3_DAYS = (By.XPATH, "//div[text()='трое суток']")
    RENTAL_PERIOD_4_DAYS = (By.XPATH, "//div[text()='четверо суток']")
    RENTAL_PERIOD_5_DAYS = (By.XPATH, "//div[text()='пятеро суток']")
    RENTAL_PERIOD_6_DAYS = (By.XPATH, "//div[text()='шестеро суток']")
    RENTAL_PERIOD_7_DAYS = (By.XPATH, "//div[text()='семеро суток']")

    # Локатор чекбокса
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")

    # Локатор поля комментария
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Локатор кнопки "Заказать"
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons__1xGrp')]//button[text()='Заказать']")

    # Локатор модального окна с подтверждением заказа
    ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    # Локатор кнопки "Да" в модальном окне
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal__YZ-d3')]//button[text()='Да']")
    # Локатор кнопки "Нет" в модальном окне
    CANCEL_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal__YZ-d3')]//button[text()='Нет']")
    # Локатор сообщения об успешном заказе
    ORDER_NUMBER_TEXT = (By.CLASS_NAME, "Order_Text__2broi")

    # Локатор кнопки "Посмотреть статус"
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    # Альтернативные локаторы
    NAME_FIELD_ALT = (By.XPATH, "//input[@class='Input_Input__1iN_Z' and @placeholder='* Имя']")
    LAST_NAME_FIELD_ALT = (By.XPATH, "//input[@class='Input_Input__1iN_Z' and @placeholder='* Фамилия']")
    ADDRESS_FIELD_ALT = (By.XPATH, "//input[@class='Input_Input__1iN_Z' and @placeholder='* Адрес: куда привезти заказ']")

    # Новые локаторы для куки
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
