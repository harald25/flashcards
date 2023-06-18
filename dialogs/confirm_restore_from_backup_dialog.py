import customtkinter as ctk


class ConfirmRestoreFromBackupDialog(ctk.CTkToplevel):
    def __init__(self, parent, controller, backup, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure variables
        self.controller = controller
        self.backup = backup
        self.backup_stringrep = self.controller.model.convert_backup_filename_to_datetime(self.backup)
        self.label_text = f"Are you sure that you want do restore the backup\nfrom {self.backup_stringrep}?\n\nThis action can not be undone, and all current,\n and not saved progress will be lost."

        # Configure window
        self.geometry("400x180")
        self.title = f"Confirm restore from backup."

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Create label
        self.label = ctk.CTkLabel(self, text=self.label_text)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20,
                        sticky="nsew")

        # Create button YES
        self.yes_button = ctk.CTkButton(self, text="Yes",
                                        command=lambda: self.controller.restore_from_backup_dialog_event(
                                            backup=backup, input=True,
                                            dialog=self))
        self.yes_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Create button NO
        self.no_button = ctk.CTkButton(self, text="Cancel",
                                       command=lambda: self.controller.restore_from_backup_dialog_event(
                                           backup=backup, input=False,
                                           dialog=self))
        self.no_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
