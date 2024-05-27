import customtkinter as ctk

def create_theme_tab(frame):
    theme_font = ("Helvetica", 40)
    middle_font = ("Helvetica", 20)

    theme_label = ctk.CTkLabel(master=frame, text="Themes", font=theme_font)
    theme_label.pack(pady=20)

    def set_theme(theme):
        ctk.set_appearance_mode(theme)

    light_button = ctk.CTkButton(master=frame, text="Light Theme", font=middle_font, command=lambda: set_theme("light"))
    dark_button = ctk.CTkButton(master=frame, text="Dark Theme", font=middle_font, command=lambda: set_theme("dark"))
    system_button = ctk.CTkButton(master=frame, text="System Theme", font=middle_font, command=lambda: set_theme("system"))

    light_button.pack(pady=10)
    dark_button.pack(pady=10)
    system_button.pack(pady=10)
