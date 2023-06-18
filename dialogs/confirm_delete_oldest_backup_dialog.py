import customtkinter as ctk


class ConfirmDeleteOldestBackupDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.label_text = "You are only allowed 10 backup files. If you save\nthis backup the oldest backup file will be deleted.\n\nAre you sure you want to continue with the backup?"

        # Configure window
        self.geometry("400x180")
        self.title = f"Confirm delete last backup."

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create label
        self.label = ctk.CTkLabel(self, text=self.label_text)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20,
                        sticky="nsew")

        # Create button YES
        self.yes_button = ctk.CTkButton(self, text="Yes", command=lambda: self.controller.save_backup_dialog_event(input=True, dialog=self))
        self.yes_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Create button NO
        self.no_button = ctk.CTkButton(self, text="Cancel", command=lambda: self.controller.save_backup_dialog_event(input=False, dialog=self))
        self.no_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
