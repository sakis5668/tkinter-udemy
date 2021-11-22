import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


def greet(*args):
    print(f"Hello, {user_name.get()}!")


root = tk.Tk()
root.resizable(False, False)
root.title()

style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use("clam"))

main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()

greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(row=0, column=2, sticky="EW", padx=10)

root.bind("<Return>", greet)
root.mainloop()