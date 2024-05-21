# from customtkinter import windows
# from screeninfo import get_monitors
#
# window = windows.CTk()
#
# WIDTH_CONSTANT = 600
# HEIGHT_CONSTANT = WIDTH_CONSTANT - 200
#
# width = get_monitors()[0].width - WIDTH_CONSTANT
# height = get_monitors()[0].height - HEIGHT_CONSTANT
#
# window.geometry('{}x{}'.format(width, height))
# window.title('Task Manager')
#
# window.mainloop()

import tkinter as tk
from system_info import get_processor_frequency

def create_window():
    root = tk.Tk()
    root.title("Processor Frequency")

    frequency = get_processor_frequency()
    label = tk.Label(root, text=f"Processor Frequency: {frequency:.2f} MHz")
    label.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_window()