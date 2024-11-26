import image_capture as ic
import model_training as mt
import facial_recognition_hardware as frh
import tkinter as tk
from tkinter import messagebox

def start_facial_recognition():
    name, user_valid = frh.run_facial_recognition()
    if user_valid:
        show_textfield_gui(name)

def validate_user(name, otp):
    return frh.check_user_otp(name, otp)

def show_home_gui(name):
    def add_new_user():
        def submit_name():
            PERSON_NAME = name_entry.get()  # Get the entered name
            PERSON_EMAIL = email_entry.get()
            print(PERSON_NAME)
            print(PERSON_EMAIL)
            name_window.destroy()  # Close the pop-up window
            ic.capture_photos(PERSON_NAME, PERSON_EMAIL)  # Call capture_photos with the entered name
            mt.train_model()  # Train the model after capturing photos

        name_window = tk.Toplevel(home)
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

        submit_button = tk.Button(name_window, text="Submit", command=lambda:[submit_name(),home.focus_force()])
        submit_button.pack(pady=10)

    def unlock():
        #ADD CODE TO UNLOCK THE LOCK HERE
        messagebox.showinfo("Unlock", "Unlock button clicked!")

    def lock():
        # ADD CODE TO LOCK THE LOCK HERE
        messagebox.showinfo("Lock", "Lock button clicked!")

    home = tk.Tk()
    home.title("Blackout")

    # Get screen dimensions and center the window
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    window_width, window_height = 300, 300
    x_coord = (screen_width // 2) - (window_width // 2)
    y_coord = (screen_height // 2) - (window_height // 2)
    home.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

    # Make the window take focus
    home.focus_force()

    # Create the welcome screen
    label = tk.Label(home, text=f"Welcome to Blackout, {name}", font=("Helvetica", 16))
    label.pack(pady=50)

    # Create buttons
    btn_add_user = tk.Button(home, text="Add New User", command=add_new_user, width=20)
    btn_unlock = tk.Button(home, text="Unlock", command=unlock, width=20)
    btn_lock = tk.Button(home, text="Lock", command=lock, width=20)

    # Place buttons on the window
    btn_add_user.pack(pady=10)
    btn_unlock.pack(pady=10)
    btn_lock.pack(pady=10)

    # Run the GUI
    home.mainloop()

def show_textfield_gui(name):
    def submit_and_validate():
        nonlocal validation_successful
        # Get the user input from the text field
        user_input = entry.get()

        # Validate the user input
        if validate_user(name, user_input):
            validation_successful = True
            textfield_window.destroy()  # Close the window if validation succeeds
            show_home_gui(name)
        else:
            entry.delete(0, tk.END)  # Clear the text field if validation fails

    validation_successful = False  # Flag to track validation success

    while not validation_successful:
        # Create a new Tkinter window for the text field
        textfield_window = tk.Tk()
        textfield_window.title(f"Hello {name}. Enter The OTP:")

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

        submit_button = tk.Button(
            textfield_window, text="Submit", command=submit_and_validate
        )
        submit_button.pack(pady=10)

        # Keep the window running
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

# when final change to show_welcome_gui()
show_welcome_gui()