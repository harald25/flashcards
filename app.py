import customtkinter as ctk
from frames.menu_frame import MenuFrame



class App(ctk.CTk):
    def __init__(self, controller, *args, **kwargs):
        super().__init__()

        self.controller = controller
        # # Create a model
        # model = Flashcards(filename="data.csv")

        # configure window
        self.title("Flashcards 3.0")
        self.geometry(f"{980}x{580}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create menu frame
        self.menu_frame = MenuFrame(parent=self, controller=self.controller)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        ctk.set_appearance_mode(new_appearance_mode)

