from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import schools, users
from app.database import engine, Base

# Initialize database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
description = """
SchoolManagementApp API helps you do awesome stuff. 🚀

## Schools
## Users
## Clusters

You can perform **CRUD-L**.
- **C**: Create
- **R**: Read
- **U**: Update
- **D**: Delete
- **L**: List

Feel free to test this API and have fun. 😊
"""

contact = {
    "name": "School Management System API",
    "email": "devopsconet@gmail.com"
}
app = FastAPI(title="School Management System API", description=description, contact=contact, version="1.0.0", redoc_url=None)

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(schools.router, prefix="/api/v1/schools", tags=["School"])
app.include_router(users.router, prefix="/api/v1/users", tags=["User"])

# define a root `/` endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to School Management System API"}
