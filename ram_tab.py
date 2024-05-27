import psutil
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    # Graph
    fig, ax = plt.subplots()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().place(x=350, y=150, width=1000, height=300)
    memory_percentages = []

    def update_graph():
        # Append data to lists
        memory_percentages.append(psutil.virtual_memory().percent)

        if len(memory_percentages) > 60:
            del memory_percentages[0]

        # Keep only the last 60 data points
        memory_percentages[:] = memory_percentages[-60:]

        # Clear and redraw the plot
        ax.clear()
        ax.plot(memory_percentages, label='Memory Usage (%)', color='blue')
        ax.set_xlabel('')  # Remove x-axis label
        ax.set_ylabel('Memory Usage (%)')
        ax.set_ylim(0, 100)
        ax.set_xticks([])  # Remove x-axis tick marks
        ax.set_xticklabels([])  # Remove x-axis tick labels
        ax.legend(loc='upper right')
        ax.grid(True)

        canvas.draw()

        frame.after(1000, update_graph)

    def update_ram():
        total_label.configure(text=f"Total : {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
        available_label.configure(text=f"Available : {psutil.virtual_memory().available / (1024 ** 3):.2f} GB")
        used_label.configure(text=f"Used : {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
        percent_label.configure(text=f"Usage : {psutil.virtual_memory().percent}%")

        frame.after(1000, update_ram)

    update_ram()
    update_graph()