import customtkinter as ctk


class ErrorDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, error_code, error_message, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.error_code = error_code
        self.error_message = error_message

        # Configure window
        self.geometry("400x180")
        self.title = f"Error: {error_code}."

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create error code label
        self.error_code_label = ctk.CTkLabel(self, text=f"Error: {self.error_code}")
        self.error_code_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Create error message label
        self.error_message_label = ctk.CTkLabel(self, text=self.error_message, wraplength=300)
        self.error_message_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Create button OK
        self.yes_button = ctk.CTkButton(self, text="OK", command=lambda: self.controller.close_dialog(self))
        self.yes_button.grid(row=2, column=0, padx=10, pady=10, sticky="ns")
