
---

# App Uninstaller Script for Android

Hi there!

Recently, I watched a video by Stark Privacy (https://www.youtube.com/watch?v=mKgOzjNUJ-I) that demonstrated how to uninstall apps that are normally unremovable, even for developers, to get more privacy and space. I was doing this manually, so I created a script to automate the process.

## Overview

This repository contains two PowerShell scripts (`.ps1` files):
- **`uninstall_apps.ps1`**: A script to uninstall specified apps.
- **`install_apps.ps1`**: A script to reinstall apps if needed.

### Prerequisites

To use these scripts, you will need [ADB (Android Debug Bridge)](https://developer.android.com/tools/releases/platform-tools?hl=es-419). Please install it before proceeding.

### Usage

1. **Download the scripts** and create a list of apps in a text file (e.g., `apps&services.txt`).
2. **Connect your Android device** via USB and enable USB debugging.
3. Open PowerShell and navigate to the folder containing the scripts and the app list.
4. Run the following command to uninstall apps:

   ```powershell
   ./uninstall_apps.ps1 -l apps&services.txt
   ```

### Execution Policy

If you encounter permission issues while running the script, try the following:

1. Run PowerShell as an administrator.
2. Check your current execution policy:

   ```powershell
   Get-ExecutionPolicy
   ```

3. Set the execution policy to `RemoteSigned` or `Unrestricted`:

   ```powershell
   Set-ExecutionPolicy RemoteSigned
   ```

   or

   ```powershell
   Set-ExecutionPolicy Unrestricted
   ```

4. Reset PowerShell.

### Troubleshooting

If something goes wrong, don’t worry! You can run the following command to reinstall the apps:

```powershell
./install_apps.ps1 -l apps&services.txt
```

Afterward, restart your device to ensure all changes take effect.

### Important Note

Be cautious when uninstalling essential packages. If you uninstall a critical package and then reset or power off your device without reinstalling it, you may need to unlock your device using secure boot and perform a factory reset.

### Apps & services

There is a list with some google, microsoft, Samsung apps, etc, that are normally installed by default. If you dont want to uninstall few of them, remove it from the list, on the other hand, if you want to install some packages that dont appear in the list, just add them and execute the script. I will add more apps or services in the future, only I need to check them before including it.

---

Feel free to modify any sections as needed!
