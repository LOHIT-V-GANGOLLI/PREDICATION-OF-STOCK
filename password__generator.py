

import random
import string
import tkinter as tk

def password_generator(length):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    password = ''.join(random.choice(letters + digits + punctuation)for i in range(length))
    return password

def generate_password():
    length = int(length_entry.get())
    password = password_generator(length)
    password_label.config(text=password)

def copy_password(a):
    # copy password to clipboard
    password_label.clipboard_clear()
    password_label.clipboard_append(password_label.cget('text'))
    password_label.update()

def save_password(password):
    website = website_entry.get()
    username = username_entry.get()
    with open('passwords.csv', 'a') as f:    #path to file
        f.write(f'{website}, {username}, {password}\n')
        f.close()

        
window = tk.Tk()
# icon
window.iconbitmap('icon.ico')

window.title('Password Manager')
window.geometry('300x300')
# bg color of the window =  white and text color = black
window.configure(background='white')
# input field to enter website
website_label = tk.Label(window, text='Website')
website_label.grid(row=0, column=0)
website_entry = tk.Entry(window)
website_entry.grid(row=0, column=1)
website = website_entry.get()
# text field in the center with title username or email
username_label = tk.Label(window, text='Username/Email')
username_label.grid(row=1, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1)
username = username_entry.get()
length_label = tk.Label(window, text='Length')
length_label.grid(row=2, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=2, column=1)

# button to generate password
generate_button = tk.Button(window, text='Generate Password', command=generate_password)
generate_button.grid(row=4, column=1)
# text field to display generated password
password_label = tk.Label(window, text='Password')
password_label.grid(row=5, column=1)
# button to save the password
save_button = tk.Button(window, text='Save Password', command=lambda: save_password(password_label.cget('text')))
save_button.grid(row=6, column=1)

# copy botton to copy the password
copy_button = tk.Button(window, text='Copy Password', command=lambda: copy_password(password_label.cget('text')))
copy_button.grid(row=7, column=1)

window.mainloop()
# made with ♥ by Athar Mujtaba Wani
