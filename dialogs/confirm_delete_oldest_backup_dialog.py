import customtkinter as ctk


class ConfirmDeleteOldestBackupDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.user = user
        self.label_text = f"Are you sure that you want do delete {self.user}?\n\nThis action can not be undone, and all data and\nprogress for the user will be deleted."

        # Configure window
        self.geometry("400x180")
        self.title = f"Confirm delete user: {self.user}."

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create label
        self.label = ctk.CTkLabel(self, text=self.label_text)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20,
                        sticky="nsew")

        # Create button YES
        self.yes_button = ctk.CTkButton(self, text="Yes",
                                        command=lambda: self.controller.delete_user_event(
                                            user=user, input=True,
                                            dialog=self))
        self.yes_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Create button NO
        self.no_button = ctk.CTkButton(self, text="Cancel",
                                       command=lambda: self.controller.delete_user_event(
                                           user=user, input=False,
                                           dialog=self))
        self.no_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
