import sqlite3
import image_capture as ic
import model_training as mt
import tkinter as tk

def add_new_user():
    def submit_name():
        PERSON_NAME = name_entry.get()  # Get the entered name
        PERSON_EMAIL = email_entry.get()
        PERSON_ROLE = "Admin"
        print(PERSON_NAME)
        print(PERSON_EMAIL)
        name_window.destroy()  # Close the pop-up window
        ic.capture_photos(PERSON_NAME, PERSON_EMAIL, PERSON_ROLE)  # Call capture_photos with the entered name
        mt.train_model()  # Train the model after capturing photos

    name_window = tk.Tk()
    name_window.title("Add New User")

    # Center the window
    screen_width = name_window.winfo_screenwidth()
    screen_height = name_window.winfo_screenheight()
    window_width, window_height = 300, 300
    x_coord = (screen_width // 2) - (window_width // 2)
    y_coord = (screen_height // 2) - (window_height // 2)
    name_window.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")
    name_window.attributes('-topmost', True)
    name_window.focus_force()

    tk.Label(name_window, text="Enter the name of the new user:", font=("Helvetica", 12)).pack(pady=10)
    name_entry = tk.Entry(name_window, width=30)
    name_entry.pack(pady=10)

    tk.Label(name_window, text="Enter the email of the new user:", font=("Helvetica", 12)).pack(pady=10)
    email_entry = tk.Entry(name_window, width=30)
    email_entry.pack(pady=10)

    submit_button = tk.Button(name_window, text="Submit", command=lambda: [submit_name()])
    submit_button.pack(pady=10)

    name_window.mainloop()

con = sqlite3.connect("Blackout.db")

cur = con.cursor()

cur.execute("CREATE TABLE users(name,role, secret_key)")

cur.execute("CREATE TABLE data_log(name, timestamp)")

add_new_user()

con.commit()  # Save the changes
con.close()  # Close the connection
