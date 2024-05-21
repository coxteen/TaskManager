import create_window as cw
import customtkinter as ctk
import psutil
import cpuinfo

def create_cpu_window():
    cpu_font = 40
    name_font = 26
    middle_font = 20
    small_font = 16

    window = cw.create_window()

    cpu_label = ctk.CTkLabel(master=window, text="CPU", font=("Helvetica", cpu_font))
    cpu_name_label = ctk.CTkLabel(master=window, text=cpuinfo.get_cpu_info()['brand_raw'],
                                  font=("Helvetica", name_font))
    utilization_label = ctk.CTkLabel(master=window, text="Utilization : ", font=("Helvetica", middle_font))
    speed_label = ctk.CTkLabel(master=window, text="Speed : ", font=("Helvetica", middle_font))
    processes_label = ctk.CTkLabel(master=window, text="Processes : ", font=("Helvetica", middle_font))
    threads_label = ctk.CTkLabel(master=window, text="Threads : ", font=("Helvetica", middle_font))
    handles_label = ctk.CTkLabel(master=window, text="Handles : ", font=("Helvetica", middle_font))
    up_time_label = ctk.CTkLabel(master=window, text="Up time : ", font=("Helvetica", middle_font))
    base_speed_label = ctk.CTkLabel(master=window, text="Base speed : ", font=("Helvetica", small_font))
    sockets_label = ctk.CTkLabel(master=window, text="Sockets : ", font=("Helvetica", small_font))
    cores_label = ctk.CTkLabel(master=window, text="Cores : ", font=("Helvetica", small_font))
    logica_processors_label = ctk.CTkLabel(master=window, text="Logical processors : ", font=("Helvetica", small_font))
    virtualization_label = ctk.CTkLabel(master=window, text="Virtualization : ", font=("Helvetica", small_font))
    L1_cache_label = ctk.CTkLabel(master=window, text="L1 cache : ", font=("Helvetica", small_font))
    L2_cache_label = ctk.CTkLabel(master=window, text="L2 cache : ", font=("Helvetica", small_font))
    L3_cache_label = ctk.CTkLabel(master=window, text="L3 cache : ", font=("Helvetica", small_font))

    big_padding = 30
    small_padding = 20
    fist_column_left_padding = 60
    left_padding = 200

    cpu_label.grid(row=0, column=0, padx=(fist_column_left_padding, 0), pady=big_padding, sticky="w")
    cpu_name_label.grid(row=0, column=2, padx=(10, 0), pady=big_padding, sticky="w")
    utilization_label.grid(row=1, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    speed_label.grid(row=2, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    processes_label.grid(row=3, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    threads_label.grid(row=4, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    handles_label.grid(row=5, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    up_time_label.grid(row=6, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    base_speed_label.grid(row=1, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    sockets_label.grid(row=2, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    cores_label.grid(row=3, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    logica_processors_label.grid(row=4, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    virtualization_label.grid(row=5, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    L1_cache_label.grid(row=1, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")
    L2_cache_label.grid(row=2, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")
    L3_cache_label.grid(row=3, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")

    window.mainloop()