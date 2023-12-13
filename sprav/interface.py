"""Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
from vivod_kontaktov import print_contacts, add_contakt, find_contact, copi_old
 
CONSTACTS = "sprav\contakt.txt"

def interface():
    while True:
        print("Выберерете действие:\
            \n 1 - Добавить контакт\
            \n 2 - Вывести контакт\
            \n 3 - Найти контакт\
            \n 4 - Скопировать данные в новый файл\
            \n 0 - Выйти из программы")
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contakt(CONSTACTS)
            case 2:
                print_contacts(CONSTACTS)
            case 3:
                find_contact(CONSTACTS)
            case 4:
                copi_old(CONSTACTS)
            case _:
                print('Не введена команда.')


if __name__ == '__main__':
    interface()