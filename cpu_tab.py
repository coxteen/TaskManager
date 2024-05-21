import create_window as cw
import customtkinter as ctk
import psutil
import cpuinfo

cpu_font = 40
name_font = 26
middle_font = 20
small_font = 16

window = cw.create_window()

cpu_label = ctk.CTkLabel(master=window, text="CPU", font=("Helvetica", cpu_font))
cpu_name_label = ctk.CTkLabel(master=window, text=cpuinfo.get_cpu_info()['brand_raw'], font=("Helvetica", name_font))
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

cpu_label.grid(row=0, column=0, padx=big_padding, pady=big_padding, sticky="w")
cpu_name_label.grid(row=0, column=3, padx=(100, big_padding), pady=big_padding)
utilization_label.grid(row=1, column=0, padx=small_padding, pady=small_padding)
speed_label.grid(row=2, column=0, padx=small_padding, pady=small_padding)
processes_label.grid(row=3, column=0, padx=small_padding, pady=small_padding)
threads_label.grid(row=4, column=0, padx=small_padding, pady=small_padding)
handles_label.grid(row=5, column=0, padx=small_padding, pady=small_padding)
up_time_label.grid(row=6, column=0, padx=small_padding, pady=small_padding)
base_speed_label.grid(row=1, column=1, padx=small_padding, pady=small_padding)
sockets_label.grid(row=2, column=1, padx=small_padding, pady=small_padding)
cores_label.grid(row=3, column=1, padx=small_padding, pady=small_padding)
logica_processors_label.grid(row=4, column=1, padx=small_padding, pady=small_padding)
virtualization_label.grid(row=5, column=1, padx=small_padding, pady=small_padding)
L1_cache_label.grid(row=1, column=2, padx=small_padding, pady=small_padding)
L2_cache_label.grid(row=2, column=2, padx=small_padding, pady=small_padding)
L3_cache_label.grid(row=3, column=2, padx=small_padding, pady=small_padding)

window.mainloop()
