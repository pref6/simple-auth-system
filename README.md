# simple-auth-system
Simple-auth-system - это простое приложение на основе фреймворка Django, которое включает в себя основную страницу, систему авторизации и панель управления. Использует django-auto-reload для горячей перезагрузки, чтобы облегчить вашу разработку. Также django-tailwind, чтобы вы могли сразу же начать использовать TailwindCSS.

**Компоненты:**
  1. landing_page - она же основная страница, куда попадает пользователь, когда только заходит на сайт.
  2. account - система регистрации, логина и выхода с аккаунта.
  3. dashboard - сюда пользователь попадает после регистрации/логина. Если пользователь уже залогинен - он минует landing_page.

**Для работы необходимо:**
  1. Python 3
  2. Django (последняя версия)

**Установка на Linux:**

Клонируйте репозиторий в нужную вам директорию:
```
git clone https://github.com/pref6/simple-auth-system.git
```
Создайте виртуальное окружение и активируйте его:
```
python3 -m venv <ваше название>
<ваше название>/bin/activate
```
Установите Django:
```
pip install django
```
Установите зависимости из requirements.txt:
```
pip install -r requirements.txt
```
Запустите setup.sh и введите новое имя проекта:
```
sh setup.sh
...
Введите новое имя проекта: 
```
Измените название .env.example на .env и замените ключ в параметре SECRET_KEY.
```
DEBUG="True"
SECRET_KEY=""
```
**Использование:**

Запустите tailwind:
```
python manage.py tailwind start
```
Запустите Django:
```
python manage.py runserver
```
**Добавление Tailwind в дополнительные шаблоны:**

По умолчанию landing_page, accounts и dashboard имеют встроенную поддержку Tailwind в соответствующих файлах base.html.

Однако если вы хотите создать новое приложение и добавить в него поддержку Tailwind, либо наследуйте файлы base.html других приложений, либо добавьте следующие теги в свои новые HTML-шаблоны:
```
{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>
```
