from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(20), nullable=False, unique=True)
    #
    # students = relationship('Students', passive_deletes=True)

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(20), nullable=False, unique=True)
    group_id = Column('group_id', ForeignKey('groups.id'))
    #
    # students = relationship('Students', passive_deletes=True)



# class Teachers(Base):
#     __tablename__ = "teachers"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String(150), nullable=False)
#
#     disciplines = relationship('Disciplines', passive_deletes=True)
#
#
# class Disciplines(Base):
#     __tablename__ = "disciplines"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(150), nullable=True)
#     teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete="CASCADE"))
#
#     teachers = relationship('Teachers', passive_deletes=True)
#     grades = relationship('Grades', passive_deletes=True)





