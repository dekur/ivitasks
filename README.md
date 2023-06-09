# Тестовые задачи от Иви

Сценарий 1: test_ivi_links_in_pictures
```
неавторизованный пользователь заходит в https://www.google.com/
ищет ivi
переходит в картинки
выбирает большие
убеждается, что не менее 3 картинок в выдаче ведут на сайт ivi.ru
```

Cценарий 2: test_ivi_rating_from_google_search_and_google_play
```
неавторизованный пользователь заходит в https://www.google.com/
ищет ivi
на первых 5 страницах находит ссылки на приложение ivi в play.google.com
убеждается, что рейтинг приложения на кратком контенте страницы совпадает с рейтингом при переходе
```

Сценарий 3: test_wikipedia_has_link_to_ivi
```
неавторизованный пользователь заходит в https://www.google.com/
ищет ivi
на первых 5 страницах находит ссылку на статью в wikipedia об ivi
убеждается, что в статье есть ссылка на официальный сайт ivi.ru
```

# Используется:
```
Selenium 4.9.1
```
```
Pytest 7.3.1
```
# Запуск
## Через терминал:
1. Клонировать и открыть проект
```
git clone https://github.com/dekur/ivitasks.git
```
```
cd .\ivitasks\
```
2. Создать и войти в виртуальное окружение
```
pipenv —python 3.10.5
```
```
pipenv shell
```
3. Установить requirements.txt
```
pip install -r .\requirements.txt
```
4. Запустить тесты
```
pytest tests
```
## Через PyCharm:
1. Клонировать и открыть проект
2. Создать виртуальное окружение
3. Установить модули из requirements.txt
4. Убедиться, что pytest выбран как **Default test runner** в **Settings > Tools > Python Integrated Tools**
5. Запустить тесты через любую конфигурацию pytest

# Используемые материалы:
Функция для проверки готовности загрузки страницы
```
https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
```
Структура Page Object
```
https://www.pvsm.ru/python/333802
```
Для реализации второго и третьего тестов понадобились циклы, идеи взял здесь
```
https://www.w3schools.com/python/python_for_loops.asp
```
```
https://favtutor.com/blogs/repeat-n-times-python
```
Идея для функции go_to_page(if elif else)
```
https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html
```
CSS и XPath селекторы
```
https://comaqa.gitbook.io/selenium-webdriver-lectures/selenium-webdriver.-slozhnye-voprosy./lokatory.-css-xpath-jquery.
```
```
https://stackoverflow.com/questions/12323403/how-do-i-find-an-element-that-contains-specific-text-in-selenium-webdriver-pyth
```
XPath селектор по ссылке
```
https://stackoverflow.com/questions/33155454/how-to-find-an-element-by-href-value-using-selenium-python
```
Идея для функции go_to_search_type
```
https://devqa.io/selenium-click-link-by-href/
```
Идея для функции return_element_if_present(try except)
```
https://www.w3schools.com/python/python_try_except.asp
```
