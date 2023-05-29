import customtkinter as ctk
from app import App
from flashcards import Flashcards


class Controller():
    def __init__(self):
        self.view = App(controller=self)
        self.model = Flashcards(filename="data.csv")

        self.view.mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        self.view.change_appearance_mode_event(new_appearance_mode)

