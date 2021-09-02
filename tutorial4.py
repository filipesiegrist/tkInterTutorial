from tkinter import *
from tkinter import ttk

root = Tk()

main_frame = ttk.Frame(root)
text_label = ttk.Label(main_frame, text="Minha primeira label")

img = PhotoImage(file="resources/tutorial4.png")
image_label = ttk.Label(main_frame, image=img)

main_frame.grid(row=0, column=0, sticky=(N,S,W,E))
text_label.grid(row=0, column=0)
image_label.grid(row=0, column=1)

root.mainloop()