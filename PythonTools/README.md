
---

# MP3 Converter Script

This script allows you to download audio from YouTube videos and convert it to MP3 format using the `yt-dlp` library. It’s a simple and effective way to extract audio for offline listening.

## Prerequisites

- **Python**: Ensure that Python is installed on your system.
- **yt-dlp**: Install the `yt-dlp` library by running:

  ```bash
  pip install yt-dlp
  ```

- **FFmpeg**: You will also need FFmpeg installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html). Make sure to note the installation path.

## Script Overview

This script performs the following tasks:

1. Prompts the user to enter a YouTube link.
2. Downloads the audio in the best quality available.
3. Converts the audio to MP3 format.

### Key Features

- **Customizable Output Directory**: Change the `outtmpl` option in the script to specify where to save the downloaded MP3 files.
- **FFmpeg Integration**: The script uses FFmpeg to handle the audio conversion. Make sure to set the correct path to your FFmpeg installation.

## Running the Script

1. **Modify the Script**: Before running the script, make sure to:
   - Update the `outtmpl` variable with your desired output directory (e.g., `C:\\X\\X\\X\\%(title)s.%(ext)s` for Windows).
   - Update the `ffmpeg_location` variable with the path to your FFmpeg installation.

2. **Run the script**:

   ```bash
   python your_script_name.py
   ```

3. **Input the YouTube link**: When prompted, enter the URL of the YouTube video you wish to download.

## Important Notes

- **Permissions**: Depending on your operating system, you may need to run the script with elevated privileges.
- **Error Handling**: The script includes basic error handling to notify you if the download fails.

If you have any questions or need further assistance, feel free to reach out!

---
