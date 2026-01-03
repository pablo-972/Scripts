
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