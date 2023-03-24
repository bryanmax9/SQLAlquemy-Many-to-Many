

from orm_base import Base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, Identity, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Enrollment(Base):
    """A relationship between a student and a course section that the student has enrolled in."""
    __tablename__ = "enrollments"
    enrollmentId: Mapped[int] = mapped_column('enrollment_id', Integer, Identity(start=1, cycle=True), primary_key=True)
    sectionId: Mapped[int] = mapped_column('section_id', ForeignKey("sections.section_id"), primary_key=False)
    studentId: Mapped[int] = mapped_column('student_id', ForeignKey("students.student_id"), primary_key=False)
    enrollmentDate: Mapped[datetime] = mapped_column('enrollment_date', DateTime, nullable=False)

    # Bi-directional relationship from Student to Enrollment.
    student: Mapped["Student"] = relationship( back_populates="enrollments")
    # Bi-directional relationship from Section to Enrollment.
    section: Mapped["Section"] = relationship( back_populates="enrollments")

    def __init__(self, student, section):
        self.student = student
        self.section = section
        self.studentId = student.studentID
        self.sectionId = section.sectionId
        self.enrollmentDate = datetime.now()
