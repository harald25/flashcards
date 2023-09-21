# Import necessary libraries
import customtkinter as ctk
import os

# Import view and model
from app import App
from flashcards import Flashcards

# Importing frames
from frames.play_frame import PlayFrame
from frames.card_frame import CardFrame
from frames.settings_frame import SettingsFrame
from frames.list_all_cards_frame import ListAllCardsFrame
from frames.edit_cards_frame import EditCardsFrame

# Importing dialog windows
from dialogs.confirm_delete_user_dialog import ConfirmDeleteUserDialog
from dialogs.confirm_restore_from_backup_dialog import ConfirmRestoreFromBackupDialog
from dialogs.error_dialog import ErrorDialog
from dialogs.confirm_delete_oldest_backup_dialog import ConfirmDeleteOldestBackupDialog
from dialogs.confirm_delete_backup_dialog import ConfirmDeleteBackupDialog
from dialogs.add_card_dialog import AddCardCialog
from dialogs.edit_card_dialog import EditCardCialog
from dialogs.confirm_delete_card_dialog import ConfirmDeleteCardDialog
from dialogs.how_to_use_dialog import HowToUseDialog


class Controller():
    def __init__(self):
        # First create the model
        self.model = Flashcards(filename="data.csv", controller=self)

        # Then create the view, which takes the controller as a parameter
        self.view = App(controller=self)

        # Variables
        self.open_dialog = False

        # Start view-app main loop
        self.view.mainloop()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Changes appearance mode. Possibe values: "dark", "light"."""
        # TODO: Should this be here or in app?
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

    def update_settings_frame(self):
        """Updates the settings frame to show correct values and labels."""
        self.view.settings_frame.grid_forget()
        self.view.settings_frame.destroy()
        self.view.settings_frame = SettingsFrame(parent=self.view, controller=self)
        self.view.settings_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def update_play_frame(self, card_preview=False):
        # TODO: Can I do this without showing for a brief second?
        self.view.play_frame.next_user_label.configure(text=f"The next to answer is {self.model.active_users[0]}.")
        self.update_card_frame(card_preview)

    def update_list_all_cards_frame(self, topic="All topics"):
        self.view.edit_cards_frame.list_all_cards_frame.grid_forget()
        self.view.edit_cards_frame.list_all_cards_frame.destroy()
        self.view.edit_cards_frame.list_all_cards_frame = ListAllCardsFrame(parent=self.view.edit_cards_frame, controller=self, topic=topic)
        self.view.edit_cards_frame.list_all_cards_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

    def update_edit_cards_frame(self):
        self.view.edit_cards_frame.grid_forget()
        self.view.edit_cards_frame.destroy()
        self.view.edit_cards_frame = EditCardsFrame(parent=self.view, controller=self)
        self.view.edit_cards_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


    def next_card_button_event(self):
        # TODO: Anything more to do here, or did i just forget to remove this TODO?

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

        # Update wrong/skip/correct button
        self.view.play_frame.correct_segbuttons.set("Skip")


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

    def edit_user_event(self, user):
        dialog = ctk.CTkInputDialog(text=f"What is the new name of {user}?", title="Edit user")
        new_username = dialog.get_input()

        # Change username
        success = self.model.edit_username(user, new_username)
        if type(success) is str:
            self.raise_error(success)

        # Update frames
        self.update_play_frame(card_preview=True)
        self.update_settings_frame()

    def delete_user_event(self, user: str, input: bool, dialog):

        # Destroy dialog window
        dialog.destroy()

        # Remove user from model
        if input is True:
            if len(self.model.all_users) > 1:
                self.model.remove_user(user)
            else:
                self.raise_error("E-0101")

        # Update model
        self.model.draw_card()

        # Update frames
        self.update_play_frame(card_preview=True)
        self.update_settings_frame()



    def open_confirm_delete_user_dialog(self, user):
        dialog = ConfirmDeleteUserDialog(parent=self.view, controller=self, user=user)
        dialog.wm_transient(self.view)



    def raise_error(self, error_code: str):
        errors = {"E-0000": "Unknown error.",
                  "E-0101": "Cannot delete user. There must be atleast one user in the system at all times. ",
                  "E-0102": "Username is too long. Length of username cannot exceed 25 cahracters.",
                  "E-0103": "Username cannot contain any special characters.",
                  "E-0104": "This username is already in use.",
                  "E-0105": "This user does not exist."}

        if error_code not in errors:
            error_code = "E-0000"
        error_message = errors[error_code]

        error_dialog = ErrorDialog(parent=self.view, controller=self, error_code=error_code, error_message=error_message)
        error_dialog.wm_transient(self.view)

    def close_dialog(self, dialog):
        dialog.destroy()

    def add_user_event(self):
        dialog = ctk.CTkInputDialog(text=f"What is the new name of the new user?", title="Add user")
        new_user = dialog.get_input()
        print(f"New user: {new_user}")

        # Add user to model
        self.model.add_user(new_user)
        print("Added to model")

        # Update frames
        self.update_play_frame(card_preview=True)
        self.update_settings_frame()
        print("Updated")

    def confirm_save_backup_event(self):
        list_of_files = os.listdir("backups")
        if len(list_of_files) >= 10:
            confirm_delete_oldest_backup_dialog = ConfirmDeleteOldestBackupDialog(parent=self.view, controller=self)
            confirm_delete_oldest_backup_dialog.wm_transient(self.view)
        else:
            self.model.save_backup()
            self.update_settings_frame()

    def save_backup_dialog_event(self, input, dialog):
        # Cloase dialog
        dialog.destroy()
        # Save backup
        if input is True:
            self.model.save_backup()
            self.update_settings_frame()

    def delete_backup_event(self, backup):
        # Open confirm dialog
        dialog = ConfirmDeleteBackupDialog(parent=self.view, controller=self, backup=backup)
        dialog.wm_transient(self.view)

    def delete_backup_dialog_event(self, backup, input, dialog):
        # Close dialog window
        dialog.destroy()

        # Delete backup
        if input is True:
            self.model.delete_backup(backup)

        # Update window
        self.update_settings_frame()

    def restore_from_backup_event(self, backup):
        # Open confirm dialog
        dialog = ConfirmRestoreFromBackupDialog(parent=self.view, controller=self, backup=backup)
        dialog.wm_transient(self.view)

    def restore_from_backup_dialog_event(self, backup, input, dialog):
        """Method for handling the events from buttons pressed in the
        restore_from_backup_dialog window."""
        # Close dialog
        dialog.destroy()

        # Restore from backup
        if input is True:
            self.model.restore_from_backup(backup)

        # Update window
        self.update_play_frame()
        self.update_settings_frame()

    def filter_cards_by_topic_event(self, topic="All topics"):
        self.update_list_all_cards_frame(topic)

    def add_card_event(self):
        dialog = AddCardCialog(parent=self.view, controller=self)
        dialog.wm_transient(self.view)

    def add_card_dialog_event(self, dialog):
        new_card_topic = dialog.select_topic_combobox.get()
        new_card_text = dialog.enter_card_text_textbox.get("0.0", "end")[:-1]

        # Check if new card is valid
        if self.model.check_if_new_card_is_valid(new_card_topic, new_card_text) is True:
            dialog.destroy()
            self.model.add_card(new_card_topic, new_card_text)

            # Update frames
            self.update_play_frame()
            self.update_card_frame(preview=True)    # Is this needed?
            self.update_settings_frame()
            self.update_edit_cards_frame()

    def edit_card_text_event(self, old_card_text):
        print(old_card_text)
        dialog = EditCardCialog(parent=self.view, controller=self, old_card_text=old_card_text)
        dialog.wm_transient(self.view)

    def edit_card_text_dialog_event(self, dialog):
        new_card_text = dialog.enter_card_text_textbox.get("0.0", "end-1c")
        old_card_text = dialog.old_card_text

        # Check if new card text is valid
        if self.model.check_if_new_card_text_is_valid(old_card_text, new_card_text) is True:
            # Destroy dialog window
            dialog.destroy()

            # Edit card
            self.model.edit_card(old_card_text, new_card_text)

            # Update frames
            self.update_play_frame()
            self.update_card_frame(preview=True)    # Is this needed?
            self.update_settings_frame()
            self.update_edit_cards_frame()

    def delete_card_event(self, card_text):
        dialog = ConfirmDeleteCardDialog(parent=self.view, controller=self, card_text=card_text)
        dialog.wm_transient(self.view)

    def delete_card_dialog_event(self, dialog):
        """Deletes the card from the model when confirmed by the dialog action."""
        card_to_be_deleted = dialog.card_text
        dialog.destroy()
        self.model.remove_card(card_to_be_deleted)

        # Update frames
        self.update_play_frame()
        self.update_card_frame(preview=True)  # Is this needed?
        self.update_settings_frame()
        self.update_edit_cards_frame()

    def open_how_to_use_dialog(self):
        dialog = HowToUseDialog(parent=self.view, controller=self)
        dialog.wm_transient(self.view)

