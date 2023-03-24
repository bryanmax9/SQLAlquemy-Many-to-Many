from typing import List

from sqlalchemy import Column, Integer, String, Time, UniqueConstraint, ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from orm_base import Base
from Enrollment import Enrollment

class Section(Base):
    __tablename__ = 'sections'

    # Surrogate key from Section
    sectionId: Mapped[int] = mapped_column('section_id', Integer, primary_key=True, autoincrement=True)
    departmentAbbreviation: Mapped[str] = mapped_column('department_abbreviation', String(10), nullable=False)
    courseNumber: Mapped[int] = mapped_column('course_number', Integer, nullable=False)
    sectionNumber: Mapped[int] = mapped_column('section_number', Integer, nullable=False)
    semester: Mapped[str] = mapped_column('semester', String(10), nullable=False)
    sectionYear: Mapped[int] = mapped_column('section_year', Integer, nullable=False)
    building: Mapped[str] = mapped_column('building', String(6), nullable=False)
    room: Mapped[int] = mapped_column('room', Integer, nullable=False)
    schedule: Mapped[str] = mapped_column('schedule', String(6), nullable=False)
    startTime: Mapped[Time] = mapped_column('start_time', Time, nullable=False)
    instructor: Mapped[str] = mapped_column('instructor', String(80), nullable=False)

    # Bi-directional relationship from Section to Enrollment.
    enrollments: Mapped[List["Enrollment"]] = relationship(back_populates="section",cascade="all, save-update, delete-orphan")


    course: Mapped["Course"] = relationship("Course", back_populates="sections")

    __table_args__ = (
        UniqueConstraint('building', 'room', 'schedule', 'start_time', name='sections_uk_01'),
        UniqueConstraint('building', 'room', 'semester', 'section_year', 'schedule', 'start_time', 'instructor', name='sections_uk_02'),
        UniqueConstraint('department_abbreviation', 'course_number', 'section_number', 'semester', 'section_year', name='sections_uk_03'),
        UniqueConstraint('department_abbreviation', 'course_number', name='sections_uk_04'),
        ForeignKeyConstraint(
            [departmentAbbreviation, courseNumber],
            ["courses.departmentAbbreviation", "courses.courseNumber"],
            name="fk_sections_courses"
        ),

    )


    def __init__(self, course, sectionNumber, semester, sectionYear, building, room, schedule, startTime, instructor):
        self.course = course
        self.departmentAbbreviation = course.departmentAbbreviation
        self.courseNumber = course.courseNumber
        self.sectionNumber = sectionNumber
        self.semester = semester
        self.sectionYear = sectionYear
        self.building = building
        self.room = room
        self.schedule = schedule
        self.startTime = startTime
        self.instructor = instructor

    def add_student(self, student):
        # Make sure that this student does not already have this section.
        for next_student in self.enrollments:
            if next_student.student == student:
                return  # This student already has this section
        # Create the new instance of StudentMajor to connect this Student to the supplied Major.
        section_student = Enrollment(self, student)  # How does this gets commited?

        # student.enrollments.append(section_student)  # Add this Student to the supplied Section.
        # self.enrollments.append(section_student)  # Add the supplied Section to this student.

    def remove_student(self, student):
        for next_student in self.enrollments:
            # This item in the list is the major we are looking for for this student.
            if next_student.student == student:
                self.enrollments.remove(next_student)
                return

    def __str__(self):
        return f"{self.departmentAbbreviation} {self.courseNumber}-{self.sectionNumber} ({self.semester} {self.sectionYear}) with {self.instructor} at {self.building} {self.room}, {self.schedule} {self.startTime}"
