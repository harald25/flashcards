import customtkinter as ctk


class ChooseActiveUserFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active users")
        self.participants_switches = {}
        self.participants_variables = {}

        # Create participants switches
        for i in range(len(self.controller.model.all_users)):
            user = self.controller.model.all_users[i]
            self.participants_variables[user] = ctk.StringVar(self, f"{user}/0")
            switch = ctk.CTkSwitch(self, text=f"{user}", state="on", offvalue=f"{user}/x",
                                   onvalue=f"{user}/1", variable=self.participants_variables[user],
                                   command=self.update_participating_users)
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            switch.select()
            self.participants_switches[user] = switch

    def update_participating_users(self):
        print("TODO")
        pass