import customtkinter as ctk
from frames.list_all_cards_frame import ListAllCardsFrame


class EditCardsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Variables
        self.topic = "All topics"

        # Configure grid layout
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create header label
        self.edit_cards_header_label = ctk.CTkLabel(
            master=self, text="EDIT CARDS", font=ctk.CTkFont(size=18), anchor="center"
        )
        self.edit_cards_header_label.grid(
            row=0, column=0, columnspan=2, padx=0, pady=(20, 30), sticky="ew"
        )

        # Create add card label
        self.add_card_label = ctk.CTkLabel(master=self, text="Add a new card")
        self.add_card_label.grid(row=1, column=0, padx=20, pady=(0, 30), sticky="w")

        # Create add card button
        self.add_card_button = ctk.CTkButton(
            master=self,
            text="Add card",
            width=140,
            command=self.controller.add_card_event,
        )
        self.add_card_button.grid(row=1, column=1, padx=10, pady=(0, 30), sticky="w")

        # Create filter cards label
        self.filter_cards_label = ctk.CTkLabel(
            master=self, text="Filter cards by topic"
        )
        self.filter_cards_label.grid(row=2, column=0, padx=20, pady=0, sticky="w")

        # Create filter cards option menu
        topics = self.controller.model.all_topics
        topics.insert(0, "All topics")
        self.filter_cards_option_menu = ctk.CTkOptionMenu(
            master=self,
            width=260,
            values=topics,
            command=self.controller.filter_cards_by_topic_event,
        )
        self.filter_cards_option_menu.grid(row=2, column=1, padx=10, pady=0, sticky="w")

        # Create list all cards frame
        self.list_all_cards_frame = ListAllCardsFrame(
            parent=self, controller=self.controller, topic=self.topic
        )
        self.list_all_cards_frame.grid(
            row=4, column=0, columnspan=2, padx=20, pady=20, sticky="nsew"
        )
