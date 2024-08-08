#Делает миграцию базы данных
python manage.py makemigrations && python manage.py migrate

#Переименовывает проект
echo "Введите новое имя проекта: "
read project_name
python manage.py rename 'simple-auth-system' $project_name

#Запускает сервер
python manage.py runserver

#Устаналивает зависимости для tailwind
python manage.py tailwind install

echo "Установка завершена."