import customtkinter as ctk


class HowToUseDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller

        # Configure window
        self.geometry("500x240")
        self.configure(title="How to use this app")

        # Configure grid layout
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)



        self.close_dialog_button = ctk.CTkButton(master=self, width=140,
                                           text="Close window!", command=self.destroy)
        self.close_dialog_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")