# django_tree_menu

### Установка.

Cоздать и активировать виртуальное окружение:

python -m venv venv
Для *nix-систем:

source venv/bin/activate
Для windows-систем:

source venv/Scripts/activate
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

cd yatube_api
python manage.py makemigrations menu
python manage.py migrate
Создать суперпользователя django:

python manage.py createsuperuser
Запустить проект:

python manage.py runserver
Проект и админ-панель :

http://127.0.0.1:8000

http://127.0.0.1:8000/admin


Создание меню:

1. Создайте меню в админке

2. Создайте дочерние пункты меню для этого меню в админке

3. При необходимости добавьте подпункты. В этом случае поле меню должно быть пустым.
