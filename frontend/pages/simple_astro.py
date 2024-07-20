import customtkinter as ctk
from components.custom_button import create_button
from components.custom_title_labels import create_custom_title_lable

class Simple_Astro(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

        create_custom_title_lable(self, 'Simple Astro')

        create_button(self, "New Target", lambda: parent.show_page("New Target"))
        create_button(self, "Last Targets", lambda: parent.show_page("Last Targets"))
        create_button(self, "Settings/Config", lambda: parent.show_page("Settings/Config"))

        parent.event_manager.subscribe("show_page", self.on_show_page)

    def on_show_page(self, page_name):
        if page_name == "Simple Astro":
            self.pack(expand=True, fill='both')
        else:
            self.pack_forget()