# django_tree_menu

### Установка.

## Cоздать и активировать виртуальное окружение:

```bash 
python -m venv venv
```
Для *nix-систем:

```bash 
source venv/bin/activate
```
Для windows-систем:

```bash 
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:

```bash 
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:

```bash
python manage.py makemigrations menu
python manage.py migrate
```
Создать суперпользователя django:

```bash 
python manage.py createsuperuser
```
Запустить проект:

```bash 
python manage.py runserver
```
Проект и админ-панель :

http://127.0.0.1:8000

http://127.0.0.1:8000/admin


Создание меню:

1. Создайте меню в админке;

2. Создайте пункты для этого меню в админке;

3. Добавьте подпункты. В этом случае поле меню должно быть пустым.


# Разработчики

[Грицай Андрей](https://github.com/Netsky_29): весь проект.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
