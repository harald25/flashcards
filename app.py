import customtkinter as ctk
from frames.menu_frame import MenuFrame
from frames.play_frame import PlayFrame
from frames.settings_frame import SettingsFrame



class App(ctk.CTk):
    def __init__(self, controller, *args, **kwargs):
        super().__init__()

        self.controller = controller

        # Set appearance mode
        self.change_appearance_mode_event("Dark")

        # configure window
        self.title("Flashcards 3.0")
        self.geometry(f"{980}x{580}")
        # TODO: Stop resizing

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create menu frame
        self.menu_frame = MenuFrame(parent=self, controller=self.controller)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # Create play frame
        self.play_frame = PlayFrame(parent=self, controller=self.controller)
        self.play_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Create setting frame
        self.settings_frame = SettingsFrame(parent=self, controller=self.controller)
        self.settings_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Show frame
        self.controller.show_frame(self.play_frame)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        ctk.set_appearance_mode(new_appearance_mode)

