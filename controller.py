import customtkinter as ctk
from app import App
from flashcards import Flashcards
from frames.card_frame import CardFrame


class Controller():
    def __init__(self):
        # First create the model
        self.model = Flashcards(filename="data.csv")

        # Then create the view, which takes the controller as a parameter
        self.view = App(controller=self)

        # Start view-app main loop
        self.view.mainloop()

        # Variables
        self.open_dialog_window = False

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        self.view.change_appearance_mode_event(new_appearance_mode)

    def show_frame(self, frame):
        """Raises the given frame."""
        frame.tkraise()

    def update_card_frame(self, preview=False):
        """Updates the card frame to show correct values and labels."""
        self.view.play_frame.card_frame.grid_forget()
        self.view.play_frame.card_frame.destroy()
        self.view.play_frame.card_frame = CardFrame(parent=self.view.play_frame, controller=self, preview=preview)
        self.view.play_frame.card_frame.grid(row=1, column=1, padx=100, pady=0, sticky="nsew")

    def update_play_frame(self):
        print("TODO!!!")
        # TODO
        pass

    def next_card_button_event(self):
        # TODO

        # Check if showing card or preview
        if not self.view.play_frame.card_frame.preview:

            # Give points
            answer = self.view.play_frame.correct_segbuttons.get()
            if answer == "Correct":
                self.model.add_attempt_to_card(self.model.current_card, True)
            elif answer == "Wrong":
                self.model.add_attempt_to_card(self.model.current_card, False)

        # Draw new card
        self.model.draw_card()

        # Update card_frame
        self.update_card_frame(preview=False)

        # Update next player label
        self.view.play_frame.next_user_label.configure(text=f"The next to answer is {self.model.active_users[0]}.")


    def randomness_slider_event(self, value):
        value = round(value)

        # Update label
        self.view.play_frame.randomness_label_mid.configure(text=f"Degree of randomness: {value}%")

        # Update model
        self.model.degree_of_randomness = value
