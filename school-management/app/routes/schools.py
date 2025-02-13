from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database, models, schemas, auth, crud_l
from typing import List

# Create a new instance of the APIRouter class
router = APIRouter()

# Create a new school - CRUD-L: Create
@router.post("/create", response_model=schemas.SchoolResponse)
async def create_school(school: schemas.SchoolCreate, db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    if user.role not in ['admin', 'manager', 'Admin', 'Manager']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
    return crud_l.create_school(db, school)

# Get all schools - CRUD-L: List
@router.get("/all", response_model=List[schemas.SchoolResponse])
async def get_schools(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud_l.get_schools(db, skip, limit)

# Get a school by ID - CRUD-L: Read
@router.get("/{school_id}", response_model=schemas.SchoolResponse)
async def get_school(school_id: int, db: Session = Depends(database.get_db)):
    school = crud_l.get_school(db, school_id)
    if not school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School not found")
    return school

# Update a school by ID - CRUD-L: Update
@router.put("/{school_id}", response_model=schemas.SchoolResponse)
async def update_school(school_id: int, school: schemas.SchoolUpdate, db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    if user.role not in ['admin', 'manager', 'Admin', 'Manager']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
    updated_school = crud_l.update_school(db, school_id, school)
    if not updated_school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School not found")
    return updated_school

# Deletes School by ID - CRUD-L: Delete
@router.delete("/{school_id}")
async def delete_school(school_id: int, db: Session = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    if user.role not in ['admin', 'manager', 'Admin', 'Manager']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized User")
    deleted_school = crud_l.delete_school(db, school_id)
    if not deleted_school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="School not found")
    return {"message": f"""School -> {deleted_school.name} -> was deleted sucessfully!"""}
