import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """
    Класс для работы со страницей оформления заказа самоката
    Содержит методы для заполнения всех полей формы заказа
    """

    @allure.step("Ввести имя заказчика: {name}")
    def fill_name_field(self, name):
        """Заполнить поле с именем пользователя"""
        try:
            self.input_text(OrderPageLocators.NAME_FIELD, name)
        except:
            self.input_text(OrderPageLocators.NAME_FIELD_ALT, name)

    @allure.step("Ввести фамилию заказчика: {last_name}")
    def fill_surname_field(self, last_name):
        """Заполнить поле с фамилией пользователя"""
        try:
            self.input_text(OrderPageLocators.LAST_NAME_FIELD, last_name)
        except:
            self.input_text(OrderPageLocators.LAST_NAME_FIELD_ALT, last_name)

    @allure.step("Ввести адрес доставки: {address}")
    def enter_delivery_address(self, address):
        """Заполнить поле с адресом доставки"""
        self.input_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        """Выбрать станцию метро из выпадающего списка"""
        # Сначала принимаем куки если есть
        try:
            cookie_banner = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.COOKIE_BANNER))
            cookie_button = cookie_banner.find_element(*OrderPageLocators.COOKIE_BUTTON)
            cookie_button.click()
            # Ждем исчезновения баннера через BasePage
            self.wait_for_invisibility(OrderPageLocators.COOKIE_BANNER, timeout=5)
        except:
            pass  # Если баннера нет - продолжаем

        # Кликаем на поле метро
        self.click_element(OrderPageLocators.METRO_FIELD)
        
        # Ждем появления списка станций через BasePage
        self.wait_for_presence(OrderPageLocators.METRO_STATION_1, timeout=5)

        # Прокручиваем и ищем станцию
        if station_name == "Сокольники":
            # Ждем присутствия и прокручиваем через BasePage
            station_element = self.wait_for_presence(OrderPageLocators.METRO_STATION_1)
            self.execute_script("arguments[0].scrollIntoView();", station_element)
            # Ждем кликабельности через BasePage
            self.wait_for_element_clickable(OrderPageLocators.METRO_STATION_1)
            self.click_element(OrderPageLocators.METRO_STATION_1)
        elif station_name == "Лубянка":
            station_element = self.wait_for_presence(OrderPageLocators.METRO_STATION_2)
            self.execute_script("arguments[0].scrollIntoView();", station_element)
            self.wait_for_element_clickable(OrderPageLocators.METRO_STATION_2)
            self.click_element(OrderPageLocators.METRO_STATION_2)

    @allure.step("Ввести номер телефона: {phone}")
    def input_phone_number(self, phone):
        """Заполнить поле с контактным телефоном"""
        self.input_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Перейти к данным аренды")
    def proceed_to_rental_section(self):
        """Нажать кнопку для перехода к следующему шагу"""
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def choose_delivery_date(self, use_date=False):
        """Выбрать дату доставки самоката"""
        self.click_element(OrderPageLocators.DATE_SCOOTER)

        if use_date:
            self.click_element(OrderPageLocators.SELECTED_DATE)
        else:
            self.click_element(OrderPageLocators.SELECTED_DATE_2)

    @allure.step("Выбрать период аренды: {period}")
    def pick_rental_period(self, period=None):
        """Выбрать срок аренды самоката"""
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        
        # Ждем появления выпадающего списка через BasePage
        self.wait_for_presence(OrderPageLocators.RENTAL_PERIOD_1_DAY, timeout=5)

        if period == "двое суток":
            self.click_element(OrderPageLocators.RENTAL_PERIOD_2_DAYS)
        elif period == "трое суток":
            self.click_element(OrderPageLocators.RENTAL_PERIOD_3_DAYS)
        elif period == "четверо суток":
            self.click_element(OrderPageLocators.RENTAL_PERIOD_4_DAYS)
        else:
            # По умолчанию - сутки
            self.click_element(OrderPageLocators.RENTAL_PERIOD_1_DAY)

    @allure.step("Выбрать черный цвет самоката")
    def select_black_color(self):
        """Выбрать черный цвет самоката"""
        self.click_element(OrderPageLocators.BLACK_CHECKBOX)

    @allure.step("Выбрать серый цвет самоката")
    def select_grey_color(self):
        """Выбрать серый цвет самоката"""
        self.click_element(OrderPageLocators.GREY_CHECKBOX)

    @allure.step("Добавить комментарий для курьера: {comment}")
    def add_comment_for_courier(self, comment):
        """Ввести комментарий для курьера (необязательное поле)"""
        if comment:
            self.input_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Подтвердить оформление заказа")
    def finalize_order_creation(self):
        """Нажать кнопку подтверждения заказа"""
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ в диалоговом окне")
    def confirm_order_dialog(self):
        """Подтвердить заказ во всплывающем окне"""
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверить успешное оформление заказа")
    def is_order_successfully_created(self):
        """Проверить отображение сообщения об успешном заказе"""
        return self.is_element_visible(OrderPageLocators.ORDER_NUMBER_TEXT)

    @allure.step("Выполнить полное оформление заказа самоката")
    def complete_scooter_order(self, user_data):
        """
        Полный процесс оформления заказа самоката
        от заполнения формы до подтверждения

        Args:
            user_data: объект с данными пользователя (USER_1 или USER_2)
        """
        # Заполнение персональных данных
        self.fill_name_field(user_data.first_name)
        self.fill_surname_field(user_data.last_name)
        self.enter_delivery_address(user_data.delivery_address)
        self.select_metro_station(user_data.metro_station)
        self.input_phone_number(user_data.phone_number)

        # Переход к данным аренды
        self.proceed_to_rental_section()

        # Заполнение данных аренды - ИСПОЛЬЗУЕМ ДАННЫЕ ИЗ data.py
        self.choose_delivery_date(user_data.delivery_date)
        self.pick_rental_period(user_data.rental_period)

        # Выбираем цвет в зависимости от user_data
        if user_data.scooter_color == 'black':
            self.select_black_color()
        elif user_data.scooter_color == 'grey':
            self.select_grey_color()

        self.add_comment_for_courier(user_data.comment)

        # Завершение оформления
        self.finalize_order_creation()
        self.confirm_order_dialog()
