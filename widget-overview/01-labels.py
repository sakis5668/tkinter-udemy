import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

# label = ttk.Label(root, text="Hello World", padding=20)
# label.config(font=("Segoe UI", 20))
# label.pack()

# image = Image.open("logo.png").resize((64,64))
# photo = ImageTk.PhotoImage(image)
# label = ttk.Label(root, text="Image with text", image=photo, padding=5, compound="right")
# label.pack()

greeting = tk.StringVar()

label = ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set("Hello, John!")

root.mainloop()
