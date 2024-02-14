# Phonebookproject_v_1.0
Простое консольное приложение для управления телефонным справочником с использованием CSV-файла в качестве базы данных.

Данный скрипт предоставляет управление телефонным справочником через командную строку.
С помощью этого скрипта можно выполнять операции добавления, редактирования, поиска и вывода контактов.

## Как использовать
1. Склонируйте репозиторий:
   ```
   git clone <repo>
   ```
2. Установите необходимые зависимости:

   ```
   pip install -r requirements.txt
   ```
3. Запустите главный файл main.py:
   ```
   python main.py
   ```
Следуйте инструкциям в консоли для выполнения различных команд (list, add, edit, search).

Доступные команды:
- list: Вывести список всех контактов в телефонном справочнике.
- add: Добавить новый контакт в телефонный справочник.
- edit: Редактировать существующий контакт в телефонном справочнике.
- search: Выполнить поиск контактов на основе указанных критериев(в консоли будет задан вопрос о критерии поиска, и конкретном значении поиска).


Проект использует CSV-файл contacts.csv в качестве хранилища данных.
Каждый контакт содержит информацию о имени, фамилии, отчестве, организации, рабочем и личном телефонах.
Контакты также записываются в CSV-файл для сохранения данных между сеансами.