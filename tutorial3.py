from tkinter import *
from tkinter import ttk


def hourly_salary(monthly_salary, hours_per_day, days_per_month):
    return monthly_salary / (hours_per_day * days_per_month)

class Hourly_Salary_Program:
    def __init__(self, root):
        self.root = root

    @property
    def window_title(self):
        return "Cálculo de Salário por Hora"

    def _get_main_frame(self):
        main_frame = ttk.Frame(root, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(N, S, W, E))
        return main_frame

    def _root_configure(self, root):
        root.title(self.window_title)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def _setup_variables(self):
        self.salary = StringVar()
        self.hours_per_day = StringVar()
        self.days_per_month = StringVar()
        self.hourly_salary = StringVar()

    def _render_salary(self, main_frame):
        salary_label = ttk.Label(main_frame, text="Seu Salário: ")
        salary_label.grid(column=0, row=0)
        salary_entry = ttk.Entry(main_frame, width=7, textvariable=self.salary)
        salary_entry.grid(column=1, row=0)

    def _render_hours(self, main_frame):
        hours_label = ttk.Label(main_frame, text="Horas trabalhadas por dia: ")
        hours_label.grid(column=0, row=1)
        hours_per_day_entry = ttk.Entry(main_frame, width=7, textvariable=self.hours_per_day)
        hours_per_day_entry.grid(column=1, row=1)

    def _render_days(self, main_frame):
        days_per_month_label = ttk.Label(main_frame, text="Dias trabalhados no mês: ")
        days_per_month_label.grid(column=0, row=2)
        days_per_month_entry = ttk.Entry(main_frame, width=7, textvariable=self.days_per_month)
        days_per_month_entry.grid(column=1, row=2)

    def _render_button(self, main_frame):
        convert_button = ttk.Button(main_frame, text="Calcular", command=self._calculate)
        convert_button.grid(row=3, sticky=(E,W))

    def _render_result(self, main_frame):
        hourly_salary_label = ttk.Label(
            main_frame,
            textvariable=self.hourly_salary
        )
        hourly_salary_label.grid(row=3, column=1, sticky=(E,W))

    def _calculate(self, *args):
        try:
            salary = float(self.salary.get())
            hours_per_day = float(self.hours_per_day.get())
            days_per_month = float(self.days_per_month.get())

            self.hourly_salary.set(
                hourly_salary(
                    salary,
                    hours_per_day,
                    days_per_month
                )
            )
        except ValueError:
            pass
    
    def render(self):
        self._root_configure(self.root)
        self._setup_variables()

        main_frame = self._get_main_frame()

        self._render_salary(main_frame)
        self._render_hours(main_frame)
        self._render_days(main_frame)
        self._render_button(main_frame)
        self._render_result(main_frame)

        for child in main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()

    program_window = Hourly_Salary_Program(root)
    program_window.render()

    root.mainloop()
