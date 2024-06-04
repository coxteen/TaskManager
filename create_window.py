from screeninfo import get_monitors
import customtkinter as ctk


def create_window():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    WIDTH = 1366
    HEIGHT = 768

    # width = get_monitors()[0].width - DIFFERENCE
    # height = get_monitors()[0].height - DIFFERENCE

    window = ctk.CTk()
    window.title("Task Manager")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    window.resizable(True, True)

    return window