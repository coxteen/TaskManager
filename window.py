import customtkinter
from PIL import Image
import create_window as CW

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = CW.create_window()  # Create CTk window like you do with the Tk window
def button_function():
    print("button pressed")

# Load the image using PIL
button_image_path = "bahoi.jpg"  # Path to your image file
button_image = Image.open(button_image_path)

# Convert to ctk
ctk_button_image = customtkinter.CTkImage(light_image=button_image, dark_image=button_image)

# Define pady constant
PADDING_Y = 30

# Buttons
CPU = customtkinter.CTkButton(
    master=app,
    command=button_function,
    width=80,
    height=60,
    text="CPU",  # Set button text
    font=("CPU", 20)
)
CPU.pack(pady=PADDING_Y, anchor='w')  # Align to the left

GPU = customtkinter.CTkButton(
    master=app,
    command=button_function,
    width=80,
    height=60,
    text="GPU",  # Set button text
    font=("GPU", 20)
)
GPU.pack(pady=PADDING_Y, anchor='w')  # Align to the left

RAM = customtkinter.CTkButton(
    master=app,
    command=button_function,
    width=80,
    height=60,
    text="RAM",  # Set button text
    font=("RAM", 20)
)
RAM.pack(pady=PADDING_Y, anchor='w')  # Align to the left

HDD = customtkinter.CTkButton(
    master=app,
    command=button_function,
    width=80,
    height=60,
    text="HDD",  # Set button text
    font=("HDD", 20)
)
HDD.pack(pady=PADDING_Y, anchor='w')  # Align to the left

SSD = customtkinter.CTkButton(
    master=app,
    command=button_function,
    width=80,
    height=60,
    text="SSD",  # Set button text
    font=("SSD", 20)
)
SSD.pack(pady=PADDING_Y, anchor='w')  # Align to the left

app.mainloop()
