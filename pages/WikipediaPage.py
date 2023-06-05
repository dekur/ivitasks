from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class WikipediaPageLocators(object):
    wikipedia_logo = (By.CSS_SELECTOR, '[class="mw-wiki-logo"]')
    ivi_link = (By.XPATH, '//a[contains(@href,"ivi.ru")]')


class WikipediaPage(BasePage):

    def wikipedia_logo(self):
        # проверяем что википедия открылась, судим по иконке википедии
        return self.return_element_if_present(WikipediaPageLocators.wikipedia_logo)

    def ivi_link_element(self):
        # находим все ссылки содержащие ivi.ru
        return self.return_element_if_present(WikipediaPageLocators.ivi_link)