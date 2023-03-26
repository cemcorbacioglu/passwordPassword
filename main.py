from tkinter import *
import pycountry
import random
import string
import pyperclip


def generate_country_name():
    countries = list(pycountry.countries)
    country = random.choice(countries)
    if 5 < len(country.name) < 8 and len(country.name.split()) == 1:
        return country.name
    else:
        return generate_country_name()


def generate_country_password():
    special_chars = "-!@*?$_.%"
    digits = string.digits

    country_name = generate_country_name()

    password = random.choice(special_chars) # one special character at the beginning
    password += ''.join(random.choice(digits) for _ in range(2)) # 2 digits
    password += random.choice(special_chars) # one special character
    password += country_name

    return password


def generate_password():
    special_chars = "-!@*?$_.%"
    digits = string.digits
    
    password = random.choice(special_chars) # one special character at the beginning
    password += ''.join(random.choice(digits) for _ in range(2)) # 2 digits
    password += random.choice(special_chars) # one special character
    password += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6)) # 6 character long string
    
    return password

def copy_to_clipboard(password_var):
    password = password_var.get()
    pyperclip.copy(password)


def generate_password_gui():
    root = Tk()
    root.title("Password Generator")
    root.geometry("300x200")

    password_var = StringVar()

    password_label = Label(root, textvariable=password_var, font=("Helvetica", 16))
    password_label.pack(pady=10)

    generate_password_button = Button(root, text="Generate Password", font=("Helvetica", 12), command=lambda: password_var.set(generate_password()))
    generate_password_button.pack(pady=10)

    generate_country_button = Button(root, text="Generate Country Password", font=("Helvetica", 12), command=lambda: password_var.set(generate_country_password()))
    generate_country_button.pack(pady=10)

    copy_button = Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password_var))

    copy_button.pack(pady=10)

    root.mainloop()

generate_password_gui()
