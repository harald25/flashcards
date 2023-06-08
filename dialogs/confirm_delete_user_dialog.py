import customtkinter as ctk

class ConfirmDeleteUserDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, user, *args, **kwargs):
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
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        # Create button YES
        self.yes_button = ctk.CTkButton(self, text="Yes", command=lambda: self.confirm_delete_user_dialog_event(True, self.user))
        self.yes_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Create button NO
        self.no_button = ctk.CTkButton(self, text="Cancel", command=lambda: self.confirm_delete_user_dialog_event(False, self.user))
        self.no_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    def confirm_delete_user_dialog_event(self, input, user):

        # Update variable
        self.controller.open_dialog_window = False

        # Destroy input window
        self.destroy()

        # Remove user from data
        if input is True:
            self.controller.model.remove_user(user)

        # Update settings window?? TODO: Is this working?
        self.controller.view.settings_frame.scrollable_frame_active_users.update_frame()
        