from sqlalchemy import func, desc, and_

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


def select_2():
    res_query = session.query(Discipline.name,
                              Student.fullname,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == 1) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return f'{res_query[0][0]} - {res_query[0][1]}: {res_query[0][2]}'


def select_3():
    result_list = []
    res_query = session.query(Discipline.name,
                              Group.name,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == 1) \
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


def select_5():
    result_list = []
    res_query = session.query(Discipline.name,
                              Teacher.fullname
                              ) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == 1) \
        .group_by(Discipline.name, Teacher.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][1]} - {res_query[i][0]}')
    return '\n'.join(result_list)


def select_6():
    result_list = []
    res_query = session.query(Group.name,
                              Student.fullname
                              ) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == 1) \
        .group_by(Group.name, Student.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]} - {res_query[i][1]}')
    return '\n'.join(result_list)


def select_7():
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
        .filter(and_(Group.id == 1, Grade.discipline_id == 1)) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]}, {res_query[i][1]} - {res_query[i][2]}: {res_query[i][3]}')
    return '\n'.join(result_list)


def select_8():
    res_query = session.query(Teacher.fullname,
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == 1) \
        .group_by(Teacher.fullname) \
        .all()
    return f'{res_query[0][0]}: {res_query[0][1]}'


def select_9():
    result_list = []
    res_query = session.query(Discipline.name,
                              Student.fullname,
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Student.id == 1)\
        .group_by(Student.id, Discipline.name) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][1]} - {res_query[i][0]}')
    return '\n'.join(result_list)


def select_10():
    result_list = []
    res_query = session.query(Discipline.name.label('discipline'),
                              Student.fullname.label('student'),
                              Teacher.fullname.label('teacher'),
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Student.id == 1, Teacher.id == 1))\
        .group_by(Student.fullname, Discipline.name, Teacher.fullname) \
        .all()
    for i in range(len(res_query)):
        result_list.append(f'{res_query[i][0]}: {res_query[i][1]} - {res_query[i][2]}')
    return '\n'.join(result_list)


def select_11():
    res_query = session.query(Student.fullname.label('student'),
                              Teacher.fullname.label('teacher'),
                              func.round(func.avg(Grade.grade), 2).label('avg_grade')
                              ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(and_(Student.id == 1, Teacher.id == 1)) \
        .group_by(Teacher.fullname, Student.fullname) \
        .all()
    return f'{res_query[0][1]} - {res_query[0][0]} :{res_query[0][2]}'


def select_12():
    return 'Sorry. This chapter is under work.'


# if __name__ == '__main__':
#     print(select_11())
