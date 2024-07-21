import customtkinter as ctk

def create_button(parent, text, callback) -> ctk.CTkButton:
    button = ctk.CTkButton(
        parent, 
        text=text, 
        corner_radius=8,
        fg_color='#C850C1', 
        hover_color='#415810',
        width=200,
        height=50,
        command=callback
    )
    button.pack(pady=(10, 30), padx=20, anchor='center')
    return button