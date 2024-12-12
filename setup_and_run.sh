#!/bin/bash

# Exit on error
set -e

echo "Checking for python3-venv..."
if ! dpkg -s python3-venv &> /dev/null; then
    echo "python3-venv is not installed. Installing it now..."
    if [ "$(uname)" == "Darwin" ]; then
      if ! command -v brew &> /dev/null; then
          echo "Homebrew not found. Installing Homebrew..."
          /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || { echo "Failed to install Homebrew."; exit 1; }
      fi
        echo "Running on MacOS. Using Homebrew to install python3-venv."
        brew install python@3.9 || { echo "Failed to install python3-venv with Homebrew."; exit 1; }
    elif [ "$(uname)" == "Linux" ]; then
        sudo apt update || { echo "Failed to update package list."; exit 1; }
        sudo apt install -y python3-venv || { echo "Failed to install python3-venv."; exit 1; }
    else
        echo "Unsupported OS. Please install python3-venv manually."
        exit 1
    fi
else
    echo "python3-venv is already installed."
fi

# Step 1: Create a virtual environment with system-site-packages
echo "Creating virtual environment..."
python3 -m venv --system-site-packages face_rec

# Step 2: Activate the virtual environment
echo "Activating the virtual environment..."
source face_rec/bin/activate

# Step 3: Update and upgrade the system
echo "Updating and upgrading the system..."
if [ "$(uname)" == "Linux" ]; then
    sudo apt update && sudo apt full-upgrade -y || { echo "Failed to update and upgrade system."; exit 1; }
elif [ "$(uname)" == "Darwin" ]; then
    echo "Updating system using Homebrew on MacOS (not necessary)."
else
    echo "Unsupported OS. Please update manually."
    exit 1
fi

# Step 4: Install OpenCV
echo "Installing OpenCV..."
pip install --upgrade opencv-python || { echo "Failed to install OpenCV."; exit 1; }

# Step 5: Install Imutils
echo "Installing Imutils..."
pip install --upgrade imutils || { echo "Failed to install Imutils."; exit 1; }

# Step 6: Install CMake
echo "Installing CMake..."
if [ "$(uname)" == "Linux" ]; then
    sudo apt update || { echo "Failed to update package list."; exit 1; }
    sudo apt install -y cmake || { echo "Failed to install CMake."; exit 1; }
elif [ "$(uname)" == "Darwin" ]; then
    brew install cmake || { echo "Failed to install CMake with Homebrew."; exit 1; }
else
    echo "Unsupported OS. Please install CMake manually."
    exit 1
fi

echo "CMake installed successfully!"

# Step 7: Install the face-recognition library
echo "Installing face-recognition library. This may take some time, so feel free to grab a cup of tea!"
pip install --upgrade face-recognition || { echo "Failed to install face-recognition library."; exit 1; }

# Step 8: Install additional dependencies from requirements.txt
echo "Installing additional dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt || { echo "Failed to install additional dependencies."; exit 1; }
else
    echo "requirements.txt not found. Skipping additional dependency installation."
fi

# Step 9: Run the setup.py file
if [ -f "setup.py" ]; then
    echo "Running setup.py..."
    python setup.py || { echo "Failed to run setup.py."; exit 1; }
else
    echo "setup.py not found. Please ensure it exists in the project directory."
fi

# Step 10: Inform the user of completion
echo "Setup is complete! Your project is ready to use."
