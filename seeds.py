from datetime import datetime, timedelta
from random import randint

from faker import Faker

from connect_db import session
from models import Student, Group

NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
GROUPS = ['БД-23-1', 'БД-23-2', 'БД-23-3']
DISCIPLINES = [
    'SQLite',
    'MySQL',
    'Oracle',
    'SQL Server',
    'PostgreSQL',
    'SQL Alchemy',
    'MongoDB',
    'Redis'
]

fake = Faker()

def seed_groups():
    for num_group in GROUPS:
        group = Group(
            name=num_group
        )
        session.add(group)
    session.commit()


def seed_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
            fullname=fake.name(),
            group_id=randint(1, NUMBER_TEACHERS)
        )
        session.add(student)
    session.commit()


def seed_disciplines(curs):
    sql = 'INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);'
    curs.executemany(sql, zip(DISCIPLINES, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(DISCIPLINES)))))


def seed_grades(curs):
    sql = 'INSERT INTO grades(grade, discipline_id, student_id, date_of) VALUES(?, ?, ?, ?);'
    start_date = datetime.fromisoformat('2022-09-01')
    end_date = datetime.fromisoformat('2023-06-29')
    list_work_days = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.isoweekday() < 6:
            list_work_days.append(current_date)
        current_date += timedelta(days=1)
    grades = []
    for day in list_work_days:
        random_discipline = randint(1, len(DISCIPLINES))
        random_student = [randint(1, len(DISCIPLINES)) for _ in range(5)]
        for student in random_student:
            grades.append((randint(1, 12), random_discipline, student, day.date()))
    curs.executemany(sql, grades)