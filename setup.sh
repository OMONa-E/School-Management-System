#!/bin/bash

# Name of our project
directory="school-management"
log_file="setup.log"

# Project directory and structure
mkdir -p $directory/app/routes $directory/app/ml $directory/tests

# Initialize python dev virtual environment
echo "Initializing Python virtual environmen ........." | tee -a $log_file
python3 -m venv .venv

cd $directory || exit

# Activate the virtual environ
. .venv/bin/activate

# Install dependencies to be used
echo "Installing dependencies .........." | tee -a $log_file
pip install --upgrade pip
pip install python-jose
pip install "fastapi[standard]" uvicorn sqlalchemy alembic bcrypt python-dotenv scikit-learn pandas numpy matplotlib

# Write dependencies to requirements.txt
pip freeze > requirements.txt

# Touch/create files
echo "Creating necessary files ..........." | tee -a $log_file
touch app/__init__.py app/main.py app/models.py app/database.py app/crud_l.py app/schemas.py app/auth.py
touch app/routes/__init__.py app/routes/schools.py app/routes/users.py
# touch app/ml/__init__.py app/ml/model.py app/ml/train.py

# Initialize database migrations
echo "Initializing Alembic for database migrations ..........." | tee -a $log_file
alembic init alembic | tee -a $log_file

echo "Setup complete! Run '. .venv/bin/activate' to activate dev environ if not activated." | tee -a $log_file
