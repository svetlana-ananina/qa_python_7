# qa_python_7
# Тест-сьют для проверки API приложения "Самокат" с помощью Pytest и библиотеки Requests

## Файлы:
- tests/ - папка с файлами тестов:
- tests/test_create_courier.py - тесты эндпойнта создания курьера
- tests/test_login_courier.py  - тесты эндпойнта регистрации курьера
- tests/test_create_order.py   - тесты эндпойнта создания заказа
- tests/test_get_order_list.py - тесты эндпойнта получения списка заказов
- tests/test_delete_courier.py - тесты эндпойнта удаления курьера
- tests/test_get_order.py      - тесты эндпойнта получения заказа по трек-номеру
- tests/test_accept_order.py   - тесты эндпойнта принятия заказа курьером


- helpers/ - папка вспомогательных функций:
- helpers/helpers_on_create_courier.py - функции для создания и регистрации курьера
- helpers/helpers_on_delete_courier.py - функции для удаления курьера
- helpers/helpers_on_create_order.py   - функции для создания заказа и получения списка заказов
- helpers/helpers_on_check_response.py - функции для проверки полученного ответа на запрос к API


- conftest.py - функции для setup и teardown тестов 
- data.py - константы, URL-адреса и данные для тестов


- .gitignore - файл для проекта в Git/GinHub
- requirements.txt - файл с внешними зависимостями
- README.md - файл с описанием проекта (этот файл)


## Для запуска тестов должны быть установлены пакеты:
- pytest,
- requests, 
- allure-pytest и
- allure-python-commons.

## Для генерации отчетов необходимо дополнительно установить:
- фреймворк Allure,
- JDK

## Запуск всех тестов выполняется командой:

    pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

    pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

    allure serve allure_results

Генерация файла внешних зависимостей requirements.txt выполняется командой:

    pip freeze > requirements.txt

Установка зависимостей из файла requirements.txt выполняется командой:

    pip install -r requirements.txt
