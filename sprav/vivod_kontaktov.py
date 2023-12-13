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
import shutil

def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print("Список контактов пустой!")

def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 80295485523): ')
    cont_info = input()
    return cont_info

def add_contakt(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print('Введите критерий для поиска:\
          \n 1 - Имя \
          \n 2 - Фамилия \
          \n 3 - Телефон')
    
    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)

def copi_old(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            all_cont = {index + 1: value for index, value in enumerate(all_cont)}
            for (k,v) in all_cont.items():
                print(k, v)

            print('Выберите строку для копирования: ')
            comm = int(input())
            print(all_cont[comm])
            new_cont = str(all_cont[comm])
            with open('sprav\\new_file.txt', 'w', encoding='utf8') as file:
                file.writelines(new_cont)
            #shutil.copyfile('sprav\contakt.txt', 'new_file(full).txt')
            print(f'Скопированя строка: {all_cont[comm]}')
        else:
            print("Список контактов пустой!")