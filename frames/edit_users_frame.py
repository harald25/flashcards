import customtkinter as ctk


class EditUsersFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Edit users")

        # Add user buttons
        self.add_user_buttons()


    def add_user_buttons(self):
        self.edit_user_buttons = {}

        for i in range(len(self.controller.model.all_users) + 1):
            if i < len(self.controller.model.all_users):
                user = self.controller.model.all_users[i]
                row = i + 1

                user_label = ctk.CTkLabel(self, text=user, justify=ctk.LEFT, anchor="w")
                user_label.grid(row=row, column=0, padx=10, pady=(0, 10), sticky="w")

                edit_user_button = ctk.CTkButton(self, text="Edit", width=70,
                                       command=lambda user=user: self.controller.edit_user_event(user))
                edit_user_button.grid(row=row, column=1, padx=0, pady=(0, 10), sticky="e")
                self.edit_user_buttons[user] = edit_user_button


                delete_user_button = ctk.CTkButton(self, text="Delete", width=70, command=lambda user=user: self.controller.open_confirm_delete_user_dialog(user))
                delete_user_button.grid(row=row, column=2, padx=(5, 0), pady=(0, 10), sticky="e")
            else:
                add_user_label = ctk.CTkLabel(self, text="Add new user", text_color="gray", justify=ctk.LEFT, anchor="w")
                add_user_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

                edit_user_button = ctk.CTkButton(self, text="Add", width=70, command=self.controller.add_user_event)
                edit_user_button.grid(row=0, column=1, columnspan=2, padx=0, pady=(0, 10), sticky="e")
