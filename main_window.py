# import customtkinter
# from PIL import Image
# import create_window as CW
# import cpu_tab
#
# app = CW.create_window()  # Create CTk window like you do with the Tk window
#
# def delete_frame():
#     for widget in app.winfo_children():
#         widget.destroy()
#
#
# def cpu_button_pressed():
#     print("CPU button pressed\n")
#     delete_frame()
#     cpu_tab.create_cpu_window()
#
#
# def gpu_button_pressed():
#     print("GPU button pressed\n")
#     # Add code to create GPU window or switch to GPU page here
#
# def ram_button_pressed():
#     print("RAM button pressed\n")
#     # Add code to create RAM window or switch to RAM page here
#
# def hdd_button_pressed():
#     print("HDD button pressed\n")
#     # Add code to create HDD window or switch to HDD page here
#
# def ssd_button_pressed():
#     print("SSD button pressed\n")
#     # Add code to create SSD window or switch to SSD page here
#
# # Load the image using PIL
# # button_image_path = "bahoi.jpg"  # Path to your image file
# # button_image = Image.open(button_image_path)
#
# # Convert to ctk
# # ctk_button_image = customtkinter.CTkImage(light_image=button_image, dark_image=button_image)
#
# # Define pady constant
# PADDING_Y = 30
#
# # Buttons
# CPU = customtkinter.CTkButton(
#     master=app,
#     command=cpu_button_pressed,
#     width=80,
#     height=60,
#     text="CPU",  # Set button text
#     font=("CPU", 20)
# )
# CPU.pack(pady=PADDING_Y, anchor='w')  # Align to the left
#
# GPU = customtkinter.CTkButton(
#     master=app,
#     command=gpu_button_pressed,
#     width=80,
#     height=60,
#     text="GPU",  # Set button text
#     font=("GPU", 20)
# )
# GPU.pack(pady=PADDING_Y, anchor='w')  # Align to the left
#
# RAM = customtkinter.CTkButton(
#     master=app,
#     command=ram_button_pressed,
#     width=80,
#     height=60,
#     text="RAM",  # Set button text
#     font=("RAM", 20)
# )
# RAM.pack(pady=PADDING_Y, anchor='w')  # Align to the left
#
# HDD = customtkinter.CTkButton(
#     master=app,
#     command=hdd_button_pressed,
#     width=80,
#     height=60,
#     text="HDD",  # Set button text
#     font=("HDD", 20)
# )
# HDD.pack(pady=PADDING_Y, anchor='w')  # Align to the left
#
# SSD = customtkinter.CTkButton(
#     master=app,
#     command=ssd_button_pressed,
#     width=80,
#     height=60,
#     text="SSD",  # Set button text
#     font=("SSD", 20)
# )
# SSD.pack(pady=PADDING_Y, anchor='w')  # Align to the left
#
# app.mainloop()
