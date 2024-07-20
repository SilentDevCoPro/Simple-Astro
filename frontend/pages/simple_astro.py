import customtkinter as ctk

class Simple_Astro(ctk.CTkFrame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page_callback = show_page_callback
        self.pack(expand=True, fill='both')

        title_label = ctk.CTkLabel(self, text="Simple Astro", font=("Arial", 50))
        title_label.pack(pady=(30, 50))

        self.create_button("New Target", "New Target")
        self.create_button("Last Targets")
        self.create_button("Settings/Config")
        
    def create_button(self, text, page_name=None):
        button = ctk.CTkButton(
            self, 
            text=text, 
            corner_radius=8,
            fg_color='#C850C0', 
            hover_color='#4158D0',
            width=200,
            height=50,
            command=lambda: self.show_page_callback(page_name) if page_name else None
        )
        button.pack(pady=(10, 30), padx=20, anchor='center')
