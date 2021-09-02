from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meter.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_field = ttk.Entry(main_frame, width=7, textvariable=feet)
feet_field.grid(column=2, row=1, sticky=(W, E))

meter = StringVar()
meter_label = ttk.Label(main_frame, textvariable=meter)
meter_label.grid(column=2, row=2, sticky=(W, E))

convert_button = ttk.Button(main_frame, text="Calculate", command=calculate)
convert_button.grid(column=3, row=3, sticky=W)

ttk.Label(main_frame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(main_frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(main_frame, text="meters").grid(column=3, row=2, sticky=W)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_field.focus()

root.bind("<Return>", calculate)

root.mainloop()