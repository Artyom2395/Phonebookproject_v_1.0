import csv

class PhoneBookManager:
    def list_contacts(self, filename: str) -> None:
        """
        Выводит список контактов из телефонного справочника, считанных из CSV-файла.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        None
        """
        self.read_and_print_csv(filename)

    def add_contact(self, filename: str) -> None:
        """
        Добавляет новый контакт в телефонный справочник, сохраняя данные в CSV-файл.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        None
        """
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите организацию: ")
        work_phone = input("Введите рабочий телефон: ")
        personal_phone = input("Введите личный телефон: ")

        contact_data = {
            'Имя': first_name,
            'Фамилия': last_name,
            'Отчество': middle_name,
            'Организация': organization,
            'Рабочий телефон': work_phone,
            'Личный телефон': personal_phone
        }

        self.write_data_to_csv(filename, contact_data)
        print("Контакт успешно добавлен")

    def write_data_to_csv(self, filename: str, data: dict) -> None:
        """
        Записывает данные о контакте в CSV-файл.

        Parameters:
        - filename (str): Путь к CSV-файлу.
        - data (dict): Данные о контакте.

        Returns:
        None
        """
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']

        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()
            data['ID'] = str(self.generate_unique_id(filename))
            
            writer.writerow(data)
            print("Контакт добавлен в CSV")
    
    def generate_unique_id(self, filename: str) -> int:
        """
        Генерирует уникальный ID для контакта на основе существующих ID в CSV-файле.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        int: Уникальный ID.
        """
        existing_ids = set()
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_ids.add(int(row['ID']))

        
        new_id = 1
        while new_id in existing_ids:
            new_id += 1

        return new_id

    def edit_contact(self, filename: str, contact_id: int) -> None:
        """
        Редактирует контакт в телефонном справочнике на основе введенного ID.

        Parameters:
        - filename (str): Путь к CSV-файлу.
        - contact_id (int): ID контакта для редактирования.

        Returns:
        None
        """
        contacts = self.read_csv(filename)

        found_contact = None
        for contact in contacts:
            if int(contact['ID']) == contact_id:
                found_contact = contact
                break

        if found_contact:
            updated_contact = self.edit_contact_data(found_contact)
            self.update_contact_in_csv(filename, contact_id, updated_contact)
            print("Контакт успешно обновлен")
        else:
            print(f"Контакт с ID {contact_id} не найден")

    def edit_contact_data(self, contact: dict) -> dict:
        """
        Запрашивает у пользователя новые значения полей контакта для редактирования.

        Parameters:
        - contact (dict): Исходные данные о контакте.

        Returns:
        dict: Обновленные данные о контакте.
        """
        fields_to_edit = ['Имя', 'Фамилия', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']

        for field in fields_to_edit:
            new_value = input(f"Введите новое значение для {field} ({contact[field]}): ")
            if new_value:
                contact[field] = new_value

        return contact

    def update_contact_in_csv(self, filename: str, contact_id: int, updated_contact: dict) -> None:
        """
        Обновляет данные контакта в CSV-файле.

        Parameters:
        - filename (str): Путь к CSV-файлу.
        - contact_id (int): ID контакта для обновления.
        - updated_contact (dict): Обновленные данные о контакте.

        Returns:
        None
        """
        contacts = self.read_csv(filename)

        for contact in contacts:
            if int(contact['ID']) == contact_id:
                contact.update(updated_contact)
                break

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ID', 'Имя', 'Фамилия', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                writer.writerow(contact)

    def search_contacts(self, filename: str) -> None:
        """
        Выполняет поиск контактов в телефонном справочнике на основе заданных критериев.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        None
        """
        field_mapping = {
            'имя': 'Имя',
            'фамилия': 'Фамилия',
            'отчество': 'Отчество',
            'организация': 'Организация',
            'рабочий телефон': 'Рабочий телефон',
            'личный телефон': 'Личный телефон',
            'id': 'ID'
        }

        print("Доступные критерии поиска:")
        for russian_name, csv_field in field_mapping.items():
            print(f"{russian_name.capitalize()} ({csv_field})")

        while True:
            search_criterion = input("Введите критерий поиска (на русском): ").lower()

            # Проверка, что пользовательский ввод соответствует критериям
            if search_criterion in field_mapping:
                break
            else:
                print("Некорректный критерий поиска. Пожалуйста, повторите ввод.")

        search_value = input("Введите значение для поиска: ")

        # Поиск по заданному критерию
        contacts = self.read_csv(filename)
        matching_contacts = []

        for contact in contacts:
            if search_value.lower() in contact[field_mapping[search_criterion]].lower():
                matching_contacts.append(contact)

        print(f"Найдено {len(matching_contacts)} контактов")
        for contact in matching_contacts:
            print(f"ID: {contact['ID']}")
            print(f"ФИО: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}")
            print(f"Организация: {contact['Организация']}")
            print(f"Рабочий телефон: {contact['Рабочий телефон']}")
            print(f"Личный телефон: {contact['Личный телефон']}")
            print("-" * 30)

    def read_csv(self, filename: str) -> list:
        """
        Считывает данные о контактах из CSV-файла.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        list: Список словарей с данными о контактах.
        """
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def read_and_print_csv(self, filename: str) -> None:
        """
        Считывает и выводит на экран данные о контактах из CSV-файла.

        Parameters:
        - filename (str): Путь к CSV-файлу.

        Returns:
        None
        """
        contacts = self.read_csv(filename)

        for contact in contacts:
            print(f"ID: {contact['ID']}")
            print(f"ФИО: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}")
            print(f"Организация: {contact['Организация']}")
            print(f"Рабочий телефон: {contact['Рабочий телефон']}")
            print(f"Личный телефон: {contact['Личный телефон']}")
            print("-" * 30)


