import cv2
import os
from datetime import datetime
import sqlite3
import pyotp
import pyqrcode

def create_folder(folder, name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    person_folder = os.path.join(folder, name)
    if not os.path.exists(person_folder):
        os.makedirs(person_folder)
    return person_folder


def delete_folder(name):
    dataset_folder = "dataset"
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)

    person_folder = os.path.join(dataset_folder, name)
    if os.path.exists(person_folder):
        os.rmdir(person_folder)

def capture_photos(name, email, role):
    space_count = 0
    folder = create_folder("dataset",name)
    
    # Initialize the camera
    cam = cv2.VideoCapture(0)

    photo_count = 0
    
    print(f"Taking photos for {name}. Press SPACE to capture, 'q' to quit.")
    
    while True:
        # Capture frame from camera
        ret, image = cam.read()
        
        # Display the frame
        cv2.imshow('SPACE to capture image. Q to quit', image)

        key = cv2.waitKey(1)
        
        if key == ord(' '):  # Space key
            photo_count += 1
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.jpg"
            filepath = os.path.join(folder, filename)
            cv2.imwrite(filepath, image)
            print(f"Photo {photo_count} saved: {filepath}")
            space_count += 1
        
        elif key == ord('q'):  # Q key
            break

    if space_count == 0:
        delete_folder(name)
    else:
        con = sqlite3.connect("Blackout.db")
        cur = con.cursor()

        otp_folder = create_folder("OTP", name)
        person_qr = os.path.join(otp_folder, "OTP.svg")

        if not os.path.exists(person_qr):
            secret_key = pyotp.random_base32()

            url_qr = pyotp.totp.TOTP(secret_key).provisioning_uri(email, issuer_name="Facial Recognition")
            url = pyqrcode.create(url_qr)
            url.svg(person_qr, scale=8)


        # Use parameterized queries to insert the data
        cur.execute("INSERT INTO users (name,role, secret_key) VALUES (?, ?, ?)", (name, role, secret_key))
        con.commit()  # Save the changes
        con.close()  # Close the connection


    # Clean up
    cam.release()
    cv2.destroyAllWindows()
    print(f"Photo capture completed. {photo_count} photos saved for {name}.")