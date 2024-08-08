from django.core.management.base import BaseCommand
import os
import sys

class Command(BaseCommand):
    help = "Переименовывает Django проект."
    
    def add_arguments(self, parser):
        parser.add_argument('old_project_name', type=str, help='Актуальное имя')
        parser.add_argument('new_project_name', type=str, help='Новое имя')
    
    def handle(self, *args, **kwargs):

        # Получает старое и новое имя из аргументов командной строки
        old_project_name = kwargs['old_project_name']
        new_project_name = kwargs['new_project_name']
        
        print(f"Renaming {old_project_name} to {new_project_name}...")
        
        #Rename the project directory
        os.rename(old_project_name, new_project_name)

        # Проходится по всем файлам в каталоге проекта и его подкаталогах
        for root, dirs, files in os.walk(new_project_name):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    # Открывает файл для чтения
                    with open(file_path, 'r') as f:
                        file_contents = f.read()

                    # Заменяет все старые имена на новое
                    file_contents = file_contents.replace(old_project_name, new_project_name)

                    # Открывает файл для записи и записывает измененное значение
                    with open(file_path, 'w') as f:
                        f.write(file_contents)
                except:
                    pass

        # Переименовывает название проекта в manage.py
        with open(f"./manage.py", 'r') as f:
            file_contents = f.read()

            # Заменяет старые имена на новые
            file_contents = file_contents.replace(f'{old_project_name}', f'{new_project_name}')

            # Открывает файл для записи и записывает измененное значение
            with open(f"./manage.py", 'w') as f:
                print("writing to file")
                f.write(file_contents)

        # Сообщает, что имя проекта было изменено
        print(f"{old_project_name} has been renamed to {new_project_name}.")