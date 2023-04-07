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
    password = (''.join(random.sample(password, len(password))))
    pos = random.randint(0, len(password) - 1)  # pick random position to insert name
    password = "".join((password[:pos], country_name, password[pos:]))  # insert name at pos

    return password


def generate_password():
    special_chars = "-!@*?$_.%"
    digits = string.digits
    
    password = random.choice(special_chars) # one special character at the beginning
    password += ''.join(random.choice(digits) for _ in range(2)) # 2 digits
    password += random.choice(special_chars) # one special character
    password += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6)) # 6 character long string

    return (''.join(random.sample(password, len(password))))

def copy_to_clipboard(password_var):
    password = password_var.get()
    pyperclip.copy(password)


def generate_password_gui():
    root = Tk()
    root.title("Password Generator")
    root.geometry("270x115")
    root.iconbitmap("pwd.ico")

    password_var = StringVar()

    password_label = Label(root, textvariable=password_var, font=('Anonymous Pro Regular', 13))
    password_label.pack(pady=1)

    generate_password_button = Button(root, text="Generate Password", font=('Anonymous Pro Regular', 10), command=lambda: password_var.set(generate_password()))
    generate_password_button.pack(pady=1)

    generate_country_button = Button(root, text="Generate Country Password", font=('Anonymous Pro Regular', 10), command=lambda: password_var.set(generate_country_password()))
    generate_country_button.pack(pady=1)

    copy_button = Button(root, text="Copy to Clipboard", font=('Anonymous Pro Regular', 10), command=lambda: copy_to_clipboard(password_var))
    copy_button.pack(pady=1)

    root.mainloop()

generate_password_gui()
