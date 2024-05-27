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

    # Create labels for each disk
    row_index = 1
    for i, partition in enumerate(partitions):
        if "rw" in partition.opts:

            disk_name = f"Disk{i}"
            disk_label = ctk.CTkLabel(master=frame, text=disk_name, font=disk_font)
            disk_name_label = ctk.CTkLabel(master=frame, text=f"Name: {partition.device}", font=middle_font)
            disk_capacity_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            used_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            free_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            usage_label = ctk.CTkLabel(master=frame, text="", font=middle_font)
            mount_label = ctk.CTkLabel(master=frame, text="", font=middle_font)

            disk_label.grid(row=row_index, column=i + 5, padx=30, pady=20, sticky="w")
            disk_name_label.grid(row=row_index + 1, column=i + 5, padx=10, pady=20, sticky="w")
            disk_capacity_label.grid(row=row_index + 2, column=i + 5, padx=10, pady=20, sticky="w")
            used_label.grid(row=row_index + 3, column=i + 5, padx=10, pady=20, sticky="w")
            free_label.grid(row=row_index + 4, column=i + 5, padx=10, pady=20, sticky="w")
            usage_label.grid(row=row_index + 5, column=i + 5, padx=10, pady=20, sticky="w")
            mount_label.grid(row=row_index + 6, column=i + 5, padx=10, pady=20, sticky="w")

            # Get disk usage statistics
            total, used, free, percent = get_disk_usage(partition.device)

            # Update labels with disk usage information
            disk_capacity_label.configure(text=f"Total: {bytes2human(total)}")
            used_label.configure(text=f"Used: {bytes2human(used)}")
            free_label.configure(text=f"Free: {bytes2human(free)}")
            usage_label.configure(text=f"Usage: {percent}%")
            mount_label.configure(text=f"Mount: {partition.mountpoint}")

