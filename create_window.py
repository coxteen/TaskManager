from screeninfo import get_monitors
import customtkinter as ctk


def create_window():
    WIDTH = 800
    HEIGHT = WIDTH - 400

    width = get_monitors()[0].width - WIDTH
    height = get_monitors()[0].height - HEIGHT

    window = ctk.CTk()
    window.title("Task Manager")
    window.geometry(str(width) + "x" + str(height))

    window.resizable(False, False)

    return window
