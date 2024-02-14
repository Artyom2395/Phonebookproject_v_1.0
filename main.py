from phone_book_manager import PhoneBookManager

def main():
    filename = 'contacts.csv'
    phone_book_manager = PhoneBookManager()
    
    while True:
        command = input("Доступные команды: list, add, edit, search. Введите 'exit' для выхода: ")

        if command == 'exit':
            break
        elif command == 'list':
            phone_book_manager.list_contacts(filename)
        elif command == 'add':
            phone_book_manager.add_contact(filename)
        elif command == 'edit':
            while True:
                try:
                    contact_id = int(input("Введите ID контакта для редактирования: "))
                    phone_book_manager.edit_contact(filename, contact_id)
                    break  # Выход из цикла при успешном вводе ID
                except ValueError:
                    print("Недопустимый формат ID. Введите корректный ID.")
        elif command == 'search':
            phone_book_manager.search_contacts(filename)
        else:
            print("Недопустимая команда")
            
if __name__ == "__main__":
    main()