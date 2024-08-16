from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    job_title = Column(String(50), nullable=True)
    salary = Column(Numeric(10, 2), nullable=True)
    department = Column(String(50), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    percentage = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, nullable=True)

class Assignment(Base):
    __tablename__ = "assignments"

    id_assignment = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    assignment_date = Column(Date, nullable=False)

    employee = relationship("Employee", back_populates="assignments")
    project = relationship("Project", back_populates="assignments")

Employee.assignments = relationship("Assignment", back_populates="employee")
Project.assignments = relationship("Assignment", back_populates="project")
