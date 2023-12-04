Проект REST API для туристических горных перевалов.

Описание:
Этот проект разрабатывается студентами SkillFactory для Федерации Спортивного Туризма и Развития (ФСТР) с целью упростить процесс учета горных перевалов и сократить время обработки данных. 

По заданию необходимо усовершенствовать REST API для ведения базы горных перевалов, которая пополняется туристами. 

Реализованы методы: 
1. API POST/submitData для добавления туристом информации о новом перевале; 
2. GET /submitData/ — получение одной записи о перевале по ее id, в том числе статус модерации; 
3. PATCH /submitData/ — редактирование существующей записи, если она еще не поступила в работу модератору;
4. GET /submitData/?user__email= — список данных обо всех объектах, которые пользователь с почтой отправил на сервер.

Параметры реализации:
1. При подготовке проекта использована база данных PostgreSQL, установка производится командой:
   pip install psycopg2
2. Порт, логин, пароль и путь к базе данных берется из переменных окружения с использованием библиотеки dotenv:
   pip install python-dotenv
3. В файле requirements.txt приведен список внешних зависимостей, который формируется командoй 
   pip freeze > requirements.txt. 
4. Установите зависимости командой:
   pip install -r requirements.txt
5. Добавлен визуальный интерфейс Swagger. 
   За основу при установке взят следующий источник 
   /api/schema/swagger-ui, для генерирования документации /api/schema/redoc/
6. Код приложения был покрыт тестами, установлена библиотека coverage.
7. Сменить статус модерации можно только через админ-панель по адресу: 
   /admin. 
8. Возможность работы в ней обеспечивается созданием модератора по команде:
python manage.py createsuperuser

Как работать с API (endpoints):

1. Создать информацию о новом перевале с помощью POST.
   /api/submitData/pereval/ 
   или api/schema/swagger-ui/#/api/api_submitData_pereval_create 
2. Получить одну запись о перевале по ее id, в том числе статус модерации c помощью GET. 
   /api/submitData/pereval/id или 
   api/schema/swagger-ui/#/api/api_submitData_pereval_retrieve 
3. Редактировать существующую запись, если она еще не поступила в работу модератору с помощь PATCH.
   /api/submitData/pereval/id или 
   /api/schema/swagger-ui/#/api/api_submitData_pereval_partial_update 
4. С помощью GET получить список данных обо всех объектах, которые пользователь с почтой отправил на сервер.
   /api/submitData/user__email=str:email или 
   /api/schema/swagger-ui/#/api/api_submitData_user__email%3D_list  

Пример JSON-запроса для создания, редактирования сведений о перевале:

{
    "beauty_title": "Куркурек",
    "title": "Северо-Чуйский хребет",
    "other_titles": "Звенящий",
    "connect": "",
    "user": {
        "email": "proba2@yandex.ru",
        "fam": "Иванов",
        "name": "Петр",
        "otc": "Михайлович",
        "phone": "89167854534"
    },
    "coords": {
        "latitude": 50.12536,
        "longitude": 87.65502,
        "height": 3989
    },
    "level": {
        "winter": "1b",
        "summer": "",
        "autumn": "",
        "spring": ""
    },
    "images": [
        { 
          "data": ""
          "title" ""
        }
    ]
}



Этапы Проект Pereval

1. Создание виртуального окружения:
   python -m venv venv
2. Активировать виртуальное окружение:
   venv\scripts\activate
3. Установка django:
   pip install django
4. Создание проекта pereval:
   django-admin startproject perval
5. Создание приложения pereval_app:
   python manage.py startapp pereval_app
6. Создание базы данных postgresql :
   Используемая СУБД - PostgreSQL
7. Проектирование моделей:
   User; Coords; Level; Pereval; Image;
8. Проектирование Views и Serializers
9. Приметение миграций, настройки приложения
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
10. Проверки тестирование