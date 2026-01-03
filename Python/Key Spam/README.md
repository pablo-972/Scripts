
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