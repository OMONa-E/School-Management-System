from sqlalchemy.orm import Session
from app import models, schemas

# ==============================
# CRUD-L Operations for Schools
# ==============================
# Create a new school - CRUD-L: Create
def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(**school.model_dump())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

# Get all schools - CRUD-L: List
def get_schools(db: Session, skip: int = 0, limit: int = 200):
    return db.query(models.School).offset(skip).limit(limit).all()

# Get a school by ID - CRUD-L: Read
def get_school(db: Session, school_id: int):
    return db.query(models.School).filter(models.School.id == school_id).first()

# Update a school by ID - CRUD-L: Update
def update_school(db: Session, school_id: int, school_update: schemas.SchoolUpdate):
    db_school = db.query(models.School).filter(models.School.id == school_id).first()
    
    if db_school:
        for key, value in school_update.model_dump(exclude_unset=True).items():
            setattr(db_school, key, value)
        db.commit()
        db.refresh(db_school)
        return db_school
    return None

# Deletes School by ID - CRUD-L: Delete
def delete_school(db: Session, school_id: int):
    db_school = db.query(models.School).filter(models.School.id == school_id).first()
    
    if db_school:
        db.delete(db_school)
        db.commit()
        return db_school
    return None
