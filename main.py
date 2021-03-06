from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letter + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="oops", message="please don't leave your field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading from data file
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Write to data.json
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating data.json
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Write to data.json
                json.dump(data, data_file, indent=4)

        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="no file", message="there is file with this name")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="result", message=f"email: {email}\n password:{password}")
        else:
            messagebox.showerror(title="no data", message="no data file with this")
    finally:
        entry_password.delete(0, END)
        entry_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(pady=70, padx=70)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_email = Entry(width=53)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "robel@gmail.com")
entry_password = Entry(width=35)
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate password", command=password_generator)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=45, command=save_data)
button_add.grid(row=4, column=1, columnspan=2)
button_search = Button(text="search", width=14, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
