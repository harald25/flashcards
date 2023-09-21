import customtkinter as ctk
from frames.card_frame import CardFrame

# TODO: Edit this card button on the current card

class PlayFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=3)

        # Configure headings frame
        self.headings_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.headings_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.headings_frame.grid_columnconfigure(0, weight=1)
        self.headings_frame.grid_rowconfigure(0, weight=1)

        self.header_label = ctk.CTkLabel(self.headings_frame, text="F L A S H C A R D S", font=ctk.CTkFont(size=24))
        self.header_label.grid(row=1, column=0, padx=0, pady=0, sticky="ew")

        self.post_header_label = ctk.CTkLabel(self.headings_frame, text="Study like the champs!", text_color="gray")
        self.post_header_label.grid(row=2, column=0, padx=10, pady=0, sticky="ew")

        self.card_frame = CardFrame(parent=self, controller=self.controller, preview=True)
        self.card_frame.grid(row=1, column=1, padx=100, pady=0, sticky="nsew")

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
        self.buttons_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.correct_button_label = ctk.CTkLabel(self.buttons_frame, text="Did you answer correctly?", text_color="gray")
        self.correct_button_label.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=(10, 0))

        self.correct_segbuttons = ctk.CTkSegmentedButton(self.buttons_frame, width=260, dynamic_resizing=False)
        self.correct_segbuttons.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 20))
        self.correct_segbuttons.configure(values=["Wrong", "Skip", "Correct"])
        self.correct_segbuttons.set("Skip")

        self.next_user_label = ctk.CTkLabel(self.buttons_frame, text=f"The next to answer is {self.controller.model.active_users[0]}.", text_color="gray")
        self.next_user_label.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=20, pady=(0, 0))

        next_button = ctk.CTkButton(self.buttons_frame, text="Next card", width=260, round_width_to_even_numbers=False, command=controller.next_card_button_event)
        next_button.grid(row=3, column=0, columnspan=3, padx=20, pady=(0, 20))

        randomness_label_left = ctk.CTkLabel(self.buttons_frame, text="0% (Worst score)", text_color="gray")
        randomness_label_left.grid(row=4, column=0, sticky="w", padx=20, pady=(0, 0))

        self.randomness_label_mid = ctk.CTkLabel(self.buttons_frame, text=f"Degree of randomness: {50}%", text_color="gray", width=200)
        self.randomness_label_mid.grid(row=4, column=1, sticky="nsew", padx=20, pady=(0, 0))

        randomness_label_right = ctk.CTkLabel(self.buttons_frame, text="(Random card) 100%", text_color="gray")
        randomness_label_right.grid(row=4, column=2, sticky="e", padx=20, pady=(0, 0))

        self.randomness_slider = ctk.CTkSlider(self.buttons_frame, to=100, width=260, command=self.controller.randomness_slider_event)
        self.randomness_slider.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=20, pady=(0, 20))
        self.randomness_slider.set(50)
        self.controller.model.degree_of_randomness = 50
