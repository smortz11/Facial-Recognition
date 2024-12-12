#!/bin/bash

# Exit on error
set -e

# Step 1: Create a virtual environment with system-site-packages
echo "Creating virtual environment..."
python3 -m venv --system-site-packages face_rec

# Step 2: Activate the virtual environment
echo "Activating the virtual environment..."
source face_rec/bin/activate

# Step 3: Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update && sudo apt full-upgrade -y

# Step 4: Install OpenCV
echo "Installing OpenCV..."
pip install opencv-python

# Step 5: Install Imutils
echo "Installing Imutils..."
pip install imutils

# Step 6: Install CMake (you may need to confirm during this step)
echo "Installing CMake..."
sudo apt install -y cmake

# Step 7: Install the face-recognition library
echo "Installing face-recognition library. This may take some time, so feel free to grab a cup of tea!"
pip install face-recognition

# Step 8: Install additional dependencies from requirements.txt
echo "Installing additional dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping additional dependency installation."
fi

# Step 9: Run the setup.py file
if [ -f "setup.py" ]; then
    echo "Running setup.py..."
    python setup.py
else
    echo "setup.py not found. Please ensure it exists in the project directory."
fi

# Step 10: Inform the user of completion
echo "Setup is complete! Your project is ready to use."