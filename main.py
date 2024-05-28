import customtkinter as ctk
from tkinter import ttk
import create_window as cw
from screeninfo import get_monitors
import cpu_tab
import gpu_tab
import ram_tab
import disk_tab
import theme_tab
def create_tabs(window):
    style = ttk.Style()
    style.theme_create('dark_mode', parent='alt', settings={
        'TNotebook': {
            'configure': {
                'background': '#333333',
                'tabmargins': [2, 5, 2, 0],
            }
        },
        'TNotebook.Tab': {
            'configure': {
                'background': '#000000',
                'foreground': '#FFFFFF',
                'padding': [50, 5],
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

    cpu_frame = ctk.CTkFrame(notebook)
    cpu_tab.create_cpu_window(cpu_frame)
    notebook.add(cpu_frame, text='CPU')

    gpu_frame = ctk.CTkFrame(notebook)
    gpu_tab.create_gpu_tab(gpu_frame)
    notebook.add(gpu_frame, text='GPU')

    ram_frame = ctk.CTkFrame(notebook)
    ram_tab.create_ram_window(ram_frame)
    notebook.add(ram_frame, text='RAM')

    disk_frame=ctk.CTkFrame(notebook)
    disk_tab.create_disk_tab(disk_frame)
    notebook.add(disk_frame, text='Disk')

    theme_frame = ctk.CTkFrame(notebook)
    theme_tab.create_theme_tab(theme_frame)
    notebook.add(theme_frame, text='Theme')

    return notebook



def main():
    window = cw.create_window()
    create_tabs(window)
    window.mainloop()

if __name__ == "__main__":
    main()
