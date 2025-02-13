from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Define the School Model
class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    level = Column(String, nullable=False)
    location = Column(String, nullable=False)
    student_count = Column(Integer, nullable=False)
    student_age_range = Column(String, nullable=False)
    student_performance_avg = Column(String, nullable=False) 
    male_female_ratio = Column(String, nullable=False)
    male_female_dropout_ratio = Column(String, nullable=False)
    teacher_count = Column(Integer, nullable=False)    
    teacher_phd_count = Column(Integer, nullable=False)
    teacher_degree_count = Column(Integer, nullable=False)
    teacher_diploma_count = Column(Integer, nullable=False)
    teacher_cert_count = Column(Integer, nullable=False)
    teacher_experience_1_3_count = Column(Integer, nullable=False)
    teacher_experience_4_6_count = Column(Integer, nullable=False)
    teacher_experience_7_10_count = Column(Integer, nullable=False)
    teacher_experience_10_plus_count = Column(Integer, nullable=False)
    
# Define the User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    