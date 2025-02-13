from pydantic import BaseModel, __version__ as pydantic_version
from typing import Optional

# Base Schema for school
class SchoolBase(BaseModel):
    name: str
    level: str
    location: str
    student_count: int
    male_female_ratio: str
    teacher_count: int
    student_age_range: str
    student_performance_avg: str
    male_female_ratio: str
    male_female_dropout_ratio: str
    teacher_count: int    
    teacher_phd_count: int
    teacher_degree_count: int
    teacher_diploma_count: int
    teacher_cert_count: int
    teacher_experience_1_3_count: int
    teacher_experience_4_6_count: int
    teacher_experience_7_10_count: int
    teacher_experience_10_plus_count: int

    class Config:
        if pydantic_version.startswith('1'):
            orm_mode = True
        else:
            from_attributes = True

# Schema for creating a school
# Inherits from SchoolBase
# This is the schema that the client will send to the server
class SchoolCreate(SchoolBase):
    pass
# Schema for updating a school
# Inherits from SchoolBase
# This is the schema that the client will send to the server
class SchoolUpdate(BaseModel):
    name: Optional[str] = None
    level: Optional[str] = None
    location: Optional[str] = None
    student_count: Optional[int] = None
    male_female_ratio: Optional[str] = None
    teacher_count: Optional[int] = None
    student_age_range: Optional[str] = None
    student_performance_avg: Optional[str] = None
    male_female_ratio: Optional[str] = None
    male_female_dropout_ratio: Optional[str] = None
    teacher_count: Optional[int] = None    
    teacher_phd_count: Optional[int] = None
    teacher_degree_count: Optional[int] = None
    teacher_diploma_count: Optional[int] = None
    teacher_cert_count: Optional[int] = None
    teacher_experience_1_3_count: Optional[int] = None
    teacher_experience_4_6_count: Optional[int] = None
    teacher_experience_7_10_count: Optional[int] = None
    teacher_experience_10_plus_count: Optional[int] = None

    class Config:
        if pydantic_version.startswith('1'):
            orm_mode = True
        else:
            from_attributes = True

# Schema for response from the server
# Inherits from SchoolBase
# This is the schema that the server will send to the client
class SchoolResponse(SchoolBase):
    id: int
    
# Base User Schema
class UserBase(BaseModel):
    username: str
    email: str
    role: str

    class Config:
        if pydantic_version.startswith('1'):
            orm_mode = True
        else:
            from_attributes = True

# Schema for creating a user
# Inherits from UserBase
# This is the schema that the client will send to the server
class UserCreate(UserBase):
    password: str
# Schema for updating a user
# Inherits from UserBase
# This is the schema that the client will send to the server
class UserUpdate(BaseModel):
    password: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None

    class Config:
        if pydantic_version.startswith('1'):
            orm_mode = True
        else:
            from_attributes = True

# Schema for response from the server
# Inherits from UserBase
# This is the schema that the server will send to the client
class UserResponse(UserBase):
    id: int

# Schema for User password change
class ChangePassword(BaseModel):
    old_password: str
    new_password: str

    class Config:
        if pydantic_version.startswith('1'):
            orm_mode = True
        else:
            from_attributes = True

# Schema for User password change
class UserPassword(ChangePassword):
    pass
