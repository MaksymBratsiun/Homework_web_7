from sqlalchemy import func

from connect_db import session
from models import Student, Group


def select_test():
    result = session.query(Student.fullname, Group.name).select_from(Student).join(Group).filter(Group.id == 1)
    for res in result:
        print(res)


if __name__ == '__main__':
    select_test()