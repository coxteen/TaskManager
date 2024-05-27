import customtkinter as ctk
import GPUtil
from threading import Thread
import time

def create_gpu_tab(frame):
    gpu_font = ("Helvetica", 40)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    gpu_label = ctk.CTkLabel(master=frame, text="GPU", font=gpu_font)
    gpu_label.pack(pady=20)

    gpu_name_label = ctk.CTkLabel(master=frame, text="GPU Name: ", font=middle_font)
    gpu_utilization_label = ctk.CTkLabel(master=frame, text="Utilization: ", font=middle_font)
    gpu_temperature_label = ctk.CTkLabel(master=frame, text="Temperature: ", font=middle_font)
    gpu_memory_label = ctk.CTkLabel(master=frame, text="Memory: ", font=middle_font)

    gpu_name_label.pack(pady=10)
    gpu_utilization_label.pack(pady=10)
    gpu_temperature_label.pack(pady=10)
    gpu_memory_label.pack(pady=10)

    def update_gpu_info():
        while True:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                gpu_name_label.configure(text=f"GPU Name: {gpu.name}", font=small_font)
                gpu_utilization_label.configure(text=f"Utilization: {gpu.load * 100:.2f}%", font=small_font)
                gpu_temperature_label.configure(text=f"Temperature: {gpu.temperature}°C", font=small_font)
                gpu_memory_label.configure(text=f"Memory: {gpu.memoryUsed / 1024:.2f} GB / {gpu.memoryTotal / 1024:.2f} GB", font=small_font)
            time.sleep(1)

    Thread(target=update_gpu_info, daemon=True).start()
