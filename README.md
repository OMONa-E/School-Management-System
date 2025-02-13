# School Management System API

This project is a **FastAPI-based backend API** designed for **school management** with **Role-Based Access Control (RBAC)**. It allows **CRUD-L (Create, Read, Update, Delete, List)** operations for schools and users, with authentication and authorization mechanisms in place. The system is built for the **Ministry of Education and Sports** to manage school-related data efficiently.

---

## Features
- **CRUD-L Operations** for Schools and Users.
- **Role-Based Access Control (RBAC)** for Admin, Manager and Users.
- **JWT Authentication** for secure access.
- **SQLAlchemy ORM** for database interactions.
- **Alembic** for database migrations.
- **API Versioning** with `/api/v1/`.
- Automated setup using **Bash scripts** (`setup.sh` and `alembic_setup.sh`).
- Well-documented API endpoints accessible via Swagger UI.

---

## Folder Structure
```
school-management/
│── app/
│   ├── main.py            # FastAPI app entry point
│   ├── models.py          # SQLAlchemy ORM models
│   ├── database.py        # DB connection setup
│   ├── crud.py            # CRUDL operations
│   ├── routes/
│   │   ├── schools.py     # School management endpoints
│   │   ├── users.py       # Authentication & RBAC 
│   ├── schemas.py         # Pydantic models
│   ├── auth.py            # JWT authentication
│── tests/                 # Unit tests
│── requirements.txt       # Dependencies
│── .env                   # Environment variables
│── alembic_setup.sh       # Database Migration and setup automated
│── README.md              # Documentation
│── setup.sh               # Folder creation automated
```

---

## Prerequisites
- Python 3.9 or higher
- SQLite (or any SQL database supported by SQLAlchemy)
- FastAPI
- SQLAlchemy
- Alembic
- JWT for authentication

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd school-management
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# python3 -m venv .venv
source .venv/bin/activate  # For Linux/MacOS
# . .venv/bin/activate    # For Linux/MacOS
# .venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
Create a `.env` file in the root directory with the following content:
```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run Database Migrations
Navigate to the directory containing `alembic_setup.sh` and run:
```bash
chmod +x alembic_setup.sh  # Make the script executable
./alembic_setup.sh         # Run the script
```

### 6. Start the FastAPI Server
Navigate to the `app` directory and run:
```bash
fastapi dev main.py
```

### 7. Access the API Documentation
Open your browser and go to:
```
http://localhost:8000/docs
```
This will open the **Swagger UI** where you can interact with the API endpoints.

---

## API Endpoints

### School Management
- **GET** `/api/v1/schools/all` - List all schools.
- **GET** `/api/v1/schools/{school_id}` - Retrieve a specific school by ID.
- **POST** `/api/v1/schools/create` - Create a new school.
- **PUT** `/api/v1/schools/{school_id}` - Update a school by ID.
- **DELETE** `/api/v1/schools/{school_id}` - Delete a school by ID.

### User Management (RBAC)
- **POST** `/api/v1/users/register` - Register a new user.
- **POST** `/api/v1/users/login` - Login and get an access token.
- **GET** `/api/v1/users/all` - List all users (Admin only).
- **GET** `/api/v1/users/me` - Retrieve current user.
- **GET** `/api/v1/users/{user_id}` - Retrieve a specific user by ID (Admin only).
- **PUT** `/api/v1/users/{user_id}` - Update a user by ID (Admin only).
- **DELETE** `/api/v1/users/{user_id}` - Delete a user by ID (Admin only).

---

## Environment Variables
The `.env` file should contain the following variables:
- `SECRET_KEY`: A secret key for JWT token generation.
- `ALGORITHM`: The algorithm used for JWT token signing (default: `HS256`).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes.

---

## Database Schema

### School Table
| Column                        | Type        | Description                                       |
|-------------------------------|-------------|---------------------------------------------------|
| ID                            | Integer     | Primary Key                                       |
| Name                          | String      | Name of the school                                |
| Level                         | String      | School level (e.g., Primary)                      |
| Location                      | String      | School location                                   |
| Student Count                 | Integer     | Total number of students                          |
| Male/Female Ratio             | String      | Ratio of male to female students                  | 
| Teacher Count                 | Integer     | Total number of teachers                          |
| Student Age Range             | String      | Age range of students                             |
| Student Performance Avg       | Float       | Average student performance (e.g., exam score)    |
| Male/Female Dropout Ratio     | String      | Ratio of male to female dropouts                  |
| Teacher PhD Count             | Integer     | Number of teachers with PhD qualifications        |
| Teacher Degree Count          | Integer     | Number of teachers with degree qualifications     |
| Teacher Diploma Count         | Integer     | Number of teachers with diploma qualifications    |
| Teacher Cert Count            | Integer     | Number of teachers with certificate qualifications|
| Teacher Experience 1-3 Count  | Integer     | Number of teachers with 1-3 years of experience   |
| Teacher Experience 4-6 Count  | Integer     | Number of teachers with 4-6 years of experience   |
| Teacher Experience 7-10 Count | Integer     | Number of teachers with 7-10 years of experience  |
| Teacher Experience 10+ Count  | Integer     | Number of teachers with 10+ years of experience   |

### User Table
| Column            | Type        | Description                     |
|-------------------|-------------|---------------------------------|
| ID                | Integer     | Primary Key                     |
| Username          | String      | Unique username                 |
| Password Hash     | String      | Hashed password                 |
| Role              | String      | User role (Admin/User)          |

---

### Notes:
1. **Student Performance Avg**: This column stores the average performance of students (e.g., exam scores or grades).
2. **Male/Female Dropout Ratio**: This column tracks the dropout ratio between male and female students.
3. **Teacher Qualifications**: The `Teacher PhD Count`, `Teacher Degree Count`, `Teacher Diploma Count`, and `Teacher Cert Count` columns track the number of teachers with specific qualifications.
4. **Teacher Experience**: The experience columns categorize teachers based on their years of experience..
---

## Dependencies
Listed in `requirements.txt`:
```
cat requirements.txt  # to view
# pip freeze  # to view
# pip freeze > requirements.txt  # to write to file 
```

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or issues, please open an issue on the repository or contact the maintainer.

---

Happy coding! 🚀
