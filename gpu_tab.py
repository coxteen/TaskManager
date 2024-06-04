import customtkinter as ctk
from threading import Thread
import subprocess
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_gpu_info():
    gpu_info = {
        "name": "N/A",
        "utilization": "N/A",
        "temperature": "N/A",
        "memory": "N/A"
    }

    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,utilization.gpu,temperature.gpu,memory.used,memory.total',
             '--format=csv,noheader,nounits'],
            capture_output=True, text=True, check=True)
        output = result.stdout.split('\n')[0].split(', ')

        gpu_info = {
            "name": output[0],
            "utilization": float(output[1]),
            "temperature": float(output[2]),
            "memory_used": float(output[3]) / 1024,
            "memory_total": float(output[4]) / 1024
        }
    except Exception as e:
        print(f"Error getting GPU info: {e}")
        gpu_info["error"] = True

    return gpu_info

def create_gpu_tab(frame):
    gpu_font = ("Helvetica", 40)
    big_font = ("Helvetica", 30)
    middle_font = ("Helvetica", 20)
    small_font = ("Helvetica", 16)

    gpu_label = ctk.CTkLabel(master=frame, text="GPU", font=gpu_font)
    gpu_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    gpu_name_label = ctk.CTkLabel(master=frame, text="N/A", font=big_font)
    gpu_utilization_label = ctk.CTkLabel(master=frame, text="Utilization: N/A", font=middle_font)
    gpu_temperature_label = ctk.CTkLabel(master=frame, text="Temperature: N/A", font=middle_font)
    gpu_memory_label = ctk.CTkLabel(master=frame, text="Memory: N/A", font=middle_font)

    gpu_name_label.grid(row=0, column=2, padx=20, pady=10, sticky="w")
    gpu_utilization_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    gpu_temperature_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    gpu_memory_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    # Graphs
    fig_util, ax_util = plt.subplots(facecolor='#808080', figsize=(10, 6))
    fig_temp, ax_temp = plt.subplots(facecolor='#808080', figsize=(10, 6))

    canvas_util = FigureCanvasTkAgg(fig_util, master=frame)
    canvas_util.get_tk_widget().place(x=500, y=150, width=600, height=450)

    canvas_temp = FigureCanvasTkAgg(fig_temp, master=frame)
    canvas_temp.get_tk_widget().place(x=1100, y=150, width=600, height=450)

    gpu_utilization = []
    gpu_temperature = []

    def update_graphs():
        gpu_info = get_gpu_info()

        if "error" in gpu_info:
            return

        gpu_utilization.append(gpu_info["utilization"])
        gpu_temperature.append(gpu_info["temperature"])

        if len(gpu_utilization) > 60:
            del gpu_utilization[0]
        if len(gpu_temperature) > 60:
            del gpu_temperature[0]

        gpu_utilization[:] = gpu_utilization[-60:]
        gpu_temperature[:] = gpu_temperature[-60:]

        ax_util.clear()
        ax_util.plot(gpu_utilization, label='GPU Utilization (%)', color='orange')
        ax_util.set_xlabel('Time (s)')
        ax_util.set_ylabel('GPU Utilization (%)')
        ax_util.set_ylim(0, 100)
        ax_util.legend(loc='upper right')
        ax_util.grid(True)

        ax_temp.clear()
        ax_temp.plot(gpu_temperature, label='GPU Temperature (°C)', color='red')
        ax_temp.set_xlabel('Time (s)')
        ax_temp.set_ylabel('GPU Temperature (°C)')
        ax_temp.set_ylim(0, 100)
        ax_temp.legend(loc='upper right')
        ax_temp.grid(True)

        canvas_util.draw()
        canvas_temp.draw()

        frame.after(1000, update_graphs)

    def update_gpu_info():
        while True:
            gpu_info = get_gpu_info()

            if "error" in gpu_info:
                gpu_name_label.configure(text="Error: can't get GPU info", font=big_font)
                gpu_utilization_label.configure(text="Utilization: N/A", font=middle_font)
                gpu_temperature_label.configure(text="Temperature: N/A", font=middle_font)
                gpu_memory_label.configure(text="Memory: N/A", font=middle_font)
                return

            gpu_name_label.configure(text=gpu_info['name'], font=big_font)
            gpu_utilization_label.configure(text=f"Utilization: {gpu_info['utilization']}%", font=small_font)
            gpu_temperature_label.configure(text=f"Temperature: {gpu_info['temperature']}°C", font=small_font)
            gpu_memory_label.configure(
                text=f"Memory: {gpu_info['memory_used']:.2f} GB / {gpu_info['memory_total']:.2f} GB", font=small_font)
            time.sleep(1)

    Thread(target=update_gpu_info, daemon=True).start()
    update_graphs()