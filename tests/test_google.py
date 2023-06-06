from constants import google, google_ivi_search
from pages.GoogleSearchPage import GoogleSearchPage
from pages.WikipediaPage import WikipediaPage
from selenium.webdriver import Keys


def test_ivi_links_in_pictures(browser):
    browser.get(google)  # открываем главную гугла
    search_page = GoogleSearchPage(browser)  # получаем класс страницы поиска
    search_page.search_input().send_keys("ivi")  # вводим иви в поле поиска
    search_page.search_input().send_keys(Keys.ENTER)  # нажимаем enter
    search_page.go_to_search_type("Картинки")  # открываем поиск по картинкам
    search_page.instruments_button().click()  # открываем инструменты
    search_page.picture_size_selection().click()  # кликаем по выбору размера картинок
    search_page.picture_size_big().click()  # кликаем по большому размеру
    assert search_page.selected_option().get_attribute("aria-label") == "Большой"  # проверяем что выбранная опция и
    # есть опция с большим размером картинок
    assert len(search_page.ivi_links_in_pictures()) >= 3  # проверяем что на странице есть 3 ссылки на сайт ivi.ru


def test_ivi_rating_from_google_search_and_google_play(browser):
    # browser.get(google_play_ivi_page)  # открываем страницу google play
    # rating_from_google_play = browser.find_element(By.CSS_SELECTOR, "[itemprop='starRating'] div").get_text()
    # берем рейтинг
    # для выполнения шагов выше нужен vpn
    rating_from_google_play = "3,5"

    browser.get(google_ivi_search)  # открываем браузер, для экономии времени сразу с поиском иви
    search_page = GoogleSearchPage(browser)  # получаем класс страницы поиска
    max_page = 6  # проверяем первые пять страниц(крайнее правое значение не используется)

    for i in range(2, max_page):  # счет начинается со второй страницы
        link = search_page.google_play_ivi_rating()  # первая проверка будет на первой странице
        if link:  # если элемент найден то берем рейтинг
            rating = link.text
        else:  # если нет то перейдем на следующую страницу
            search_page.go_to_page(i)

    assert rating == "Рейтинг: %s" % rating_from_google_play


def test_wikipedia_has_link_to_ivi(browser):
    browser.get(google_ivi_search)  # открываем браузер, для экономии времени сразу с поиском иви
    search_page = GoogleSearchPage(browser)  # получаем класс страницы поиска
    max_page = 6

    for i in range(2, max_page):  # счет начинается со второй страницы
        link = search_page.check_for_wikipedia_link()  # первая проверка будет на первой странице
        if link:  # если элемент найден то кликаем
            link.click()
            break
        else:  # если нет то перейдем на следующую страницу
            search_page.go_to_page(i)

    wikipedia_page = WikipediaPage(browser)
    wikipedia_page.page_has_loaded()  # время на полную загрузку страницы
    assert wikipedia_page.wikipedia_logo()  # проверяем что попали на википедию
    assert wikipedia_page.ivi_link_element()  # находим ссылку на иви
