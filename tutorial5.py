from tkinter import *
from tkinter import ttk

root = Tk()

main_frame = ttk.Frame(root)

green_img = PhotoImage(file="resources/green_button.png")
first_label = ttk.Label(main_frame, text="Botão Verde", image=green_img, compound='image')

reload_img = PhotoImage(file="resources/reload_button.png")
second_label = ttk.Label(main_frame, text="Atualizar", image=reload_img, compound='center')

red_img = PhotoImage(file="resources/red_button.png")
third_label = ttk.Label(main_frame, text="Botão Vermelho", image=red_img, compound='top')

main_frame.grid(column=0, row=0, sticky=(N,S,W,E))
first_label.grid(row=0, column=0)
second_label.grid(row=0, column=1)
third_label.grid(row=0, column=2)

root.mainloop()