import customtkinter as ctk
from customtkinter import CTk 

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, window_title, window_x, window_y):
        super().__init__()
        self.window_title = window_title
        self.window_x = window_x
        self.window_y = window_y
        
    def window_attributes(self):
        self.title(self.window_title)
        self.geometry(f'{self.window_x}x{self.window_y}')
    
    def window_elements(self):
        menu = Menu(self)
        menu.pack(expand=True, fill="both")
        
    def run(self):
        self.window_attributes()
        self.window_elements()
        self.mainloop()

class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

        title_label = ctk.CTkLabel(self, text="Simple Astro", font=("Arial", 50))
        title_label.pack(pady=(30, 50))

        self.create_button("New Target")
        self.create_button("Last Targets")
        self.create_button("Settings/Config")
        
    def create_button(self, text):
        button = ctk.CTkButton(
            self, 
            text=text, 
            corner_radius=8,
            fg_color='#C850C0', 
            hover_color='#4158D0',
            width=200,
            height=50
        )
        button.pack(pady=(10, 30), padx=20, anchor='center')
        
app = App("Simple Astro", 600, 600)
app.run()
