import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")

        frame = MetresToFeet(self, padding=(30,15))
        frame.grid()

        self.bind("<Return>", frame.calculate_feet)
        self.bind("KP_Enter", frame.calculate_feet)


class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Segoe UI", 15))
        feet_label = ttk.Label( self, text="Feet:")
        feet_display= ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        metres_label.grid(column=0, row=0, sticky="W")
        metres_input.grid(column=1, row=0, sticky="WE")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="WE")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="WE")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)




    def calculate_feet(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


root = DistanceConverter()
font.nametofont("TkDefaultFont").configure(size=15)
root.columnconfigure(0, weight=1)
root.mainloop()
