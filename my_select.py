from sqlalchemy import func, desc, and_, select

from connect_db import session
from models import Student, Group, Discipline, Teacher, Grade


def select_seeded():
    has_student = session.query(Student.id).select_from(Student).filter(Student.id == 1).first()
    has_group = session.query(Group.id).select_from(Group).filter(Group.id == 1).first()
    has_discipline = session.query(Discipline.id).select_from(Discipline).filter(Discipline.id == 1).first()
    has_teacher = session.query(Teacher.id).select_from(Teacher).filter(Teacher.id == 1).first()
    has_grade = session.query(Grade.id).select_from(Grade).filter(Grade.id == 1).first()
    if (has_grade and
            has_student and
            has_discipline and
            has_teacher and
            has_group):
        return True


def select_1():
    result_list = []
    res_query = session.query(Student.fullname,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student)\
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5).all()
    for row in res_query:
        result_list.append(f'{row.fullname}: {row.avg_grade}')
    return '\n'.join(result_list)


def select_2(disc_id=1):
    res_query = session.query(Discipline.name,
                              Student.fullname,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == disc_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return f'{res_query[0][0]} - {res_query[0][1]}: {res_query[0][2]}'


def select_3(disc_id=1):
    result_list = []
    res_query = session.query(Discipline.name,
                              Group.name,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == disc_id) \
        .group_by(Discipline.name, Group.name) \
        .order_by(Group.name) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]} - {res_query[i][1]}: {res_query[i][2]}')
    return '\n'.join(result_list)


def select_4():
    res_query = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .limit(1).all()
    return f'Average grade: {res_query[0][0]}'


def select_5(teach_id=1):
    result_list = []
    res_query = session.query(Discipline.name,
                              Teacher.fullname
                              ) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teach_id) \
        .group_by(Discipline.name, Teacher.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][1]} - {res_query[i][0]}')
    return '\n'.join(result_list)


def select_6(stud_id=1):
    result_list = []
    res_query = session.query(Group.name,
                              Student.fullname
                              ) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == stud_id) \
        .group_by(Group.name, Student.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]} - {res_query[i][1]}')
    return '\n'.join(result_list)


def select_7(group_id=1, disc_id=1):
    result_list = []
    res_query = session.query(Group.name,
                              Discipline.name,
                              Student.fullname,
                              Grade.grade,
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Group.id == group_id, Grade.discipline_id == disc_id)) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]}, {res_query[i][1]} - {res_query[i][2]}: {res_query[i][3]}')
    return '\n'.join(result_list)


def select_8(teach_id=1):
    res_query = session.query(Teacher.fullname,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teach_id) \
        .group_by(Teacher.fullname) \
        .all()
    return f'{res_query[0][0]}: {res_query[0][1]}'


def select_9(stud_id=1):
    result_list = []
    res_query = session.query(Discipline.name,
                              Student.fullname,
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Student.id == stud_id)\
        .group_by(Student.id, Discipline.name) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][1]} - {res_query[i][0]}')
    return '\n'.join(result_list)


def select_10(stud_id=1, teach_id=1):
    result_list = []
    res_query = session.query(Discipline.name.label('discipline'),
                              Student.fullname.label('student'),
                              Teacher.fullname.label('teacher'),
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Student.id == stud_id, Teacher.id == teach_id))\
        .group_by(Student.fullname, Discipline.name, Teacher.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]}: {res_query[i][1]} - {res_query[i][2]}')
    return '\n'.join(result_list)


def select_11(stud_id=1, teach_id=1):
    res_query = session.query(Student.fullname.label('student'),
                              Teacher.fullname.label('teacher'),
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Student.id == stud_id, Teacher.id == teach_id)) \
        .group_by(Teacher.fullname, Student.fullname) \
        .all()
    return f'{res_query[0][1]} - {res_query[0][0]} :{res_query[0][2]}'


def select_12(disc_id=1, group_id=1):
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
                and_(Grade.discipline_id == disc_id, Group.id == group_id))
                .order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    res_query = session.query(Discipline.name,
                              Student.fullname,
                              Group.name,
                              Grade.date_of,
                              Grade.grade
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == disc_id,
                     Group.id == group_id,
                     Grade.date_of == subquery))\
        .order_by(desc(Grade.date_of))\
        .all()
    date_of = res_query[0][3].strftime("%d.%m.%Y")
    return f'{res_query[0][0]} {date_of} - {res_query[0][2]} {res_query[0][1]}: {res_query[0][4]}'


def select_group():
    result = session.query(Group.id, Group.name).select_from(Group).all()
    return result


def select_teacher():
    result = session.query(Teacher.id, Teacher.fullname).select_from(Teacher).all()
    return result


def select_student():
    result = session.query(Student.id, Student.fullname, Student.group_id).select_from(Student).all()
    return result


def select_discipline():
    result = session.query(Discipline.id, Discipline.name, Discipline.teacher_id).select_from(Discipline).all()
    return result


def select_grade():
    result = session.query(Grade.id,
                           Grade.grade,
                           Grade.discipline_id,
                           Grade.student_id,
                           Grade.date_of)\
        .select_from(Grade).all()
    return result
