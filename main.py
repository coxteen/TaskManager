import customtkinter as ctk
from tkinter import ttk
import create_window
from PIL import Image
from screeninfo import get_monitors
import cpu_tab
# Import other tab modules as needed

def create_tabs(window):
    # Create a ttk.Notebook widget
    notebook = ttk.Notebook(window)
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
    window = create_window.create_window()
    create_tabs(window)
    window.mainloop()

if __name__ == "__main__":
    main()
