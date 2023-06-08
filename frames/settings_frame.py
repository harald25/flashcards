import customtkinter as ctk
from frames.choose_active_users_frame import ChooseActiveUserFrame
from frames.choose_active_topics_frame import ChooseActiveTopicsFrame
from frames.edit_users_frame import EditUsersFrame

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
        # self.edit_users_frame = ctk.CTkScrollableFrame(self, label_text="Edit users")
        # self.edit_users_frame.grid(row=1, column=0, padx=(40, 20), pady=(0, 20), sticky="nsew")
        # self.edit_users_frame.grid_rowconfigure(0, weight=1)
        # self.edit_users_frame.grid_columnconfigure(0, weight=1)
        #
        # # Add user buttons
        # self.edit_user_buttons = {}
        #
        # for i in range(len(self.controller.model.all_users) + 1):
        #     if i < len(self.controller.model.all_users):
        #         user = self.controller.model.all_users[i]
        #         row = i+1
        #
        #         backup_data_label = ctk.CTkLabel(self.edit_users_frame, text=user, justify=ctk.LEFT, anchor="w")
        #         backup_data_label.grid(row=row, column=0, padx=10, pady=(0, 10), sticky="w")
        #
        #         button = ctk.CTkButton(self.edit_users_frame, text="Edit", width=70, command=lambda user=user: self.edit_user(user))
        #         button.grid(row=row, column=1, padx=0, pady=(0, 10), sticky="e")
        #         self.edit_user_buttons[user] = button
        #
        #         backup_data_button = ctk.CTkButton(self.edit_users_frame, text="Delete", width=70, command=lambda user=user: self.open_confirm_delete_dialog(user))
        #         backup_data_button.grid(row=row, column=2, padx=(5, 0), pady=(0, 10), sticky="e")
        #     else:
        #         add_user_label = ctk.CTkLabel(self.edit_users_frame, text="Add new user", text_color="gray", justify=ctk.LEFT, anchor="w")
        #         add_user_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")
        #
        #         button = ctk.CTkButton(self.edit_users_frame, text="Add new user", width=70, command=self.add_user)
        #         button.grid(row=0, column=1, columnspan=2, padx=0, pady=(0, 10), sticky="ew")

        # Configure data frame
        self.configure_data_frame = ctk.CTkScrollableFrame(self, label_text="Configure data")
        self.configure_data_frame.grid(row=1, column=1, padx=(20, 40), pady=(0, 20), sticky="nsew")
        self.configure_data_frame.grid_rowconfigure(0, weight=1)
        self.configure_data_frame.grid_columnconfigure(0, weight=1)

        backup_data_label = ctk.CTkLabel(self.configure_data_frame, text="Backup data", justify=ctk.LEFT, anchor="w")
        backup_data_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

        backup_data_button = ctk.CTkButton(self.configure_data_frame, text="Backup", width=70)
        backup_data_button.grid(row=0, column=1, padx=(5, 0), pady=(0, 10), sticky="e")

        restore_data_label = ctk.CTkLabel(self.configure_data_frame, text=f"Restore data from:", justify=ctk.LEFT, anchor="w")
        restore_data_label.grid(row=1, column=0, padx=10, pady=(0, 0), sticky="w")

        # restore_data_date_label = ctk.CTkLabel(self.configure_data_frame, text=f"{self.controller.model.get_time_last_backup()}", justify=ctk.LEFT, anchor="w")
        # restore_data_date_label.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        restore_data_date_button = ctk.CTkButton(self.configure_data_frame, text="Restore", width=70, command=self.controller.model.restore_from_backup)
        restore_data_date_button.grid(row=2, column=1, padx=(5, 0), pady=(0, 10), sticky="e")







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