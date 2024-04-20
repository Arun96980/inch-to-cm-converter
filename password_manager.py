from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import string

def generate_password():
    numbers = [str(i) for i in range(10)]
    c_letters = list(string.ascii_uppercase)
    s_letters = list(string.ascii_lowercase)
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '/', '?']

    c_letter = [choice(c_letters) for i in range(randint(4,5))]
    s_letter = [choice(s_letters) for i in range(randint(4,5))]
    p_number = [choice(numbers) for i in range(randint(2,4))]
    p_symbol = [choice(symbols) for i in range(randint(2,4))]

    p_list = c_letter + s_letter + p_number + p_symbol
    shuffle(p_list)

    password = "".join(p_list)
    password_entry.delete(0, END)  # Clear previous password
    password_entry.insert(0, password)
    pyperclip.copy(password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showinfo("No Password", "No password to copy!")

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please enter the correct info.")
    else:
        isok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")
        if isok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=400, width=600)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=(0, 10))

add_button = Button(text="Add", width=10, command=save)
add_button.grid(row=4, column=1)

copy_button = Button(text="Copy Password", command=copy_password)
copy_button.grid(row=3, column=3)

window.mainloop()
