#!/bin/bash

# Set the project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create a virtual environment
python3 -m venv "$PROJECT_DIR/venv"

# Activate the virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r "$PROJECT_DIR/requirements.txt"

# Deactivate the virtual environment
deactivate

echo "Virtual environment setup complete!"