import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.title("Distance converter")

font_size = 15

font.nametofont("TkDefaultFont").configure(size=font_size)

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="feet shown here")

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", font_size))
feet_label = ttk.Label( main, text="Feet:")
feet_display= ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="WE")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="WE")

calc_button.grid(column=0, row=2, columnspan=2, sticky="WE")


for child in main.winfo_children():
    child.grid_configure(padx=font_size, pady=font_size)


root.bind("<Return>", calculate_feet)
root.bind("KP_Enter", calculate_feet)

root.mainloop()
