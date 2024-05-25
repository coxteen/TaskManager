import customtkinter as ctk
import psutil

def create_ram_window(frame):

    ram_font = ("Helvetica", 40)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    ram_label = ctk.CTkLabel(master=frame, text="RAM", font=ram_font)
    total_label = ctk.CTkLabel(master=frame, text=f"Total : {psutil.virtual_memory().total / (1024 ** 3):.2f} GB", font=middle_font)
    available_label = ctk.CTkLabel(master=frame, text=f"Available : {psutil.virtual_memory().available / (1024 ** 3):.2f} GB", font=middle_font)
    used_label = ctk.CTkLabel(master=frame, text=f"Used : {psutil.virtual_memory().used / (1024 ** 3):.2f} GB", font=middle_font)
    percent_label = ctk.CTkLabel(master=frame, text=f"Usage : {psutil.virtual_memory().percent}%", font=middle_font)

    big_padding = 30
    small_padding = 20
    left_padding = 60

    ram_label.grid(row=0, column=0, padx=(left_padding, 0), pady=big_padding, sticky="w")
    total_label.grid(row=1, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    available_label.grid(row=2, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    used_label.grid(row=3, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    percent_label.grid(row=4, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")

    def update_ram():
        total_label.configure(text=f"Total : {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
        available_label.configure(text=f"Available : {psutil.virtual_memory().available / (1024 ** 3):.2f} GB")
        used_label.configure(text=f"Used : {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
        percent_label.configure(text=f"Usage : {psutil.virtual_memory().percent}%")

        frame.after(1000, update_ram)

    update_ram()
