import customtkinter as ctk


class EditCardCialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, old_card_text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.old_card_text = old_card_text

        # Configure window
        self.geometry("500x240")
        self.configure(title="Edit card")

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.enter_card_text_label = ctk.CTkLabel(master=self,
                                                  text="Enter the text to be shown on the card:")
        self.enter_card_text_label.grid(row=0, column=0, columnspan=2, padx=10,
                                        pady=(10, 0), sticky="w")

        self.enter_card_text_textbox = ctk.CTkTextbox(master=self)
        self.enter_card_text_textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")
        self.enter_card_text_textbox.insert("0.0", self.old_card_text)

        # self.confirm_edit_card_button = ctk.CTkButton(master=self, width=140, text="Edit card")
        # self.confirm_edit_card_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.confirm_edit_card_button = ctk.CTkButton(master=self, width=140, text="Edit card", command=lambda: self.controller.edit_card_text_dialog_event(self))
        self.confirm_edit_card_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.cancel_button = ctk.CTkButton(master=self, width=140, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")


