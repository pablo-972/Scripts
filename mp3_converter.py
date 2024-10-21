import yt_dlp

#MP3 CONVERTER BY DYGRAL 

class colors:
    PINK = "\033[95m"
    GREEN = "\033[92m"
    END = "\033[0m"
    R_GREEN = "\033[32m"
    R_RED = "\033[31m"

print(colors.PINK+"==================================================================================================================================\n"+colors.END)

print(colors.GREEN+" /$$      /$$ /$$$$$$$   /$$$$$$         /$$$$$$   /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$")
print("| $$$    /$$$| $$__  $$ /$$__  $$       /$$__  $$ /$$__  $$| $$$ | $$| $$   | $$| $$_____/| $$__  $$|__  $$__/| $$_____/| $$__  $$")
print("| $$$$  /$$$$| $$  \\ $$|__/  \\ $$      | $$  \\__/| $$  \\ $$| $$$$| $$| $$   | $$| $$      | $$  \\ $$   | $$   | $$      | $$  \\ $$")
print("| $$ $$/$$ $$| $$$$$$$/   /$$$$$/      | $$      | $$  | $$| $$ $$ $$|  $$ / $$/| $$$$$   | $$$$$$$/   | $$   | $$$$$   | $$$$$$$/")
print("| $$  $$$| $$| $$____/   |___  $$      | $$      | $$  | $$| $$  $$$$ \\  $$ $$/ | $$__/   | $$__  $$   | $$   | $$__/   | $$__  $$")
print("| $$\\  $ | $$| $$       /$$  \\ $$      | $$    $$| $$  | $$| $$\\  $$$  \\  $$$/  | $$      | $$  \\ $$   | $$   | $$      | $$  \\ $$")
print("| $$ \\/  | $$| $$      |  $$$$$$/      |  $$$$$$/|  $$$$$$/| $$ \\  $$   \\  $/   | $$$$$$$$| $$  | $$   | $$   | $$$$$$$$| $$  | $$")
print("|__/     |__/|__/       \\______/        \\______/  \\______/ |__/  \\__/    \\_/    |________/|__/  |__/   |__/   |________/|__/  |__/"+colors.END)

print(colors.PINK+"\n==================================================================================================================================\n"+colors.END)

print("BY DYGRAL\n")

yt_link = input("Enter a youtube link: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '<Change it with your output directory>', # If running in Windows: C:\\X\\X\\X\\%(title)s.%(ext)s this is the format
    'ffmpeg_location': '<Change it with your route to ffmpeg>', # If running in Windows: E:\\ffmpeg\\bin something like that
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_link])

    print (colors.R_GREEN + "\nDOWNLOAD SUCCESS" + colors.END)
except:
    print(colors.R_RED + "\nDOWNLOAD FAILED" + colors.END)


