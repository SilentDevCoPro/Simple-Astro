import customtkinter as ctk
from pages.new_target import New_Target
from pages.simple_astro import Simple_Astro
from pages.settings_config import Settings_Config
from listeners.event_manager import EventManager

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, window_title, window_x, window_y):
        super().__init__()
        self.window_title = window_title
        self.window_x = window_x
        self.window_y = window_y
        self.pages = {}
        self.current_page = None
        self.event_manager = EventManager()
        
    def window_attributes(self):
        self.title(self.window_title)
        self.geometry(f'{self.window_x}x{self.window_y}')
    
    def load_pages(self):
        self.pages["Simple Astro"] = Simple_Astro(self)
        self.pages["New Target"] = New_Target(self)
        self.pages["Settings/Config"] = Settings_Config(self)
        self.show_page("Simple Astro") 
        
    def run(self):
        self.window_attributes()
        self.load_pages()
        self.mainloop()

    def show_page(self, page_name):
        self.event_manager.broadcast("show_page", page_name)

def main():
    app = App("Simple Astro", 600, 600)
    app.run()

if __name__ == "__main__":
    main()