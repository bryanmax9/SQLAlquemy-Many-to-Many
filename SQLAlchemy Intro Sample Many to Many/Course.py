from typing import List
from sqlalchemy import Column, Integer, UniqueConstraint, ForeignKey, ForeignKeyConstraint
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped

from Department import Department
from orm_base import Base
from Section import Section


class Course(Base):
    __tablename__ = "courses"

    departmentAbbreviation: str = Column(String(10), ForeignKey('departments.abbreviation'), primary_key=True)
    department: Mapped[Department] = relationship(back_populates="courses")


    courseNumber: int = Column(Integer, nullable=False, primary_key=True)

    name: str = Column(String(50), nullable=False)
    description: str = Column(String(500), nullable=False)
    units: int = Column(Integer, nullable=False)


    sections: Mapped[List[Section]] = relationship("Section", back_populates="course")

    __table_args__ = (

        UniqueConstraint("departmentAbbreviation", "name", name="courses_uk_01"),
    )




    def __init__(self, department: Department, courseNumber: int, name: str, description: str, units: int):
        self.set_department(department)
        self.courseNumber = courseNumber
        self.name = name
        self.description = description
        self.units = units

    def set_department(self, department: Department):
        self.department = department
        self.departmentAbbreviation = department.abbreviation

    def __str__(self):
        return f"Department abbrev: {self.departmentAbbreviation} number: {self.courseNumber} name: {self.name}"
