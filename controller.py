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

    def update_play_frame(self, card_preview=False):
        print("TODO!!!")
        # TODO: Update card frame, update next_to_answer label, update randomness slider starting value
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

    def active_user_switch_event(self, user):

        # check if no button is turned on
        active_users_counter = 0
        for key in self.view.settings_frame.scrollable_frame_active_users.active_users_switches:
            active_users_counter += self.view.settings_frame.scrollable_frame_active_users.active_users_switches[key].get()
        if active_users_counter == 0:
            self.view.settings_frame.scrollable_frame_active_users.active_users_switches[user].select()
            return

        # Add or remove active users
        if self.view.settings_frame.scrollable_frame_active_users.active_users_switches[user].get() == 1:
            self.model.add_active_user(user)
        elif self.view.settings_frame.scrollable_frame_active_users.active_users_switches[user].get() == 0:
            self.model.remove_active_user(user)

    def active_topic_switch_event(self, topic):
        # check if no button is turned on
        active_topics_counter = 0
        for key in self.view.settings_frame.scrollable_frame_active_topics.active_topics_switches:
            active_topics_counter += self.view.settings_frame.scrollable_frame_active_topics.active_topics_switches[key].get()
        if active_topics_counter == 0:
            self.view.settings_frame.scrollable_frame_active_topics.active_topics_switches[topic].select()
            return

        # Add or remove active topics
        if self.view.settings_frame.scrollable_frame_active_topics.active_topics_switches[topic].get() == 1:
            self.model.add_active_topic(topic)
        elif self.view.settings_frame.scrollable_frame_active_topics.active_topics_switches[topic].get() == 0:
            self.model.remove_active_topic(topic)
