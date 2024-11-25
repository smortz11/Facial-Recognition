import image_capture as ic
import model_training as mt
import facial_recognition_hardware as frh
import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import time

def add_new_user():
    PERSON_NAME = input("Please enter the name of the user you would like to add: ")
    ic.capture_photos(PERSON_NAME)
    mt.train_model()

def unlock():
    messagebox.showinfo("Unlock", "Unlock button clicked!")

def lock():
    messagebox.showinfo("Lock", "Lock button clicked!")

def start_facial_recognition():
    name, user_valid = frh.run_facial_recognition()
    if user_valid:
        show_textfield_gui(name)

def show_textfield_gui(name):
    # Create a new Tkinter window for the text field
    textfield_window = tk.Tk()
    textfield_window.title(f"Hello {name}. Enter The OTP: ")

    # Center the window
    screen_width = textfield_window.winfo_screenwidth()
    screen_height = textfield_window.winfo_screenheight()
    window_width, window_height = 300, 150
    x_coord = (screen_width // 2) - (window_width // 2)
    y_coord = (screen_height // 2) - (window_height // 2)
    textfield_window.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

    # Add a text field and button
    entry = tk.Entry(textfield_window, width=30)
    entry.pack(pady=20)
    submit_button = tk.Button(textfield_window, text="Submit", command=lambda: frh.check_user_otp(name, entry.get()))
    submit_button.pack(pady=10)

    textfield_window.mainloop()

def show_welcome_gui():
    # Initialize the main window
    root = tk.Tk()
    root.title("Blackout")

    # Get screen dimensions and center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width, window_height = 300, 200
    x_coord = (screen_width // 2) - (window_width // 2)
    y_coord = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

    # Make the window take focus
    root.attributes('-topmost', True)
    root.focus_force()

    # Create the welcome screen
    label = tk.Label(root, text="Welcome to Blackout", font=("Helvetica", 16))
    label.pack(pady=50)

    login_button = tk.Button(root, text="Login", command=lambda: [root.destroy(), start_facial_recognition()])
    login_button.pack()

    # Run the application
    root.mainloop()

show_welcome_gui()