import customtkinter as ctk


class ChooseActiveUserFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active users")
        self.active_users_switches = {}
        self.active_users_variables = {}

        self.create_all_switches()


    def create_all_switches(self):
        self.active_users_switches = {}
        self.active_users_variables = {}
        for i in range(len(self.controller.model.all_users)):
            user = self.controller.model.all_users[i]
            self.active_users_variables[user] = ctk.StringVar(self, f"{user}/0")
            switch = ctk.CTkSwitch(self, text=f"{user}", state="on", offvalue=f"{user}/x",
                                   onvalue=f"{user}/1", variable=self.active_users_variables[user],
                                   command=self.update_active_users)
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            if user in self.controller.model.active_users:
                switch.select()
            self.active_users_switches[user] = switch

    def update_frame(self):
        for switch in self.active_users_switches:
            switch.grid_forget()
            switch.destroy()
        self.create_all_switches()


    def update_active_users(self):
        last_deselected_user = ""

        # Find last deselected switch
        for user in self.active_users_variables:
            string = self.active_users_variables[user].get()
            if string[-1] == "x":
                last_deselected_user = user
                new_string = string[:-1] + "0"
                self.active_users_variables[user].set(new_string)

        # Turn last deselected switch back on if all switches are off
        at_least_one = False
        for user in self.active_users_variables:
            if self.active_users_variables[user].get()[-1] == "1":
                at_least_one = True
        if not at_least_one:
            self.active_users_switches[last_deselected_user].select()

        # Update users
        for user in self.active_users_variables:
            if self.active_users_variables[user].get().split("/")[1] == "1":
                self.controller.model.add_active_user(user)
            elif self.active_users_variables[user].get().split("/")[1] == "0":
                self.controller.model.remove_active_user(user)

