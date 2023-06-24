import customtkinter as ctk


class AddCardCialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.all_topics = self.controller.model.all_topics
        if "All topics" in self.all_topics:
            self.all_topics.remove("All topics")
        if "Enter a new topic here..." not in self.all_topics:
            self.all_topics.insert(0, "Enter a new topic here...")

        # Configure window
        self.geometry("500x240")
        self.configure(title="Add a card")

        # Configure grid layout
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.select_topic_label = ctk.CTkLabel(master=self, text="Select a topic, or enter a new topic:")
        self.select_topic_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.select_topic_combobox = ctk.CTkComboBox(master=self, values=self.all_topics, width=260)
        self.select_topic_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.enter_card_text_label = ctk.CTkLabel(master=self, text="Enter the text to be shown on the card:")
        self.enter_card_text_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="w")

        self.enter_card_text_textbox = ctk.CTkTextbox(master=self)
        self.enter_card_text_textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")
        # TODO: Add default text

        self.confirm_add_card_button = ctk.CTkButton(master=self, width=140, text="Add card", command=lambda: self.controller.add_card_dialog_event(self))
        self.confirm_add_card_button.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.cancel_button = ctk.CTkButton(master=self, width=140, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        """
        Select topic, or create new         COMBOBOX
        
        What is the text for the card?
        LARGE TEXTBOX        
        
        """
