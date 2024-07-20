#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Create a temporary requirements file
pip freeze > requirements.txt

# Upgrade all packages
pip install --upgrade -r requirements.txt

# Generate the updated requirements file
pip freeze > requirements.txt

# Deactivate the virtual environment
deactivate

echo "All packages have been upgraded and requirements.txt has been updated."
