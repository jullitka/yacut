# YaCut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками
- переадресация на исходный адрес при обращении к коротким ссылкам

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?logo=flask)](https://palletsprojects.com/p/flask/)
[![Flask-SQLAlchemy](https://img.shields.io/badge/-FlaskSQLAlchemy-464646?logo=flask)](https://flask-sqlalchemy.palletsprojects.com/en/latest/)
[![Jinja](https://img.shields.io/badge/-Jinja-464646?logo=Jinja)](https://palletsprojects.com/p/jinja/)
[![Flask-WTF](https://img.shields.io/badge/-FlaskWTF-464646?logo=Flask)](https://flask-wtf.readthedocs.io/en/latest/)
[![Flask-Migrate](https://img.shields.io/badge/-Flask_Migrate-464646?logo=Flask)](https://flask-migrate.readthedocs.io/en/latest/index.html)
  
## Запуск проекта
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:jullitka/yacut.git
cd yacut
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполните миграции:
```
flask db init
flask db migrate -m "короткое сообщение"
flask db upgrade
```
Запустите проект:
```
flask run
```
После запуска проект будет доступен по адресу: http://127.0.0.1:5000

## Примеры запросов к API
Доступные эндпоинты:
```
"/api/id/"
"/api/id/{short_id}/"
```
#### Получение полного URL по короткой ссылке (метод GET):
```
 "/api/id/{short_id}/"
```
#### Создание короткой ссылки (метод POST):
```
"/api/id/"
```
В теле запроса необходимо передать:
```
{
    "url": "string",
    "custom_id": "string",
}
```
## Авторы
 [Юлия Пашкова](https://github.com/jullitka)

