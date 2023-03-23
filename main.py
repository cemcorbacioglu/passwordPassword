import random
import string
import tkinter as tk


def generate_password():
    # Define the set of special characters and choose two at random
    specials = '!@#$%^&*()_+'
    first_special = random.choice(specials)
    second_special = random.choice(specials)

    # Choose 2 random digits
    digit1 = random.choice(string.digits)
    digit2 = random.choice(string.digits)

    # Generate a random 6-character string of uppercase and lowercase letters
    chars = string.ascii_letters
    password = ''
    for i in range(6):
        password += (random.choice(chars))

    # Concatenate the components of the password and return the result
    return f"{first_special}{digit1}{digit2}{second_special}{password}"


def copy_to_clipboard(password):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    root.destroy()


def generate_password_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Password Generator")

    # Create a label to display the generated password
    password_label = tk.Label(window, text="", font=("Arial", 16))
    password_label.pack()

    # Create a button to generate a new password
    generate_button = tk.Button(window, text="Generate Password",
                                command=lambda: password_label.config(text=generate_password()))
    generate_button.pack()

    # Create a button to copy the password to the clipboard
    copy_button = tk.Button(window, text="Copy to Clipboard",
                            command=lambda: copy_to_clipboard(password_label.cget("text")))
    copy_button.pack()

    # Start the main event loop
    window.mainloop()


generate_password_gui()
