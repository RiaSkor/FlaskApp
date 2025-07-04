# FlaskApp
Веб-приложение на локальном сервере, выполненное на веб-фреймворке Flask с использованием html, css, javascript. Связано с базой данных MySQL (см. файл "конфигурация_БД_paint_products_store").
Для работы использовался редактор кода VS Code.

Рекомендации по установке:
1) в VS Code (с откртытой папкой проекта) открыть терминал: View - Terminal;
2) создать виртуальное окружение (на Windows): py -m venv virtenv;
3) активировать виртуальное окружение (на Windows): virtenv\Scripts\activate;
4) находясь в (virtenv) установить зависимости:
- pip3 install flask
- pip3 install flask-bootstrap4
- pip3 install flask-mysqldb
- pip3 install pyyaml
- pip3 install Flask-CKEditor
6) запустить приложение (на Windows): py app.py

В файле db.yaml прописать свои данные от MySQL Server.
