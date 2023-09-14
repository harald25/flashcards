import customtkinter as ctk


class ConfirmDeleteCardDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, card_text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.card_text = card_text
        self.label_text_1 = f"Are you sure that you want to delete this card?"
        self.label_text_2 = self.card_text
        self.label_text_3 = "This action can not be undone, and all players score on this\nparticular card will be lost."

        # Configure window
        self.geometry("400x220")
        self.title = f"Confirm delete card."

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create label 1
        self.label_1 = ctk.CTkLabel(self, text=self.label_text_1)
        self.label_1.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="nsew")

        # Create label 2
        self.label_2 = ctk.CTkLabel(self, text=self.label_text_2, text_color="gray")
        self.label_2.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")

        # Create label 3
        self.label_3 = ctk.CTkLabel(self, text=self.label_text_3)
        self.label_3.grid(row=2, column=0, columnspan=2, padx=10, sticky="nsew")

        # Create button YES
        self.yes_button = ctk.CTkButton(self, text="Delete", command=lambda: self.controller.delete_card_dialog_event(self))
        self.yes_button.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Create button NO
        self.no_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)
        self.no_button.grid(row=3, column=1, padx=20, pady=20, sticky="nsew")
