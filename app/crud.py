from sqlalchemy.orm import Session
from . import models, schemas

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.project_id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if db_project:
        for key, value in project.dict().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
        return db_project
    return None

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return db_project
    return None


def get_assignment(db: Session, id_assignment: int):
    return db.query(models.Assignment).filter(models.Assignment.id_assignment == id_assignment).first()

def get_assignments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Assignment).offset(skip).limit(limit).all()

def create_assignment(db: Session, assignment: schemas.AssignmentCreate):
    # Verificar si el empleado ya está asignado a otro proyecto
    existing_assignment = db.query(models.Assignment).filter(
        models.Assignment.employee_id == assignment.employee_id
    ).first()

    if existing_assignment:
        raise ValueError("Employee is already assigned to another project")

    db_assignment = models.Assignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def update_assignment(db: Session, id_assignment: int, assignment: schemas.AssignmentCreate):
    db_assignment = db.query(models.Assignment).filter(models.Assignment.id_assignment == id_assignment).first()
    if db_assignment:
        for key, value in assignment.dict().items():
            setattr(db_assignment, key, value)
        db.commit()
        db.refresh(db_assignment)
        return db_assignment
    return None

def delete_assignment(db: Session, id_assignment: int):
    db_assignment = db.query(models.Assignment).filter(models.Assignment.id_assignment == id_assignment).first()
    if db_assignment:
        db.delete(db_assignment)
        db.commit()
        return db_assignment
    return None

