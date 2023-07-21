# YaCut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

## Технологии
- Python
- Flask
- Flask-SQLAlchemy
- Jinja
- Flask-WTF
- Flask-Migrate
  
## Запуск проекта
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:jullitka/yacut.git
```

```
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
```

```
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
- [Юлия Пашкова](https://github.com/jullitka)

