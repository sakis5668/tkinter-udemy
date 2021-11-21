import tkinter as tk 
from tkinter import ttk 
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
# or : langs_select["selectmode"] = "extended" / counterpart is "browse"

langs_select.pack()

def handle_selection_change(event):
    selected_inidices = langs_select.curselection()
    for i in selected_inidices:
        print(langs_select.get(i))

langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()

