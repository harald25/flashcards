import customtkinter as ctk


class ChooseActiveTopicsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active topics")
        self.active_topics_switches = {}
        self.active_topics_variables = {}

        self.create_all_switches()


    def create_all_switches(self):
        self.active_topics_switches = {}
        self.active_topics_variables = {}
        for i in range(len(self.controller.model.all_topics)):
            topic = self.controller.model.all_topics[i]
            self.active_topics_variables[topic] = ctk.StringVar(self, f"{topic}/0")
            switch = ctk.CTkSwitch(self, text=f"{topic}", state="on", offvalue=f"{topic}/x",
                                   onvalue=f"{topic}/1", variable=self.active_topics_variables[topic],
                                   command=self.update_active_topics)
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            if topic in self.controller.model.active_topics:
                switch.select()
            self.active_topics_switches[topic] = switch

    def update_frame(self):
        for switch in self.active_topics_switches:
            switch.grid_forget()
            switch.destroy()
        self.create_all_switches()

    def update_active_topics(self):
        last_deselected_topic = ""

        # Find last deselected switch
        for topic in self.active_topics_variables:
            string = self.active_topics_variables[topic].get()
            if string[-1] == "x":
                last_deselected_topic = topic
                new_string = string[:-1] + "0"
                self.active_topics_variables[topic].set(new_string)

        # Turn last deselected switch back on if all switches are off
        at_least_one = False
        for topic in self.active_topics_variables:
            if self.active_topics_variables[topic].get()[-1] == "1":
                at_least_one = True
        if not at_least_one:
            self.active_topics_switches[last_deselected_topic].select()

        # Update topics
        for topic in self.active_topics_variables:
            if self.active_topics_variables[topic].get().split("/")[1] == "1":
                self.controller.model.add_active_topic(topic)
            elif self.active_topics_variables[topic].get().split("/")[1] == "0":
                self.controller.model.remove_active_topic(topic)

