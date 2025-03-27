# Raspberry Pi Facial Recognition 2FA System

## Overview
This project implements a facial recognition-based two-factor authentication (2FA) system using a Raspberry Pi. The system verifies a user's identity through facial recognition and a secondary authentication method before granting access to a secured area or device.

## Features
- **Facial Recognition**: Uses OpenCV and a trained model to recognize authorized users.
- **Two-Factor Authentication**: Requires both facial recognition and an additional authentication step in the form of a TOTP.
- **Secure Access Control**: Can be integrated with a relay module to control electronic locks.
- **Logging**: Logs of when the system is accessed can be saved.
- **Lightweight & Efficient**: Designed to run efficiently on a Raspberry Pi with minimal resource consumption.

## Hardware Requirements
- Raspberry Pi 4 (or Raspberry Pi 3B+)
- USB webcam
- 5V relay module (for controlling lock)
- I/O devices

## Software Requirements
- Raspbian OS (latest version recommended)
- Python 3

## Installation
1. **Enable Camera on Raspberry Pi**:
    ```sh
    sudo raspi-config
    ```
    - Navigate to *Interfacing Options > Camera* and enable it.
    - Reboot the Raspberry Pi.

2. **Install and Setup (Linux & MacOS)**:
    ```sh
    git clone https://github.com/smortz11/Facial-Recognition.git && cd facial-recognition-project && chmod +x setup_and_run.sh && ./setup_and_run.sh
    ```

3. **Install and Setup (Windows)**:
    ```sh
    git clone https://github.com/smortz11/Facial-Recognition.git cd facial-recognition-project && setup_and_run.bat
    ```

## Usage
1. Users attempt access by presenting their face to the camera.
2. If recognized, the system prompts for a second factor OTP.
3. Upon successful authentication, the system triggers access to the home GUI.
4. Users can active/deactivate the solenoid lock.
5. Logs can be saved to the desktop.

## Future Improvements
- Infrared cameras
- QR-based OTP to rid of keyboard.
- An anomaly detection system for spoofing attempts.

## License
This project is licensed under the MIT License.
