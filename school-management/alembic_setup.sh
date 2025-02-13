#!/bin/bash

# Set up error handling
set -e  # Exit script on any error

echo "Setting up Alembic migrations..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv .venv
fi

# Activate virtual environment if not already activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Ensure required dependencies are installed
pip install --upgrade pip
pip install alembic sqlalchemy

# Check if Alembic is available
if ! command -v alembic &> /dev/null; then
    echo "Error: Alembic not found even after installation."
    exit 1
fi

# Ensure correct database driver is installed based on DB type
DB_URL="sqlite:///./school_management.db"  # Change this if using PostgreSQL/MySQL

if [[ "$DB_URL" == postgresql* ]]; then
    pip install psycopg2-binary
elif [[ "$DB_URL" == mysql* ]]; then
    pip install pymysql
fi

# Initialize Alembic if not already initialized
if [ ! -d "alembic" ]; then
    echo "Initializing Alembic..."
    alembic init alembic
fi

# Update alembic.ini with database connection string
sed -i "s|sqlite:///./test.db|$DB_URL|g" alembic.ini

# Generate initial migration
echo "Generating initial migration..."
alembic revision --autogenerate -m "Initial migration" || {
    echo "Error: Migration failed."
    exit 1
}

# Apply migrations
echo "Applying migrations..."
alembic upgrade head || {
    echo "Error: Migration application failed."
    exit 1
}

echo "✅ Alembic setup completed successfully!"

