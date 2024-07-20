import customtkinter as ctk

class New_Target(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="This is new_target").pack(pady=20, padx=20)
