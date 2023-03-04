from sqlalchemy import inspect

from connect_db import engine
from seeds import seed_groups, seed_students, seed_teachers, seed_disciplines, seed_grades
import my_select


HELLO_TEXT = '''
This DB created with Alembic.
You need have existing tables in this DB.
If your DB is clear. Run in terminal
    >>>"alembic upgrade head"'''

QUERY_LIST = [
    '0. Exit',
    '1. Знайти пять студентів із найбільшим середнім балом з усіх предметів.',
    '2. Знайти студента із найвищим середнім балом з певного предмета.',
    '3. Знайти середній бал у групах з певного предмета.',
    '4. Знайти середній бал на потоці (по всій таблиці оцінок).',
    '5. Знайти які курси читає певний викладач.',
    '6. Знайти список студентів у певній групі.',
    '7. Знайти оцінки студентів у окремій групі з певного предмета.',
    '8. Знайти середній бал, який ставить певний викладач зі своїх предметів.',
    '9. Знайти список курсів, які відвідує студент.',
    '10. Список курсів, які певному студенту читає певний викладач.',
    '11. Середній бал, який певний викладач ставить певному студентові.',
    '12. Оцінки студентів у певній групі з певного предмета на останньому занятті.'
]

HANDLER_SELECT = {
    '1': my_select.select_1,
    '2': my_select.select_2,
    '3': my_select.select_3,
    '4': my_select.select_4,
    '5': my_select.select_5,
    '6': my_select.select_6,
    '7': my_select.select_7,
    '8': my_select.select_8,
    '9': my_select.select_9,
    '10': my_select.select_10,
    '11': my_select.select_11,
    '12': my_select.select_12
}


def get_handler(operator):
    return HANDLER_SELECT.get(operator)


def db_exists():
    return (inspect(engine).has_table("students") and
            inspect(engine).has_table("groups") and
            inspect(engine).has_table("teachers") and
            inspect(engine).has_table("disciplines") and
            inspect(engine).has_table("grades"))


def seed_all():
    try:
        seed_teachers()
        seed_groups()
        seed_students()
        seed_disciplines()
        seed_grades()
    except Exception as err:
        print(err)


def main():
    print(HELLO_TEXT)
    user_input = ''
    if db_exists():
        print('---------You have correct DB------------')
    else:
        print('Your DB has wrong structure. Exit and create correct DB with empty tables.')
        exit()

    db_has_info = my_select.select_seeded()
    if db_has_info:
        print('---------DB has info in tables----------')
    else:
        while True:
            user_input = input('Do you want to seed tables? (Y/N): ')
            user_input = user_input.strip().lower()
            if user_input == 'y':
                seed_all()
                print('Seed DB completed')
            elif user_input == 'n':
                break

    print('Choose any action and input number:')
    for row in QUERY_LIST:
        print(row)
    while True:
        user_input = input('Input action?(0-12): ')
        user_input = user_input.strip().lower()
        if user_input == '0':
            break
        if user_input in HANDLER_SELECT:
            print(QUERY_LIST[int(user_input)])
            try:
                str_query = str(get_handler(user_input)())
                print(str_query)
            except FileNotFoundError as e:
                print(e)
        else:
            print(f'Incorrect input: {user_input}. Try again...')


if __name__ == '__main__':
    main()
