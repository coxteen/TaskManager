from customtkinter import windows
from screeninfo import get_monitors

window = windows.CTk()

WIDTH_CONSTANT = 600
HEIGHT_CONSTANT = WIDTH_CONSTANT - 200

width = get_monitors()[0].width - WIDTH_CONSTANT
height = get_monitors()[0].height - HEIGHT_CONSTANT

window.geometry('{}x{}'.format(width, height))
window.title('Task Manager')

window.mainloop()