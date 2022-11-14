# Foodgram-project
![example workflow](https://github.com/ed-yp-re4/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Описание проекта
Foodgram-project - проект для размещания рецептов. Доступны функции:
- Просмотр рецептов
- Регистрация пользователя
- Создание рецепта
- Редактирование рецепта
- Добавление рецепта в избранное
- Подписка на автора рецепта
- Добавление ингредиентов рецепта в список для покупок
- Скачивание списка ингредиентов для покупок
- Администратору доступна панель управления данными

### Технологии:
- Python 3.8
- Django 2.2
- Django REST Flamework
- gunicorn
- nginx
- PostgreSQL
- Docker
- Docker Compose
- React

### Проект запускается в контейнерах Docker, структура контейнеров:
- web - python + Django + gunicorn - backend-часть
- db - PostgreSQL
- nginx - web-сервер
- frontend - фронтенд-часть на React

### Запуск проекта:
* Установите Docker и Docker Compose.
* Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:ed-yp-re4/foodgram-project-react.git
cd foodgram-project-react
```
* Перейти в папку с infra:
```
cd infra
```
* Создайте и заполнить файл с переменными окружения .env
```
# Параметры для контейнера db
POSTGRES_DB=<название БД>
POSTGRES_USER=<SQL пользователь БД>
POSTGRES_PASSWORD=<пароль для SQL User>
```
```
# Параметры для контейнера web
# Настройки соедиения с DB для Django:
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<название БД>
DB_USER=<SQL пользователь БД>
DB_PASS=<пароль для SQL User>
DB_HOST=db
DB_PORT=5432
DEBUG=False

ALLOWED_HOST=<IP сервера>
```
* В файле default.conf выставить IP сервера (по умолчанию 127.0.0.1):
```
server_name <IP сервера>;
```

* Запустить сборку docker-compose:
```
sudo docker-compose up -d
```
* Проверить запуск http://<IP сервера>/admin/ в браузере, интерфейс администратора Django должен быть доступен.

* Выполнить миграции:
```
sudo docker compose exec web python manage.py makemigrations --noinput
```
```
sudo docker-compose exec web python manage.py migrate
```
* Создать суперпользователя:
```
sudo docker-compose exec web python manage.py createsuperuser
```
* Собрать статику:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
* Заполнить базу предустановленным списком тегов и ингредиентов:
```
sudo docker-compose exec web python manage.py add_tags_from_data
sudo docker-compose exec web python manage.py add_ingredients_from_data
```
### Доступ к проекту:
```http://<ваш IP>/api/docs/``` - документация  
```http://<ваш IP>/api/``` - API проекта  
```http://<ваш IP>/admin``` - панель администратора  
```http://<ваш IP>/``` - проект  

### Проект развернут:
```http://62.84.127.94/api/docs/```  
```http://62.84.127.94/admin/```  
```http://62.84.127.94/api/```  
```http://62.84.127.94/```  

### Суперпользователь
`username: admin`  
`password: admin`  
