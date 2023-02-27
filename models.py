from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))

    # groups = relationship('Group', backref="notes", passive_deletes=True)



# class Teacher(Base):
#     __tablename__ = "teachers"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(150), nullable=False)
#
#     disciplines = relationship('Disciplines', passive_deletes=True)
#
#
# class Discipline(Base):
#     __tablename__ = "disciplines"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(150), nullable=True)
#     teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete="CASCADE"))
#
#     teachers = relationship('Teachers', passive_deletes=True)
#     grades = relationship('Grades', passive_deletes=True)





