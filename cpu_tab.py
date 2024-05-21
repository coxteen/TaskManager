import customtkinter as ctk
import cpuinfo

def create_cpu_window(frame):
    cpu_font = ("Helvetica", 40)
    name_font = ("Helvetica", 26)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    cpu_label = ctk.CTkLabel(master=frame, text="CPU", font=cpu_font)
    cpu_name_label = ctk.CTkLabel(master=frame, text=cpuinfo.get_cpu_info()['brand_raw'], font=name_font)
    utilization_label = ctk.CTkLabel(master=frame, text="Utilization : ", font=middle_font)
    speed_label = ctk.CTkLabel(master=frame, text="Speed : ", font=middle_font)
    processes_label = ctk.CTkLabel(master=frame, text="Processes : ", font=middle_font)
    threads_label = ctk.CTkLabel(master=frame, text="Threads : ", font=middle_font)
    handles_label = ctk.CTkLabel(master=frame, text="Handles : ", font=middle_font)
    up_time_label = ctk.CTkLabel(master=frame, text="Up time : ", font=middle_font)
    base_speed_label = ctk.CTkLabel(master=frame, text="Base speed : ", font=small_font)
    sockets_label = ctk.CTkLabel(master=frame, text="Sockets : ", font=small_font)
    cores_label = ctk.CTkLabel(master=frame, text="Cores : ", font=small_font)
    logical_processors_label = ctk.CTkLabel(master=frame, text="Logical processors : ", font=small_font)
    virtualization_label = ctk.CTkLabel(master=frame, text="Virtualization : ", font=small_font)
    l1_cache_label = ctk.CTkLabel(master=frame, text="L1 cache : ", font=small_font)
    l2_cache_label = ctk.CTkLabel(master=frame, text="L2 cache : ", font=small_font)
    l3_cache_label = ctk.CTkLabel(master=frame, text="L3 cache : ", font=small_font)

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
    logical_processors_label.grid(row=4, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    virtualization_label.grid(row=5, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    l1_cache_label.grid(row=1, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")
    l2_cache_label.grid(row=2, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")
    l3_cache_label.grid(row=3, column=2, padx=(left_padding, 0), pady=small_padding, sticky="w")