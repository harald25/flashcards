import customtkinter as ctk
from frames.choose_active_users_frame import ChooseActiveUserFrame
from frames.choose_active_topics_frame import ChooseActiveTopicsFrame
from frames.edit_users_frame import EditUsersFrame
from frames.backups_frame import BackupsFrame

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Configure grid layout
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create scrollable frame for choosing active users
        self.scrollable_frame_active_users = ChooseActiveUserFrame(self, self.controller)
        self.scrollable_frame_active_users.grid(row=0, column=0, padx=(40, 20), pady=(20, 20), sticky="nsew")

        # Create scrollable frame for choosing active topics
        self.scrollable_frame_active_topics = ChooseActiveTopicsFrame(self, self.controller)
        self.scrollable_frame_active_topics.grid(row=0, column=1, padx=(20, 40), pady=(20, 20), sticky="nsew")

        # Create scrollable frame for editing users
        self.scrollable_frame_edit_users = EditUsersFrame(self, self.controller)
        self.scrollable_frame_edit_users.grid(row=1, column=0, padx=(40, 20), pady=(0, 20), sticky="nsew")

        # Configure data frame
        self.configure_data_frame = BackupsFrame(self, self.controller)
        self.configure_data_frame.grid(row=1, column=1, padx=(20, 40), pady=(0, 20), sticky="nsew")


    def update_participating_users(self):
    #     last_deselected_user = ""
    #
    #     # Find last deselected switch
    #     for user in self.participants_variables:
    #         string = self.participants_variables[user].get()
    #         if string[-1] == "x":
    #             last_deselected_user = user
    #             new_string = string[:-1] + "0"
    #             self.participants_variables[user].set(new_string)
    #
    #     # Turn last deselected switch back on if all switches are off
    #     at_least_one = False
    #     for user in self.participants_variables:
    #         if self.participants_variables[user].get()[-1] == "1":
    #             at_least_one = True
    #     if not at_least_one:
    #         self.participants_switches[last_deselected_user].select()
    #
    #     # Update users
    #     for user in self.participants_variables:
    #         if self.participants_variables[user].get().split("/")[1] == "1":
    #             flashcards.add_participant(user)
    #         elif self.participants_variables[user].get().split("/")[1] == "0":
    #             flashcards.remove_participant(user)
        pass

    def update_available_topics(self):
        pass
    #     last_deselected_topic = ""
    #
    #     # Find last deselected switch
    #     for topic in self.topics_variables:
    #         string = self.topics_variables[topic].get()
    #         if string[-1] == "x":
    #             last_deselected_topic = topic
    #             new_string = string[:-1] + "0"
    #             self.topics_variables[topic].set(new_string)
    #
    #     # Turn last deselected switch back on if all switches are off
    #     at_least_one = False
    #     for topic in self.topics_variables:
    #         if self.topics_variables[topic].get().split("/")[1] == "1":
    #             at_least_one = True
    #     if not at_least_one:
    #         self.topics_switches[last_deselected_topic].select()
    #
    #     # Update available
    #     for topic in self.topics_variables:
    #         if self.topics_variables[topic].get().split("/")[1] == "1":
    #             flashcards.add_available_topic(topic)
    #         elif self.topics_variables[topic].get().split("/")[1] == "0":
    #             flashcards.remove_available_topic(topic)