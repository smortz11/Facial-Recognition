@echo off
REM Exit on error
setlocal enabledelayedexpansion
set "errorlevel=0"

REM Step 1: Create a virtual environment
echo Creating virtual environment...
python -m venv face_rec

REM Step 2: Activate the virtual environment
echo Activating the virtual environment...
call face_rec\Scripts\activate

REM Step 3: Install Python dependencies
echo Installing OpenCV...
pip install opencv-python

echo Installing Imutils...
pip install imutils

echo Installing CMake...
pip install cmake

echo Installing face-recognition library. This may take some time, so feel free to grab a cup of tea!
pip install face-recognition

REM Step 4: Install additional dependencies from requirements.txt
if exist requirements.txt (
    echo Installing additional dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Skipping additional dependency installation.
)

REM Step 5: Run the setup.py file
if exist setup.py (
    echo Running setup.py...
    python setup.py
) else (
    echo setup.py not found. Please ensure it exists in the project directory.
)

REM Step 6: Inform the user of completion
echo Setup is complete! Your project is ready to use.
pause
