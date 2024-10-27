
---

# Wi-Fi Spam Script

This script allows you to create multiple Wi-Fi networks using Python and the Scapy library. It leverages Airmon-ng to set the network interface into monitor mode, enabling the creation of fake access points.

## Prerequisites

- **Python**: Make sure you have Python installed on your system.
- **Scapy**: Install the Scapy library by running:

  ```bash
  pip install scapy
  ```

- **Airmon-ng**: You will need Airmon-ng to put your Wi-Fi interface into monitor mode. It is typically included in penetration testing distributions like Kali Linux.

## Setting Up Your Environment

1. **Open your terminal**.
2. **Put your Wi-Fi interface into monitor mode** using Airmon-ng:

   ```bash
   sudo airmon-ng start wlan0
   ```

   (Replace `wlan0` with your actual Wi-Fi interface name.)

3. **Modify the Script**: Before running the script, make sure to change the `interface` variable to your monitor mode interface in the script.

## Script Overview

The script generates random SSIDs for the Wi-Fi networks and allows you to specify the number of threads to execute. Key components include:

- **`generar_codigo(length=8)`**: Generates a random SSID for the access point.
- **`create_wifi()`**: Creates and sends Wi-Fi beacon frames with the random SSID.
- **Threading**: The script uses threading to create multiple networks concurrently.

## Running the Script

- If you are using Kali Linux or a similar environment, you can simply run the script using an IDE like Visual Studio Code, and it should work without any issues.
- If you encounter permission issues, you may need to run the script with `sudo`:

  ```bash
  sudo python your_script_name.py
  ```

- If you cannot run as `sudo`, consider creating a Python virtual environment, installing the required libraries, and then executing the script as `sudo`.

## Important Notes

- **Legal Disclaimer**: Use this script responsibly and ensure you have permission to create fake access points in your environment. Unauthorized use may be illegal.
- **Interface Management**: Make sure to replace the placeholder for the interface in the script with your actual monitor mode interface name.

--- 


---

# Key Spam Script

This script automates keyboard inputs using Python, allowing you to send specific keystrokes and clipboard contents programmatically. It leverages the `keyboard` and `pyautogui` libraries to simulate user input.

## Prerequisites

- **Python**: Ensure that Python is installed on your system.
- **Required Libraries**: Install the necessary libraries by running:

  ```bash
  pip install keyboard pyautogui
  ```

## Script Overview

This script includes several functions to simulate key presses:

- **`send_alt_2()`**: Sends the combination `Alt + 2`.
- **`send_tab()`**: Sends the `Tab` key.
- **`send_ctrl_v()`**: Pastes the clipboard contents using `Ctrl + V`.
- **`send_e()`**: Sends the letter "e".
- **`send()`**: This is the main function that continuously sends keystrokes. Currently, it sends the letter "e," but you can modify this function to send other keys or combine multiple keystrokes as needed.

The script runs in a separate thread, allowing it to continuously send keystrokes until interrupted.

## Running the Script

1. **Run the script**:

   ```bash
   python your_script_name.py
   ```

2. **Control the script**: 
   - Press the **`s`** key at any time to stop the script gracefully.

## Important Notes

- **Permissions**: Depending on your operating system, you may need to run the script with elevated privileges. On Linux, you can use `sudo`:

  ```bash
  sudo python your_script_name.py
  ```
- If you cannot run as `sudo`, consider creating a Python virtual environment, installing the required libraries, and then executing the script as `sudo`.

- **Usage**: This script simulates user input, which may not be appropriate for all applications. Use it responsibly and ensure that it complies with any relevant usage policies.

- **Interruptions**: The script is designed to run in the background and can be stopped at any time by pressing the `s` key.

If you have any questions or need further assistance, feel free to reach out!

--- 

If you have any questions or need further assistance, feel free to reach out!