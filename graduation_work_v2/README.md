## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```
Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```
* Подготовлен тестовый суперпользователем с именем: `admin` паролем: `admin` и e-mail: `1@1.ru`
* Команда для загрузки тестовых данных
```bash
python manage.py loaddata db.json
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
## Команды для dampdata
* Команда для создания дампа
```bash
  python manage.py dumpdata > db.json # создание дампа
```
* Команда для загрузки дампа
```bash
  python manage.py loaddata db.json # загрузка дампа
```