from tkinter import *
from tkinter import ttk


class DemoProgram:
    def __init__(self, root):
        self.root = root
        root.title(self.window_title)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    
    @property
    def window_title(self):
        return "Teste com Indicadores"
    
    def _get_main_frame(self):
        main_frame = ttk.Frame(self.root, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(N, S, W, E))
        return main_frame

    def _render_scale_controller(self, parent_frame):
        scale_controller = ttk.Scale(
            parent_frame,
            variable=self._bar_ind,
            orient=VERTICAL,
            from_=100,
            to=0,
            length=200
        )
        scale_controller.grid(column=0, row=0, padx=5)

    def _render_level_indicator(self, parent_frame):
        level_indicator = ttk.Progressbar(
            parent_frame,
            orient=VERTICAL,
            mode="determinate",
            length=200,
            variable=self._bar_ind
        )
        level_indicator.grid(column=1, row=0, sticky="W E", padx=5)

    def _render_bars_frame(self, main_frame):
        bars_frame = ttk.LabelFrame(main_frame, text="Nível")

        self._render_scale_controller(bars_frame)
        self._render_level_indicator(bars_frame)

        bars_frame.grid(column=0, row=0, sticky="N S E W")

    def _render_spin_box(self, parent_frame):
        spin_box = ttk.Spinbox(
            parent_frame,
            from_=0,
            to=1000,
            textvariable=self._numeric_value
        )
        spin_box.grid(column=0, row=0, padx=5, pady=5, sticky="N S")

    def _render_spin_box_label(self, parent_frame):
        value_label = ttk.Label(
            parent_frame,
            textvariable=self._numeric_value
        )
        value_label.grid(row=1, column=0, padx=5, pady=5, sticky="N S")

    def _render_indicators_frame(self, main_frame):
        indicators_frame = ttk.Frame(main_frame, padding=2)
        self._render_spin_box(indicators_frame)
        self._render_spin_box_label(indicators_frame)
        indicators_frame.grid(column=1, row=0, sticky="N S")

    def _setup_variables(self):
        self._bar_ind = StringVar()
        self._numeric_value = StringVar()

    def _configure_main_frame(self, main_frame):
        main_frame.columnconfigure(0, weight=7)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(0, weight=1)

    def render(self):
        self._setup_variables()

        main_frame = self._get_main_frame()
        self._render_bars_frame(main_frame)
        self._render_indicators_frame(main_frame)

        self._configure_main_frame(main_frame)



if __name__ == "__main__":
    root = Tk()
    demo_window = DemoProgram(root)
    demo_window.render()

    root.mainloop()