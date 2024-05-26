import customtkinter as ctk
import psutil
import ctypes
import cpuinfo


def create_cpu_window(frame):

    cpu_font = ("Helvetica", 40)
    name_font = ("Helvetica", 26)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    cpu_label = ctk.CTkLabel(master=frame, text="CPU", font=cpu_font)
    cpu_name_label = ctk.CTkLabel(master=frame, text=cpuinfo.get_cpu_info()['brand_raw'], font=name_font)
    utilization_label = ctk.CTkLabel(master=frame, text=f"Utilization : {psutil.cpu_percent()}%", font=middle_font)
    speed_label = ctk.CTkLabel(master=frame, text=f"Speed : {psutil.cpu_freq()}", font=middle_font)
    processes_label = ctk.CTkLabel(master=frame, text=f"Processes : {psutil.cpu_count()}", font=middle_font)
    base_speed_label = ctk.CTkLabel(master=frame, text="Base speed : ", font=small_font)
    cores_label = ctk.CTkLabel(master=frame, text="Cores : ", font=small_font)
    logical_processors_label = ctk.CTkLabel(master=frame, text="Logical processors : ", font=small_font)
    up_time_label = ctk.CTkLabel(master=frame, text="Up time : ", font=middle_font)

    big_padding = 30
    small_padding = 20
    fist_column_left_padding = 60
    left_padding = 200

    cpu_label.grid(row=0, column=0, padx=(fist_column_left_padding, 0), pady=big_padding, sticky="w")
    cpu_name_label.grid(row=0, column=1, padx=(10, 0), pady=big_padding, sticky="w")
    utilization_label.grid(row=1, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    speed_label.grid(row=2, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    processes_label.grid(row=3, column=0, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")
    base_speed_label.grid(row=1, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    cores_label.grid(row=2, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    logical_processors_label.grid(row=3, column=1, padx=(left_padding, 0), pady=small_padding, sticky="w")
    up_time_label.grid(row=1, column=2, padx=(fist_column_left_padding, 0), pady=small_padding, sticky="w")

    def count_processes():
        sum = 0
        for process in psutil.process_iter():
            sum += 1
        return sum


    def update_utilization():

        utilization_label.configure(text=f"Utilization : {psutil.cpu_percent()}%")
        speed_label.configure(text=f"Speed : {psutil.cpu_freq().current} MHz")
        processes_label.configure(text=f"Processes : {count_processes()}")
        t = int(str(ctypes.windll.kernel32.GetTickCount64())[:-3])
        mins, sec = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        up_time_label.configure(text=f"Up time : {days}d {hours}h {mins}m {sec}s")
        base_speed_label.configure(text=f"Base speed : {psutil.cpu_freq().max/ 1000} GHz")
        cores_label.configure(text=f"Cores : {psutil.cpu_count(logical=False)}")
        logical_processors_label.configure(text=f"Logical processors : {psutil.cpu_count(logical=True)}")

        frame.after(1000, update_utilization)

    update_utilization()
