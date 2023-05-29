import customtkinter as ctk
from app import App
from flashcards import Flashcards


class Controller():
    def __init__(self):
        # First create the model
        self.model = Flashcards(filename="data.csv")

        # Then create the view, which takes the model as a parameter
        self.view = App(controller=self)

        # Start view-app main loop
        self.view.mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        self.view.change_appearance_mode_event(new_appearance_mode)

    def show_frame(self, frame):
        """Raises the given frame."""
        frame.tkraise()

    def update_frame(self):
        """Updates the frame to show correct values and labels."""
        pass