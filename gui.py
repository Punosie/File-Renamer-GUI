import tkinter as tk
from tkinter import filedialog, messagebox
from app import rename_file


root = tk.Tk()
root.geometry('500x500')
root.title("File Renamer")


def open_folder_dialog():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if folder_path:
        address_entry.delete(0, tk.END)
        address_entry.insert(0, folder_path)


def on_button_click():
    address_in = address_entry.get()
    reg_in = reg_entry.get()
    # reg_in = escape(reg_in)
    result_message = rename_file(address_in, reg_in)
    messagebox.showinfo("Result", result_message)

# Label
address_label = tk.Label(text='Folder Dir: ', font=('Helvetica', 12))
reg_label = tk.Label(text='Regex: ', font=('Helvetica', 12))

# Entry
address_entry = tk.Entry(root, width=30, font=('Helvetica', 12))
reg_entry = tk.Entry(root, width=30, font=('Helvetica', 12))

# Button 
add_button = tk.Button(root, text="Open Folder", command=open_folder_dialog, font=('Helvetica', 12))
ok_button = tk.Button(root, text="OK", command=on_button_click, font=('Helvetica', 12))

# Packing

address_label.grid(row=0, column=0, pady=10)
address_entry.grid(row=0, column=1, pady=10)

add_button.grid(row=1, column=1, pady=10)

reg_label.grid(row=2, column=0, pady=10)
reg_entry.grid(row=2, column=1, pady=10)

ok_button.grid(row=3, column=1, pady=10)


root.mainloop()