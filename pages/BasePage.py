from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from constants import timeout_for_elem_search
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator, time=timeout_for_elem_search):
        # функция для поиска одного элемента по селектору
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=timeout_for_elem_search):
        # функция для поиска всех элементов по селектору
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def return_element_if_present(self, locator, timeout=timeout_for_elem_search):
        # функция если нужно проверить наличие элемента и вернуть false или сам элемент
        try:
            elem = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return elem

    def page_has_loaded(self):
        # функция для проверки готовности загрузки страницы
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'
