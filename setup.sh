#!/bin/bash

# Exit on error
set -e

echo "Starting setup process..."

# Create and activate virtual environment
echo "Setting up Python virtual environment..."
python -m venv venv

# Source the virtual environment based on OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt
pip install gdown


# Create the 'data' directory
echo "Creating 'data' directory..."
mkdir -p data

# Verify directory creation
if [ -d "data" ]; then
    echo "'data' directory created successfully."
else
    echo "Failed to create 'data' directory."
    exit 1
fi


# Download Kaggle dataset
echo "Downloading Kaggle dataset..."

python -m bin.download_data

# Start Docker containers
echo "Starting Docker containers..."
docker-compose up --build

echo "Setup complete!"