# METRO Parser
Программа для парсинга данных продуктов с сайта METRO.

### Stack:
- Python;
- requests;
- JSON;
- ООП.

### Установка и запуск:
- git clone https://github.com/Idvri/METRO_Parser.git - клонируем проект к себе в нужную директорию;
- python -m venv env - создаем вирт. окружение;
- venv/Scripts/activate (Windows) | source venv/bin/activate (Linux) - запускаем вирт. окружение;
- pip install -r requirements.txt - устанавливаем зависимости;
- python main.py - запускаем проект.

### Функционал:
- получение данных с https://api.metro-cc.ru/products-api/graph;
- запись данных в json;
- проверка дубликатов.
