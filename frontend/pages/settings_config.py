import customtkinter as ctk
from components.custom_button import create_button
from components.custom_title_labels import create_custom_title_lable

class Settings_Config(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        create_custom_title_lable(self, 'Settings/Config')

        create_button(self, "Sequencer", lambda: parent.show_page("Sequencer Settings"))
        create_button(self, "Mount", lambda: parent.show_page("Mount Settings"))
        create_button(self, "Focuser", lambda: parent.show_page("Focuser Settings"))
        create_button(self, "Guider", lambda: parent.show_page("Guider Settings"))
        parent.event_manager.subscribe("show_page", self.on_show_page)

    def on_show_page(self, page_name):
        if page_name == "Settings/Config":
            self.pack(expand=True, fill='both')
        else:
            self.pack_forget()