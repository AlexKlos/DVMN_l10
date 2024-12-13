# Clicks Counter
Скрипт для создания коротких ссылок и подсчёта кликов по ним с помощью API vk.cc.

## Установка:
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/AlexKlos/DVMN_l10.git
    ```

2. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```

## Запуск:
1. Получите сервисный ключ доступа на платформе [vk.cc]('https://dev.vk.com/ru/api/access-token/getting-started')
2. Создайте в папке проекта файл `.env` и сохраните в нём полученный сервисный ключ доступа:
    ```
    VK_SERVICE_KEY = 'сервисный ключ доступа'
    ```

3. Запустите скрипт:
    ```
    python clicks_counter.py
    ```

4. Введите ссылку:
    - Если ввсети обычную ссылку - для неё будет получена короткая ссылка:
        ```
        C:\Users> python clicks_counter.py
        Введите ссылку: dvmn.org/modules
        Сокращенная ссылка: https://vk.cc/cwSc1H
        ```

    - Если ввести короткую ссылку - будет получено количество переходов (кликов) по ссылке:
        ```
        C:\Users> python clicks_counter.py
        Введите ссылку: https://vk.cc/cwSc1H
        Количество кликов:  12
        ```
