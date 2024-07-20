import customtkinter as ctk

class New_Target(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="This is new_target").pack(pady=20, padx=20)

        parent.event_manager.subscribe("show_page", self.on_show_page)

    def on_show_page(self, page_name):
        if page_name == "New Target":
            self.pack(expand=True, fill='both')
        else:
            self.pack_forget()