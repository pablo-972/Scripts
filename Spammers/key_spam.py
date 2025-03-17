import keyboard
import threading
import time
import sys
import pyautogui

running = True

class colors:
    RED = "\033[91m"  
    END = "\033[0m"

print(colors.RED+"=======================================================================================================\n"+colors.END)

print(" /\\ \\/ /    /\\  ___\\   /\\ \\_\\ \\      /\\  ___\\   /\\  == \\ /\\  __ \\   /\\ \"-./  \\ ")
print(" \\ \\  _\"-.  \\ \\  __\\   \\ \\____ \\     \\ \\___  \\  \\ \\  _-/ \\ \\  __ \\  \\ \\ \\-./\\ \\ ")
print("  \\ \\_\\ \\_\\  \\ \\_____\\  \\/\\_____\\     \\/\\_____\\  \\ \\_\\    \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\")
print("   \\/_/\\/_/   \\/_____/   \\/_____/      \\/_____/   \\/_/     \\/_/\\/_/   \\/_/  \\/_/ "+colors.END)

print(colors.RED+"\n=======================================================================================================\n"+colors.END)

print("By Sulkaz\n")

# This function send "@"
def send_alt_2():
    pyautogui.hotkey('altright', '2')

# This function is a complement to send_alt_2
def send_tab():
    pyautogui.hotkey('tab')

# This function send whatever you have in your clipboard
def send_ctrl_v():
    pyautogui.hotkey('ctrl', 'v')

def send_e():
    keyboard.press("e")
    time.sleep(0.01)  
    keyboard.release("e")

# This function send the letter "e" non-stop
def send():
    global running
    while running:
        send_e()  
        keyboard.press("enter")
        time.sleep(0.01)  
        keyboard.release("enter")



time.sleep(5)
keyboard_thread = threading.Thread(target=send)
keyboard_thread.start()

# Press "s" repeatedly to stop the thread
while True:
    if keyboard.is_pressed("s"):
        running = False
        keyboard_thread.join()
        sys.exit(1)
