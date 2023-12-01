numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = int(input("Введіть число n: "))
result = [x for x in numbers if x < n]
print("Числа, які менші за", n, ":", result)

strings = ("\ndadada 1", "nenenene 2", "xschemxschem 3\n")
result = ", ".join(strings)
print(result)

library = {
    "Джим Керри": {"Автор": "Тедди Ватсон", "Рік видання": 1876, "Кількість сторінок": 275},
    "Комик": {"Автор": "Джон Буш", "Рік видання": 1883, "Кількість сторінок": 350},
    "Любовник": {"Автор": "Хералд Гуард", "Рік видання": 1819, "Кількість сторінок": 400},
}
book_title = input("Введіть назву книги: ")
if book_title in library:
    book_info = library[book_title]
    print(f"Інформація про книгу '{book_title}':")
    for key, value in book_info.items():
        print(f"{key}: {value}")
else:
    print(f"\nКнига '{book_title}' не знайдена в бібліотеці.")

students = {
    "Шевцов": ("Алексей", 20, "Інформатика"),
    "Марк": ("Мирон", 22, "Математика"),
    "Техник": ("Павел", 19, "Фізика"),
    "Огурцов": ("Семен", 23, "Хімія"),
    "Платон": ("Никита", 18, "Економіка"),
    "Стойко": ("Севастян", 25, "Психологія"),
    "Волох": ("Ростислав", 21, "Соціологія"),
    "Пивовар": ("Андрій", 27, "Історія"),
    "Васильчук": ("Анна", 24, "Біологія"),
    "Сивуха": ("Ярослав", 26, "Географія"),
    "Хованский": ("Максим", 20, "Філософія"),
    "Джарахов": ("Єльдар", 19, "Література"),
}
surname = input("\nВведіть прізвище студента: ")
if surname in students:
    name, age, specialty = students[surname]
    print(f"Прізвище: {surname}")
    print(f"Ім'я: {name}")
    print(f"Вік: {age} років")
    print(f"Спеціальність: {specialty}")
else:
    print("\nСтудента з таким прізвищем не знайдено.\n")

phonebook = {
    "Ярослав": ["121-121-121", "121-121-122"],
    "Єльдар": ["456-456-456", "123-123-123", "111-222-333"],
    "Никита": ["990-880-770", "660-550-440"],
    "Павел": ["115-116-117", "225-226-227", "335-336-337"],
    "Андрій": ["181-191-101", "282-292-202"],
    "Ростислав": ["424-482-848", "609-506-106"],
}
def add_phone_number(contact_name, new_phone_number):
    if contact_name in phonebook:
        phonebook[contact_name].append(new_phone_number)
    else:
        phonebook[contact_name] = [new_phone_number]
def display_phonebook():
    for contact, phone_numbers in phonebook.items():
        print(f"Контакт: {contact}")
        print(f"Номери телефонів: {', '.join(phone_numbers)}")
        print()
while True:
    contact_name = input("\nВведіть ім'я контакту (або 'вийти' для завершення): ")
    if contact_name.lower() == 'вийти':
        break
    phone_number = input("\nВведіть новий номер телефону: ")
    add_phone_number(contact_name, phone_number)
display_phonebook()

