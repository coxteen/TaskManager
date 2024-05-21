from psutil import virtual_memory

print("Poate merge\n")
print(virtual_memory().percent)