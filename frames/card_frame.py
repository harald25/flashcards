import customtkinter as ctk


class CardFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, preview=False):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Text variables
        if preview:
            user_text = f" "
            topic_text = f"Press \"Next card\" to start playing."
            card_text = f"Question will display here"
            score_text = f" "
        else:
            user_text = f"This card is for {controller.model.current_card.user}."
            topic_text = f"Topic: {controller.model.current_card.topic}"
            card_text = f"{controller.model.current_card.text}"
            score_text = f"Score: {controller.model.current_card.get_score_string()}"



        # Configure grid layout
        self.grid_rowconfigure((0, 1, 3), weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # User label
        label_user = ctk.CTkLabel(self, text=user_text, text_color="gray")
        label_user.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

        # Topic label
        label_topic = ctk.CTkLabel(self, text=topic_text, text_color="gray")
        label_topic.grid(row=1, column=0, sticky="nsew")

        # Question label
        label_question = ctk.CTkLabel(self, text=card_text, wraplength=500)
        label_question.grid(row=2, column=0, sticky="nsew")

        # score label
        label_score = ctk.CTkLabel(self, text=score_text, text_color="gray")
        label_score.grid(row=3, column=0, sticky="nsew", pady=(0, 10))