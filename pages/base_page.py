import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        """Перейти на указанный URL"""
        self.driver.get(url)

    @allure.step("Найти и дождаться элемента")
    def find_element(self, locator):
        """Найти элемент с ожиданием видимости"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        """Кликнуть на элемент"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст: '{text}' в поле")
    def input_text(self, locator, text):
        """Ввести текст в поле ввода"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента с ожиданием")
    def get_element_text(self, locator, timeout=15):
        """Получить текст элемента с ожиданием"""
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проскроллить к элементу")
    def scroll_to_element(self, locator):
        """Проскроллить страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        """Проверить видим ли элемент"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        """Переключиться на новую вкладку браузера"""
        original_tab = self.driver.current_window_handle
        self.wait.until(lambda driver: len(driver.window_handles) > 1)

        for handle in self.driver.window_handles:
            if handle != original_tab:
                self.driver.switch_to.window(handle)
                break

        return original_tab

    @allure.step("Переключиться на вкладку")
    def switch_to_tab(self, handle):
        """Переключиться на указанную вкладку"""
        self.driver.switch_to.window(handle)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title

    @allure.step("Закрыть текущую вкладку")
    def close_current_tab(self):
        """Закрыть текущую вкладку браузера"""
        self.driver.close()

    @allure.step("Дождаться URL содержащего: {url_part}")
    def wait_for_url_contains(self, url_part):
        """Дождаться пока URL содержит указанную строку"""
        self.wait.until(EC.url_contains(url_part))

    @allure.step("Ждать пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout=10):
        """Ждать пока элемент станет кликабельным"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
