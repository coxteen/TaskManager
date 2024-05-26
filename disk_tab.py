import customtkinter as ctk
import psutil
import time

# Function to get the disk name or manufacturer
def get_disk_name(device):
    """Function to get the disk name or manufacturer."""
    # This might need to be adjusted based on actual disk naming conventions
    return device.split('/')[-1]

def get_physical_disk_capacity():
    """Function to get the total capacity of all physical disks."""
    total_capacity = 0
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if "rw" in partition.opts:
            usage = psutil.disk_usage(partition.mountpoint)
            total_capacity += usage.total
    return total_capacity

# Function to create the disk tab
def create_disk_tab(frame):
    disk_font = ("Helvetica", 40)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    # Creating and placing the labels
    disk_label = ctk.CTkLabel(master=frame, text="Disk", font=disk_font)
    disk_name_label = ctk.CTkLabel(master=frame, text="Name:", font=middle_font)
    disk_capacity_label = ctk.CTkLabel(master=frame, text="Capacity:", font=middle_font)
    read_speed_label = ctk.CTkLabel(master=frame, text="Read Speed:", font=middle_font)
    write_speed_label = ctk.CTkLabel(master=frame, text="Write Speed:", font=middle_font)

    big_padding = 30
    small_padding = 20
    left_padding = 60

    disk_label.grid(row=0, column=0, padx=(left_padding, 0), pady=big_padding, sticky="w")
    disk_name_label.grid(row=1, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    disk_capacity_label.grid(row=2, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    read_speed_label.grid(row=3, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")
    write_speed_label.grid(row=4, column=0, padx=(left_padding, 0), pady=small_padding, sticky="w")

    # Variables to store previous disk I/O counters
    previous_read_bytes = 0
    previous_write_bytes = 0
    previous_time = time.time()

    def update_disk_info():
        nonlocal previous_read_bytes, previous_write_bytes, previous_time

        # Get current time and disk I/O counters
        current_time = time.time()
        io_counters = psutil.disk_io_counters()

        # Calculate the elapsed time
        elapsed_time = current_time - previous_time

        if elapsed_time > 0:
            # Calculate read and write speeds
            read_speed = (io_counters.read_bytes - previous_read_bytes) / (1024 ** 2) / elapsed_time  # MB/s
            write_speed = (io_counters.write_bytes - previous_write_bytes) / (1024 ** 2) / elapsed_time  # MB/s

            # Update previous values for the next calculation
            previous_read_bytes = io_counters.read_bytes
            previous_write_bytes = io_counters.write_bytes
            previous_time = current_time

            # Get total disk capacity
            total_capacity = get_physical_disk_capacity()

            # Update disk information labels
            partitions = psutil.disk_partitions()
            for partition in partitions:
                if "rw" in partition.opts:
                    disk_name = get_disk_name(partition.device)
                    disk_name_label.configure(text=f"Name: {disk_name}")
                    disk_capacity_label.configure(text=f"Capacity: {total_capacity / (1024 ** 3):.2f} GB")
                    read_speed_label.configure(text=f"Read Speed: {read_speed:.2f} MB/s")
                    write_speed_label.configure(text=f"Write Speed: {write_speed:.2f} MB/s")
                    break

        frame.after(1000, update_disk_info)

    update_disk_info()