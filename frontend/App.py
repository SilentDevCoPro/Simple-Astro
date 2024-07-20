import customtkinter as ctk
from pages.new_target import New_Target
from pages.simple_astro import Simple_Astro

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, window_title, window_x, window_y):
        super().__init__()
        self.window_title = window_title
        self.window_x = window_x
        self.window_y = window_y
        self.pages = {}
        self.current_page = None
        
    def window_attributes(self):
        self.title(self.window_title)
        self.geometry(f'{self.window_x}x{self.window_y}')
    
    def window_elements(self):
        self.pages["Simple Astro"] = Simple_Astro(self, self.show_page)
        self.pages["New Target"] = New_Target(self)
        self.show_page("Simple Astro") 
        
    def run(self):
        self.window_attributes()
        self.window_elements()
        self.mainloop()

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages[page_name]
        self.current_page.pack(expand=True, fill='both')


def main():
    app = App("Simple Astro", 600, 600)
    app.run()

if __name__ == "__main__":
    main()