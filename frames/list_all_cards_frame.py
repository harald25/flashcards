import customtkinter as ctk


class ListAllCardsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, topic, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.configure(label_text="Edit cards")

        self.all_cards_dict = self.controller.model.get_dict_of_topics_and_card_texts()
        if topic != "All topics":
            self.all_cards_dict = {topic: self.all_cards_dict[topic]}

        # Add all labels and buttons
        self.add_all_labels_and_buttons()


    def add_all_labels_and_buttons(self):
        """Creates all labels and buttons in this frame."""

        row = 0

        for topic in self.all_cards_dict:

            # Create topic label
            card_text_label = ctk.CTkLabel(master=self, text=topic, text_color="gray")
            card_text_label.grid(row=row, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="w")
            row += 1

            for card_text in self.all_cards_dict[topic]:

                # Create edit buttons
                edit_button = ctk.CTkButton(master=self, text="Edit", width=70, command=lambda card_text=card_text: self.controller.edit_card_text_event(old_card_text=card_text))
                edit_button.grid(row=row, column=0, padx=5, pady=(0, 10), sticky="w")

                # Create delete buttons
                delete_button = ctk.CTkButton(master=self, text="Delete", width=70)
                delete_button.grid(row=row, column=1, padx=5, pady=(0, 10), sticky="w")

                # Create labels
                card_text_label = ctk.CTkLabel(master=self, text=card_text, wraplength=520, anchor="e")
                card_text_label.grid(row=row, column=2, padx=10, pady=(0, 10), sticky="w")
                # TODO: Achor text to the left
                row += 1



        #
        #
        # # Iterate through all cards
        # for i in range(len(self.all_card_texts)):
        #     card_text = self.all_card_texts[i]
        #     row = i
        #
        #     # Create edit buttons
        #     edit_button = ctk.CTkButton(master=self, text="Edit", width=70)
        #     edit_button.grid(row=row, column=0, padx=5, pady=(0, 10), sticky="w")
        #
        #     # Create delete buttons
        #     delete_button = ctk.CTkButton(master=self, text="Delete", width=70)
        #     delete_button.grid(row=row, column=1, padx=5, pady=(0, 10), sticky="w")
        #
        #     # Create labels
        #     card_text_label = ctk.CTkLabel(master=self, text=card_text)
        #     card_text_label.grid(row=row, column=2, padx=10, pady=(0, 10), sticky="w")

