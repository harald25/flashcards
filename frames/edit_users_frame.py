import customtkinter as ctk


class EditUsersFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active users")

        # Add user buttons
        self.edit_user_buttons = {}

        for i in range(len(self.controller.model.all_users) + 1):
            if i < len(self.controller.model.all_users):
                user = self.controller.model.all_users[i]
                row = i + 1

                backup_data_label = ctk.CTkLabel(self, text=user, justify=ctk.LEFT, anchor="w")
                backup_data_label.grid(row=row, column=0, padx=10, pady=(0, 10), sticky="w")

                button = ctk.CTkButton(self, text="Edit", width=70,
                                       command=lambda user=user: self.edit_user(user))
                button.grid(row=row, column=1, padx=0, pady=(0, 10), sticky="e")
                self.edit_user_buttons[user] = button


                backup_data_button = ctk.CTkButton(self, text="Delete", width=70,
                                                   command=lambda user=user: self.open_confirm_delete_dialog(user))
                backup_data_button.grid(row=row, column=2, padx=(5, 0), pady=(0, 10), sticky="e")
            else:
                add_user_label = ctk.CTkLabel(self, text="Add new user", text_color="gray",
                                              justify=ctk.LEFT, anchor="w")
                add_user_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

                button = ctk.CTkButton(self, text="Add new user", width=70, command=self.add_user)
                button.grid(row=0, column=1, columnspan=2, padx=0, pady=(0, 10), sticky="ew")

    def edit_user(self, user):
        pass
    #     dialog = ctk.CTkInputDialog(text=f"What is the new name of {user}?", title=f"Edit user: {user}.")
    #     new_username = dialog.get_input()
    #     if new_username != user:
    #         flashcards.edit_user_name(user, new_username)
    #
    #         # Destroy and draw new serttings window
    #         self.controller.re_draw_settings_frame()

    def add_user(self):
        pass
    #     dialog = ctk.CTkInputDialog(text="What is the name of the user you want to add?", title="Add user.")
    #     new_username = dialog.get_input()
    #     flashcards.add_user(new_username)
    #     self.controller.re_draw_settings_frame()

    def open_confirm_delete_dialog(self, user):
        pass
    #     # Open dialog window if not already open.
    #     if self.open_confirm_delete_dialog_exists is False:
    #         self.open_confirm_delete_dialog_exists = True
    #         self.confirm_delete_user_dialog = ConfirmDeleteUserDialog(user=user, parent=self)
    #         self.confirm_delete_user_dialog.wm_transient(self)
    #     else:
    #         self.confirm_delete_user_dialog.focus()
