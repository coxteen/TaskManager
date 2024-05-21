from customtkinter import windows
from screeninfo import get_monitors


def create_window():
    WIDTH_CONSTANT = 700
    HEIGHT_CONSTANT = WIDTH_CONSTANT - 200

    width = get_monitors()[0].width - WIDTH_CONSTANT
    height = get_monitors()[0].height - HEIGHT_CONSTANT

    window = windows.CTk()

    window.geometry('{}x{}'.format(width, height))
    window.title('Task Manager')

    window.mainloop()

create_window()
