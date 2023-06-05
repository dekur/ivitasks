from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GoogleSearchPageLocators(object):
    search_input_field = (By.CSS_SELECTOR, '[type="search"]')
    search_submit_button = (By.CSS_SELECTOR, '[value="Поиск в Google"]')
    instruments_button = (By.XPATH, './/*[contains(@role, "button") and text() = "Инструменты"]/..')
    picture_size_selection = (By.XPATH, "//*[contains(text(), 'Размер')]")
    picture_size_big = (By.CSS_SELECTOR, '[aria-label="Большой"]')
    selected_option = (By.CSS_SELECTOR, '[data-selected="1"]')
    ivi_links_in_pictures = (By.XPATH, '//a[contains(@href,"https://www.ivi.ru")]')
    navigation_menu_search_types = (By.CSS_SELECTOR, '[id="top_nav"] [role="navigation"] a')
    navigation_menu_bottom_pages = (By.CSS_SELECTOR, '[id="botstuff"] [role="navigation"]')
    wikipedia_link_to_ivi = (By.XPATH, '//*[contains(@id, "search")]/following::h3[contains(text(), "Википедия")]')
    google_play_ivi_rating = (By.XPATH, "//div[@class='MjjYud'][.//*[contains(text(), 'Иви: сериалы, фильмы, мультики "
                                        "- Apps on Google Play')]]//*[contains(text(), 'Рейтинг')]")
    google_play_preview_rating = (By.CSS_SELECTOR, '[class="MjjYud"]')
    google_page_2 = (By.CSS_SELECTOR, '[id="botstuff"] [role="navigation"] [aria-label="Page 2"]')
    google_page_3 = (By.CSS_SELECTOR, '[id="botstuff"] [role="navigation"] [aria-label="Page 3"]')
    google_page_4 = (By.CSS_SELECTOR, '[id="botstuff"] [role="navigation"] [aria-label="Page 4"]')
    google_page_5 = (By.CSS_SELECTOR, '[id="botstuff"] [role="navigation"] [aria-label="Page 5"]')
    next_button = (By.CSS_SELECTOR, '//*[contains(@role, "heading")]/following::span[contains(text(), "Следующая")]')


class GoogleSearchPage(BasePage):

    def search_input(self):
        return self.find_element(GoogleSearchPageLocators.search_input_field)

    def submit_button(self):
        return self.find_element(GoogleSearchPageLocators.search_submit_button)

    def instruments_button(self):
        return self.find_element(GoogleSearchPageLocators.instruments_button)

    def picture_size_selection(self):
        return self.find_element(GoogleSearchPageLocators.picture_size_selection)

    def picture_size_big(self):
        return self.find_element(GoogleSearchPageLocators.picture_size_big)

    def selected_option(self):
        return self.find_element(GoogleSearchPageLocators.selected_option)

    def ivi_links_in_pictures(self):
        return self.find_elements(GoogleSearchPageLocators.ivi_links_in_pictures)
        # находим элементы с ссылкой на иви

    def google_play_ivi_rating(self):
        # находим элементы с ссылкой на гугл плей
        return self.find_element(GoogleSearchPageLocators.google_play_ivi_rating)

    def check_for_wikipedia_link(self):
        # находим элементы с ссылкой на википедию
        return self.return_element_if_present(GoogleSearchPageLocators.wikipedia_link_to_ivi)

    def go_to_page(self, expected_page_num: int):
        if expected_page_num == 2:
            self.find_element(GoogleSearchPageLocators.google_page_2).click()
        elif expected_page_num == 3:
            self.find_element(GoogleSearchPageLocators.google_page_3).click()
        elif expected_page_num == 4:
            self.find_element(GoogleSearchPageLocators.google_page_4).click()
        elif expected_page_num == 5:
            self.find_element(GoogleSearchPageLocators.google_page_5).click()
        else:
            self.find_element(GoogleSearchPageLocators.next_button).click()

    def go_to_search_page(self, expected_page_num: int):
        # берем селектор для цифр страниц в нижнем меню
        base_tuple = GoogleSearchPageLocators.navigation_menu_bottom_pages
        # берем текст из селектора
        selector = base_tuple[1]
        # добавляем в текст строчку с нужной страницей
        selector_with_page_num = selector + ' [aria-label="Page %s"]' % expected_page_num
        # собираем заново селектор с новой строчкой
        updated_tuple = (base_tuple[0], selector_with_page_num)
        # находим элемент и кликаем
        page_button = self.find_element(updated_tuple)
        page_button.click()

    def go_to_search_type(self, expected_search_type: str):
        # собираем все типы поиска
        top_menu_search_types = self.find_elements(GoogleSearchPageLocators.navigation_menu_search_types)
        # цикл по всем типам поиска
        for search_type in top_menu_search_types:
            # если текст соответствует типу поиска то кликаем
            if search_type.get_attribute("text") == expected_search_type:
                search_type.click()
                return
