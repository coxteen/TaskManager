from screeninfo import get_monitors
import customtkinter as ctk


def create_window():
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    WIDTH = 1200
    HEIGHT = WIDTH - 600

    width = get_monitors()[0].width - WIDTH
    height = get_monitors()[0].height - HEIGHT

    window = ctk.CTk()
    window.title("Task Manager")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    window.resizable(True, True)

    return window