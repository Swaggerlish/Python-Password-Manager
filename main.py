from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ---------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for char in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in random.choice(numbers)]
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    data = {
        website:{
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Title", message="Hey you have left some field empty, try again!")
    else:
            try:
                with open("data.json", mode="r") as file:
                    new_data = json.load(file)
                    new_data.update(data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            else:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="file does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{email}\n{password}")
        else:
            messagebox.showinfo(title="Error", message=f"data {website} does not exit")







window = Tk()
window.title("Password  Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=32)
website_input.focus()
website_input.grid(row=1, column=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=52)
email_input.insert(0, "hafeezakindipe@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0,)
password_input = Entry(width=32)
password_input.grid(row=3, column=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2,)
add_button = Button(text="Add", command=save, width=44)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="search", width=15, command=search)
search_button.grid(row=1, column=2)

















window.mainloop()