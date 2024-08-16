from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    job_title: Optional[str] = None
    salary: Optional[float] = None
    department: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    employee_id: int
    created_at: Optional[date]

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    project_name: str
    start_date: date
    end_date: Optional[date] = None
    percentage: Optional[int] = 0

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    project_id: int
    created_at: Optional[date]

    class Config:
        orm_mode = True

class AssignmentBase(BaseModel):
    employee_id: int
    project_id: int
    assignment_date: date

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id_assignment: int

    class Config:
        orm_mode = True
