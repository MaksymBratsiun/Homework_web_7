from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey

from connect_db import engine

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
    group = relationship("Group", backref="students")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(150), nullable=False)


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete="CASCADE"))

    teacher = relationship("Teacher", backref="disciplines")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    discipline_id = Column('discipline_id', ForeignKey('disciplines.id', ondelete="CASCADE"))
    student_id = Column('student_id', ForeignKey('students.id', ondelete="CASCADE"))
    date_of = Column(DateTime, nullable=False)

    discipline = relationship("Discipline",  backref="grades")
    student = relationship("Student", backref="grades")


Base.metadata.create_all(engine)
