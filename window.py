from customtkinter import windows
from screeninfo import get_monitors

window = windows.CTk()

WIDTH_CONSTANT = 600
H_CONSTANT = W_CONSTANT - 200

width = get_monitors()[0].width - W_CONSTANT
height = get_monitors()[0].height - H_CONSTANT

window.geometry('{}x{}'.format(width, height))
window.title('Task Manager')

window.mainloop()