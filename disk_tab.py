import customtkinter as ctk
import psutil
from psutil._common import bytes2human

def create_disk_tab(frame):
    disk_font = ("Helvetica", 40)
    middle_font = ("Helvetica", 20)
    def get_disk_usage(device):
        usage = psutil.disk_usage(device)
        return (usage.total, usage.used, usage.free, usage.percent)

    partitions = psutil.disk_partitions(all=False)

    row_index = 1
    for i, partition in enumerate(partitions):
            disk_name_label = ctk.CTkLabel(master=frame, text=f"Name: {partition.device}", font=disk_font)
            disk_capacity_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            used_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            free_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            usage_label = ctk.CTkLabel(master=frame, text="", font=middle_font)

            disk_name_label.grid(row=row_index + 1, column=i + 10, padx=50, pady=20, sticky="w")
            disk_capacity_label.grid(row=row_index + 2, column=i + 10, padx=30, pady=20, sticky="w")
            used_label.grid(row=row_index + 3, column=i + 10, padx=50, pady=20, sticky="w")
            free_label.grid(row=row_index + 4, column=i + 10, padx=50, pady=20, sticky="w")
            usage_label.grid(row=row_index + 5, column=i + 10, padx=50, pady=20, sticky="w")

            total, used, free, percent = get_disk_usage(partition.device)

            disk_capacity_label.configure(text=f"Total: {bytes2human(total)}", padx=25, pady=20)
            used_label.configure(text=f"Used: {bytes2human(used)}")
            free_label.configure(text=f"Free: {bytes2human(free)}")
            usage_label.configure(text=f"Usage: {percent}%")
