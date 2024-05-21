from screeninfo import get_monitors
import customtkinter as ctk


def create_window():
    WIDTH = 600
    HEIGHT = WIDTH - 200

    width = get_monitors()[0].width - WIDTH
    height = get_monitors()[0].height - HEIGHT

    window = ctk.CTk()
    window.title("Task Manager")
    window.geometry(str(width) + "x" + str(height))

    return window
