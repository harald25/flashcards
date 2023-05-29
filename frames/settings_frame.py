import customtkinter as ctk
from frames.choose_active_users_frame import ChooseActiveUserFrame

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

        # Create scrollable frame topics
        self.scrollable_frame_topics = ctk.CTkScrollableFrame(self, label_text="Choose topics")
        self.scrollable_frame_topics.grid(row=0, column=1, padx=(20, 40), pady=(20, 20), sticky="nsew")
        self.scrollable_frame_topics.grid_columnconfigure(0, weight=1)
        self.topics_switches = {}
        self.topics_variables = {}

        # Create topics switches
        for i in range(len(self.controller.model.all_topics)):
            topic = self.controller.model.all_topics[i]
            self.topics_variables[topic] = ctk.StringVar(self, f"{topic}/0")
            switch = ctk.CTkSwitch(self.scrollable_frame_topics, text=f"{topic}", state="on", offvalue=f"{topic}/x", onvalue=f"{topic}/1", variable=self.topics_variables[topic], command=self.update_available_topics)
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            switch.select()
            self.topics_switches[topic] = switch

        # Edit users frame
        self.edit_users_frame = ctk.CTkScrollableFrame(self, label_text="Edit users")
        self.edit_users_frame.grid(row=1, column=0, padx=(40, 20), pady=(0, 20), sticky="nsew")
        self.edit_users_frame.grid_rowconfigure(0, weight=1)
        self.edit_users_frame.grid_columnconfigure(0, weight=1)

        # Add user buttons
        self.edit_user_buttons = {}

        for i in range(len(self.controller.model.all_users) + 1):
            if i < len(self.controller.model.all_users):
                user = self.controller.model.all_users[i]
                row = i+1

                backup_data_label = ctk.CTkLabel(self.edit_users_frame, text=user, justify=ctk.LEFT, anchor="w")
                backup_data_label.grid(row=row, column=0, padx=10, pady=(0, 10), sticky="w")

                button = ctk.CTkButton(self.edit_users_frame, text="Edit", width=70, command=lambda user=user: self.edit_user(user))
                button.grid(row=row, column=1, padx=0, pady=(0, 10), sticky="e")
                self.edit_user_buttons[user] = button

                backup_data_button = ctk.CTkButton(self.edit_users_frame, text="Delete", width=70, command=lambda user=user: self.open_confirm_delete_dialog(user))
                backup_data_button.grid(row=row, column=2, padx=(5, 0), pady=(0, 10), sticky="e")
            else:
                add_user_label = ctk.CTkLabel(self.edit_users_frame, text="Add new user", text_color="gray", justify=ctk.LEFT, anchor="w")
                add_user_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

                button = ctk.CTkButton(self.edit_users_frame, text="Add new user", width=70, command=self.add_user)
                button.grid(row=0, column=1, columnspan=2, padx=0, pady=(0, 10), sticky="ew")

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

    def edit_user(self, user):
    #     dialog = ctk.CTkInputDialog(text=f"What is the new name of {user}?", title=f"Edit user: {user}.")
    #     new_username = dialog.get_input()
    #     if new_username != user:
    #         flashcards.edit_user_name(user, new_username)
    #
    #         # Destroy and draw new serttings window
    #         self.controller.re_draw_settings_frame()
        pass

    def add_user(self):
    #     dialog = ctk.CTkInputDialog(text="What is the name of the user you want to add?", title="Add user.")
    #     new_username = dialog.get_input()
    #     flashcards.add_user(new_username)
    #     self.controller.re_draw_settings_frame()
        pass

    def open_confirm_delete_dialog(self, user):
    #
    #     # Open dialog window if not already open.
    #     if self.open_confirm_delete_dialog_exists is False:
    #         self.open_confirm_delete_dialog_exists = True
    #         self.confirm_delete_user_dialog = ConfirmDeleteUserDialog(user=user, parent=self)
    #         self.confirm_delete_user_dialog.wm_transient(self)
    #     else:
    #         self.confirm_delete_user_dialog.focus()
        pass

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