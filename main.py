import customtkinter as ctk
from tkinter import ttk
import create_window as cw
from screeninfo import get_monitors
import cpu_tab
# Import other tab modules as needed


def create_tabs(window):
    style = ttk.Style()
    style.theme_create('dark_mode', parent='alt', settings={
        'TNotebook': {
            'configure': {
                'background': '#333333',  # Background color of the tab bar
                'tabmargins': [2, 5, 2, 0],  # Margins: left, top, right, bottom
            }
        },
        'TNotebook.Tab': {
            'configure': {
                'background': '#000000',  # Background color of the tabs
                'foreground': '#FFFFFF',  # Text color of the tabs
                'padding': [50, 5],  # Padding inside the tab
            },
            'map': {
                'background': [('selected', '#333333'), ('active', '#222222')],
                'foreground': [('selected', '#FFFFFF'), ('active', '#FFFFFF')],
            }
        }
    })
    style.theme_use('dark_mode')

    notebook = ttk.Notebook(window, style='TNotebook')
    notebook.pack(expand=True, fill='both')

    # Add CPU tab
    cpu_frame = ctk.CTkFrame(notebook)
    cpu_tab.create_cpu_window(cpu_frame)
    notebook.add(cpu_frame, text='CPU')

    # Add GPU tab
    gpu_frame = ctk.CTkFrame(notebook)
    # Add code to create GPU tab content here
    notebook.add(gpu_frame, text='GPU')

    # Add RAM tab
    ram_frame = ctk.CTkFrame(notebook)
    # Add code to create RAM tab content here
    notebook.add(ram_frame, text='RAM')

    # Add HDD tab
    hdd_frame = ctk.CTkFrame(notebook)
    # Add code to create HDD tab content here
    notebook.add(hdd_frame, text='HDD')

    # Add SSD tab
    ssd_frame = ctk.CTkFrame(notebook)
    # Add code to create SSD tab content here
    notebook.add(ssd_frame, text='SSD')

    return notebook

def main():
    window = cw.create_window()
    create_tabs(window)
    window.mainloop()

if __name__ == "__main__":
    main()
