import customtkinter as ctk

class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, master=parent)
        self.controller = controller

        # Sets corner radius
        self._corner_radius = 0

        # Configure grid layout
        self.grid_rowconfigure(4, weight=1)

        # Variable to decide if preview card should be shown.
        self.show_preview_card = True

        # Menu header
        label_menu_header = ctk.CTkLabel(self, text="Flashcards 3.0")
        label_menu_header.grid(row=0, column=0, padx=20, pady=(20, 0))

        # Menu header
        label_menu_header = ctk.CTkLabel(self, text="MENU", font=ctk.CTkFont(size=24))
        label_menu_header.grid(row=1, column=0, padx=20, pady=(10, 20))

        # Play button
        button_play = ctk.CTkButton(self, text="Play", command=lambda: controller.show_frame(parent.play_frame))
        button_play.grid(row=2, column=0, padx=20, pady=10)

        # Settings button
        button_settings = ctk.CTkButton(self, text="Settings", command=lambda: controller.show_frame(parent.settings_frame))
        button_settings.grid(row=3, column=0, padx=20, pady=10)

        # Appearance mode option menu
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Dark", "Light"], command=controller.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=20)