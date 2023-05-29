import customtkinter as ctk

class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, master=parent)
        self.controller = controller

        # Sets corner radius
        self._corner_radius = 0

        # Configure grid layout
        self.grid_rowconfigure(8, weight=1)

        # Menu header
        label_menu_header = ctk.CTkLabel(self, text="Flashcards")
        label_menu_header.grid(row=0, column=0, padx=20, pady=(20, 0))

        # Menu header
        label_menu_header = ctk.CTkLabel(self, text="MENU", font=ctk.CTkFont(size=24))
        label_menu_header.grid(row=1, column=0, padx=20, pady=(10, 20))

        # Play button
        button_play = ctk.CTkButton(self, text="Play", command=lambda: controller.show_frame(controller.view.play_frame))
        button_play.grid(row=2, column=0, padx=20, pady=10)

        # Settings button
        button_settings = ctk.CTkButton(self, text="Settings", command=lambda: controller.show_frame(controller.view.settings_frame))
        button_settings.grid(row=3, column=0, padx=20, pady=10)

        # Edit cards button
        button_edit_cards = ctk.CTkButton(self, text="Edit cards", state="disabled")
        button_edit_cards.grid(row=4, column=0, padx=20, pady=10)

        # Statistics button
        button_statistics = ctk.CTkButton(self, text="Statistics", state="disabled")
        button_statistics.grid(row=5, column=0, padx=20, pady=10)

        # Appearance mode option menu
        self.optionmenu_appearance_mode = ctk.CTkOptionMenu(self, values=["Dark", "Light"], command=controller.change_appearance_mode_event)
        self.optionmenu_appearance_mode.grid(row=9, column=0, padx=20, pady=20)