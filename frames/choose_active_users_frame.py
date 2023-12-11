import customtkinter as ctk


class ChooseActiveUserFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active users")
        self.active_users_switches = {}

        self.create_all_switches()

    def create_all_switches(self):
        self.active_users_switches = {}

        for i in range(len(self.controller.model.all_users)):
            user = self.controller.model.all_users[i]
            switch = ctk.CTkSwitch(
                self,
                text=f"{user}",
                state="on",
                command=lambda user=user: self.controller.active_user_switch_event(
                    user
                ),
            )
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            if user in self.controller.model.active_users:
                switch.select()
            self.active_users_switches[user] = switch

    def update_frame(self):
        # TODO: Is this needed? Should it be here?
        for switch in self.active_users_switches:
            switch.grid_forget()
            switch.destroy()
        self.create_all_switches()
