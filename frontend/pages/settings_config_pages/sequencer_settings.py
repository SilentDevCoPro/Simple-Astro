import customtkinter as ctk
from components.custom_title_labels import create_custom_title_lable

class Sequencer_Settings(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        create_custom_title_lable(self, 'Sequencer Settings')

        parent.event_manager.subscribe("show_page", self.on_show_page)

    def on_show_page(self, page_name):
        if page_name == "Sequencer Settings":
            self.pack(expand=True, fill='both')
        else:
            self.pack_forget()