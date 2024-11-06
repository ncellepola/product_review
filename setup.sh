#!/bin/bash

# Exit on error
set -e

echo "Starting setup process..."

# Clone the repository
echo "Cloning repository..."
git clone https://github.com/ncellepola/aamzon_sentiment_analysis.git
cd aamzon_sentiment_analysis

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
pip install kagglehub

# Download Kaggle dataset
echo "Downloading Kaggle dataset..."
export KAGGLE_CONFIG_DIR=.kaggle/kaggle.json
python -m bin.download_data

# Start Docker containers
echo "Starting Docker containers..."
docker-compose up --build

echo "Setup complete!"