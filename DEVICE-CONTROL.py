from os import system as c
import time
import random

# Colour Code
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'

# Banner
def logo():
    c('clear')
    print(f"""{G}
██████╗ ██╗   ██╗███████╗███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
██████╔╝ ╚████╔╝ █████╗  ███████╗█████╗  
██╔═══╝   ╚██╔╝  ██╔══╝  ╚════██║██╔══╝  
██║        ██║   ███████╗███████║███████╗
╚═╝        ╚═╝   ╚══════╝╚══════╝╚══════╝
       {Y}HACKING WORLD - DEVICE MASTER VIP
{A}-------------------------------------------------
""")

# Start Prank
def device_prank():
    logo()
    number = input(f"{C}[+] Enter Target Phone Number: ")

    print(f"\n{Y}[+] Connecting to Device {number}...")
    time.sleep(2)
    print(f"{G}[✓] Connection Successful!")

    print(f"{Y}[+] Verifying Root Permission...")
    time.sleep(2)
    print(f"{G}[X] Root  Found! Magisk Root...")
    time.sleep(3)
    print(f"{G}[✓] Device Rooted Successfully (ROOT)")

    print(f"{Y}[+] Fetching Device Information...\n")
    time.sleep(2)
    
    fake_model = random.choice(['Samsung S23 Ultra','iPhone 14 Pro Max','Redmi Note 12 Pro','Realme GT 6'])
    android_ver = random.choice(['12.0','13.0','14.0','11.0'])
    battery = random.randint(30, 100)
    storage = random.randint(50, 512)
    call_logs = random.randint(100, 500)
    sms_count = random.randint(50, 300)
    gallery_images = random.randint(500, 3000)
    apps_count = random.randint(50, 200)
    location = random.choice(['Dhaka','Chittagong','Sylhet','Mumbai','Delhi','Kolkata'])
    ip = f"192.168.{random.randint(10, 255)}.{random.randint(10, 255)}"

    print(f"{C}Device Model     : {G}{fake_model}")
    print(f"{C}Android Version  : {G}{android_ver}")
    print(f"{C}Battery Level    : {G}{battery}%")
    print(f"{C}Storage Used     : {G}{storage} GB")
    print(f"{C}Call Logs        : {G}{call_logs}")
    print(f"{C}SMS Messages     : {G}{sms_count}")
    print(f"{C}Gallery Images   : {G}{gallery_images}")
    print(f"{C}Installed Apps   : {G}{apps_count}")
    print(f"{C}Location         : {G}{location}")
    print(f"{C}Public IP        : {G}{ip}")
    print(f"{C}Root Permission  : {G}Granted")
    print(f"{C}Microphone Access: {G}ON")
    print(f"{C}Camera Access    : {G}ON")
    print(f"{C}GPS Tracking     : {G}ON\n")

    print(f"{Y}[+] Syncing Real-Time Data Streams...")
    for i in range(1,8):
        print(f"{C}[*] Accessing Module {i}...")
        time.sleep(0.7)

    print(f"\n{G}[✓] Full Control Session Active (Mode)")
    input(f"\n{A}Press Enter To Disconnect...")

# Run Tool
device_prank()