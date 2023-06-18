import customtkinter as ctk


class BackupsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, controller, *args, ** kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(label_text="Backup your progress")

        self.save_backup_label = ctk.CTkLabel(master=self, text="Save backup", text_color="gray")
        self.save_backup_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

        self.save_backup_button = ctk.CTkButton(master=self, text="Backup", width=70, command=self.controller.confirm_save_backup_event)
        self.save_backup_button.grid(row=0, column=2, padx=0, pady=(0, 10), sticky="e")

        backups = self.controller.model.get_list_of_backups()
        print(backups)
        if len(backups) == 0:
            self.no_backups_label = ctk.CTkLabel(master=self, text="You have no backups saved.")
            self.no_backups_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
        else:
            for i in range(len(backups)):
                backup = backups[i]

                # Create labels
                backup_label = ctk.CTkLabel(master=self, text=self.controller.model.convert_backup_filename_to_datetime(backup))
                backup_label.grid(row=i+1, column=0, padx=10, pady=(0, 10), sticky="w")

                # Create delete buttons
                backup_delete_button = ctk.CTkButton(master=self, text="Delete", width=70, command=lambda backup=backup: self.controller.delete_backup_event(backup))
                backup_delete_button.grid(row=i+1, column=1, padx=0, pady=(0, 10), sticky="e")

                # Create restore buttons
                backup_restore_button = ctk.CTkButton(master=self, text="Restore", width=70, command=lambda backup=backup: self.controller.restore_from_backup_event(backup))
                backup_restore_button.grid(row=i+1, column=2, padx=(5, 0), pady=(0, 10), sticky="e")