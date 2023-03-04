import argparse
from datetime import datetime

from connect_db import session
from models import Grade, Group, Teacher, Student, Discipline
from my_select import select_group, select_teacher, select_student, select_discipline, select_grade


def create_id_by_model(input_model, new_data):
    query_create = None
    if input_model == 'Grade':
        data_split = new_data.split(', ')
        if len(data_split) > 3:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 3:
            print('Not enough arguments.')
            exit()
        date_of_create = datetime.now()
        try:
            query_create = Grade(grade=data_split[0],
                                 discipline_id=data_split[1],
                                 student_id=data_split[2],
                                 date_of=date_of_create
                                 )
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Discipline':
        data_split = new_data.split(', ')
        if len(data_split) > 2:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 2:
            print('Not enough arguments.')
            exit()
        try:
            query_create = Discipline(name=data_split[0], teacher_id=data_split[1])
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Teacher':
        data_split = new_data.split(', ')
        if len(data_split) > 1:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 1:
            print('Not enough arguments.')
            exit()
        try:
            query_create = Teacher(fullname=data_split[0])
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Student':
        data_split = new_data.split(', ')
        if len(data_split) > 2:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 2:
            print('Not enough arguments.')
            exit()
        try:
            query_create = Student(fullname=data_split[0], group_id=data_split[1])
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Group':
        data_split = new_data.split(', ')
        if len(data_split) > 1:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 1:
            print('Not enough arguments.')
            exit()
        try:
            query_create = Group(name=data_split[0])
        except Exception as e:
            print('Create failure.')
            print(e)

    else:
        print(f'Model with name: {input_model} not exists')
    if query_create:
        try:
            session.add(query_create)
            session.commit()
            print('Create completed.')
        except Exception as e:
            print('Create failure.')
            print(e)
        finally:
            session.close()


def read_model(input_model, id_model):
    try:
        if id_model is None:
            id_model = 0
        id_model = int(id_model)
    except Exception as e:
        print(e)
        exit()
    if input_model == 'Group':
        group = select_group()
        print('Group list (data for create or update: "id(only for update), name")')
        if not id_model:
            for g in group:
                print(f'id: {g.id}, name: {g.name}')
        elif id_model:
            count = 0
            for g in group:
                if g[0] == id_model:
                    print(f'id: {g[0]}, name: {g[1]}')
                    count = 1
            if count == 0:
                print(f'Data with id: {id_model} not exists')

    elif input_model == 'Teacher':
        teacher = select_teacher()
        print('Teacher list (data for create or update: "id(only for update), fullname")')
        if not id_model:
            for t in teacher:
                print(f'id: {t.id}, fullname: {t.fullname}')
        elif id_model:
            count = 0
            for t in teacher:
                if t[0] == id_model:
                    print(f'id: {t[0]}, fullname: {t[1]}')
                    count = 1
            if count == 0:
                print(f'Data with id: {id_model} not exists')

    elif input_model == 'Student':
        student = select_student()
        print('Student list (data for create & update: "id(only for update), fullname, group_id")')
        if not id_model:
            for s in student:
                print(f'id: {s.id}, fullname: {s.fullname}, group_id: {s.group_id}')
        elif id_model:
            count = 0
            for s in student:
                if s[0] == id_model:
                    print(f'id: {s[0]}, fullname: {s[1]}, group_id: {s[2]}')
                    count = 1
            if count == 0:
                print(f'Data with id: {id_model} not exists')

    elif input_model == 'Discipline':
        discipline = select_discipline()
        print('Discipline list (data for create & update: "id(only for update), name, group_id")')
        if not id_model:
            for d in discipline:
                print(f'id: {d.id}, name: {d.name}, teacher_id: {d.teacher_id}')
        elif id_model:
            count = 0
            for d in discipline:
                if d[0] == id_model:
                    print(f'id: {d[0]}, fullname: {d[1]}, teacher_id: {d[2]}')
                    count = 1
            if count == 0:
                print(f'Data with id: {id_model} not exists')

    elif input_model == 'Grade':
        grade = select_grade()
        print('Grade list (data for create & update: "id(only for update), grade, discipline_id, student_id)'
              '(date_of always equally current_date")')
        if not id_model:
            for gr in grade:
                print(f'id: {gr.id},'
                      f' grade: {gr.grade}, '
                      f'discipline_id: {gr.discipline_id}, '
                      f'student_id: {gr.student_id}, '
                      f'date_of: {gr.date_of.strftime("%d.%m.%Y")}')
        elif id_model:
            count = 0
            for gr in grade:
                if gr[0] == id_model:
                    print(f'id: {gr[0]},'
                          f' grade: {gr[1]}, '
                          f'discipline_id: {gr[2]}, '
                          f'student_id: {gr[3]}, '
                          f'date_of: {gr[4].strftime("%d.%m.%Y")}')
                    count = 1
            if count == 0:
                print(f'Data with id: {id_model} not exists')
    else:
        print('Wrong name of model')
    session.close()


def update_id_in_model(input_model, id_model, new_data):
    query_update = None
    if input_model == 'Grade':
        data_split = new_data.split(', ')
        if len(data_split) > 3:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 3:
            print('Not enough arguments.')
            exit()
        date_of_create = datetime.now()
        query_update = session.query(Grade).filter(Grade.id == id_model)
        try:
            query_update.update({"grade": data_split[0],
                                 'discipline_id': data_split[1],
                                 'student_id': data_split[2],
                                 'date_of': date_of_create})
            print(f'Update Grade id: {query_update.first().id},'
                  f' grade: {query_update.first().grade},'
                  f' discipline_id: {query_update.first().discipline_id},'
                  f' student_id: {query_update.first().student_id}'
                  f' date_of: {query_update.first().date_of.strftime("%d.%m.%Y")}')
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Discipline':
        data_split = new_data.split(', ')
        if len(data_split) > 2:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 2:
            print('Not enough arguments.')
            exit()
        query_update = session.query(Discipline).filter(Discipline.id == id_model)
        try:
            query_update.update({"name": data_split[0], 'teacher_id': data_split[1]})
            print(f'Update Discipline id: {query_update.first().id},'
                  f' name: {query_update.first().name},'
                  f' teacher_id: {query_update.first().teacher_id}')
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Teacher':
        data_split = new_data.split(', ')
        if len(data_split) > 1:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 1:
            print('Not enough arguments.')
            exit()
        query_update = session.query(Teacher).filter(Teacher.id == id_model)
        try:
            query_update.update({"fullname": data_split[0]})
            print(f'Update Teacher id: {query_update.first().id},'
                  f' fullname: {query_update.first().fullname}')
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Student':
        data_split = new_data.split(', ')
        if len(data_split) > 2:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 2:
            print('Not enough arguments.')
            exit()
        query_update = session.query(Student).filter(Student.id == id_model)
        try:
            query_update.update({"fullname": data_split[0], 'group_id': data_split[1]})
            print(f'Update Student id: {query_update.first().id},'
                  f' name: {query_update.first().fullname},'
                  f' teacher_id: {query_update.first().group_id}')
        except Exception as e:
            print('Create failure.')
            print(e)

    elif input_model == 'Group':
        data_split = new_data.split(', ')
        if len(data_split) > 1:
            print('Too many arguments.')
            exit()
        elif len(data_split) < 1:
            print('Not enough arguments.')
            exit()
        query_update = session.query(Group).filter(Group.id == id_model)
        try:
            query_update.update({"name": data_split[0]})
            print(f'Update Group id: {query_update.first().id},'
                  f' name: {query_update.first().name}')
        except Exception as e:
            print('Create failure.')
            print(e)

    else:
        print(f'Model with name: {input_model} not exists')
    if query_update:
        try:
            session.commit()
            print('Create completed.')
        except Exception as e:
            print('Create failure.')
            print(e)
        finally:
            session.close()


def delete_id_in_model(input_model, id_model):
    try:
        id_model = int(id_model)
    except Exception as e:
        print(f'Data with id: {id_model} not exists')
        print(e)
        exit()
    query_del = None
    if input_model == 'Grade':
        query_del = session.query(Grade).filter(Grade.id == id_model).first()
    elif input_model == 'Discipline':
        query_del = session.query(Discipline).filter(Discipline.id == id_model).first()
    elif input_model == 'Teacher':
        query_del = session.query(Teacher).filter(Teacher.id == id_model).first()
    elif input_model == 'Student':
        query_del = session.query(Student).filter(Student.id == id_model).first()
    elif input_model == 'Group':
        query_del = session.query(Group).filter(Group.id == id_model).first()

    if query_del:
        session.delete(query_del)
        session.commit()
        print('Delete completed.')
    else:
        print(f'Data with id: {id_model} not exists')
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CRUD APP')
    parser.add_argument('-a', '--action', help='create, read, update, delete')
    parser.add_argument('-m', '--model', help='Grade, Group, Teacher, Student, Discipline')
    parser.add_argument('-i', '--id', help='id identifier')
    parser.add_argument('-d', '--data', help='with separator between values ", ": "name, group..."')

    args = parser.parse_args()
    my_args = vars(args)

    action = my_args.get('action')
    model = my_args.get('model')
    id_ = my_args.get('id')
    data = my_args.get('data')
    match action:
        case 'create':
            create_id_by_model(model, data)
        case 'read':
            read_model(model, id_)
        case 'update':
            update_id_in_model(model, id_, data)
        case 'delete':
            delete_id_in_model(model, id_)
        case _:
            print('Wrong action. -h for help.')
