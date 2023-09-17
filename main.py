import os
import tkinter as tk
from tkinter import Label,filedialog,messagebox,PhotoImage
from encrypter import *

def browse_file():
    filename = filedialog.askopenfilename(title="Select a file")
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, filename)

def encrypt_file():
    filename = file_entry.get()
    if os.path.exists(filename):
        generate_key()
        key = load_key()
        encrypt(filename, key)
        messagebox.showinfo("Encryption", "File encrypted successfully!")
    else:
        messagebox.showerror("Error", f"File '{filename}' not found")

def decrypt_file():
    filename = file_entry.get()
    if os.path.exists(filename):
        key = load_key()
        decrypt(filename, key)
        messagebox.showinfo("Decryption", "File decrypted successfully!")
    else:
        messagebox.showerror("Error", f"File '{filename}' not found")

window = tk.Tk()
window.title("File Encryption/Decryption")
window.geometry("400x250")
window.configure(bg="black")##e3dedc

label = Label(window,text = "File Encrypter and Decrypter",font = ('Serif 20 bold'),fg = "Orange",bg = "black")
label.pack(pady = 10)

file_entry = tk.Entry(window, width=40)
file_entry.place(x = 35,y = 75)

browse_button = tk.Button(window, text="Browse",width = 9, command=browse_file,fg = "Orange",bg = "black")
browse_button.place(x=300,y=75)

encrypt_button = tk.Button(window, text="Encrypt",width = 9, command=encrypt_file,fg = "Orange",bg = "black")
encrypt_button.place(x = 120,y= 110)

decrypt_button = tk.Button(window, text="Decrypt",width = 9, command=decrypt_file,fg = "Orange",bg = "black")
decrypt_button.place(x = 225,y = 110)

stop_button = tk.Button(window, text="Stop",width = 9, command=window.destroy,font = ("Serif 10 bold"),fg = "BLack",bg = "red")
stop_button.place(x = 170 ,y = 150)

window.mainloop()
