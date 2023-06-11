import customtkinter as ctk


class ChooseActiveTopicsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Choose active topics")
        self.active_topics_switches = {}

        self.create_all_switches()


    def create_all_switches(self):
        # self.active_topics_switches = {}
        # for i in range(len(self.controller.model.all_topics)):
        #     topic = self.controller.model.all_topics[i]
        #     self.active_topics_variables[topic] = ctk.StringVar(self, f"{topic}/0")
        #     switch = ctk.CTkSwitch(self, text=f"{topic}", state="on", offvalue=f"{topic}/x",
        #                            onvalue=f"{topic}/1", variable=self.active_topics_variables[topic],
        #                            command=self.update_active_topics)
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
        #     if topic in self.controller.model.active_topics:
        #         switch.select()
        #     self.active_topics_switches[topic] = switch

        self.active_topics_switches = {}

        for i in range(len(self.controller.model.all_topics)):
            topic = self.controller.model.all_topics[i]
            switch = ctk.CTkSwitch(self, text=f"{topic}", state="on", command=lambda topic=topic: self.controller.active_topic_switch_event(topic))
            switch.grid(row=i, column=0, padx=10, pady=(0, 10), sticky="ew")
            if topic in self.controller.model.active_topics:
                switch.select()
            self.active_topics_switches[topic] = switch

    def update_frame(self):
        # TODO: Is this needed? Should it be here?
        for switch in self.active_topics_switches:
            switch.grid_forget()
            switch.destroy()
        self.create_all_switches()

