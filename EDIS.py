import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pydub import AudioSegment
import cv2
import numpy as np
import os
import wave
import time
import sys
from termcolor import colored
from colorama import Fore, Style, Back, init
os.system("clear")

if os.geteuid() != 0:
    red_sudo = "\033[1;31m" + "sudo" + "\033[0m"
    print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.WHITE}You need to {Fore.YELLOW}run {Fore.WHITE}this program with {red_sudo} Please !.")
    sys.exit(1)

print(f"""
               {Fore.BLUE}.{Style.RESET_ALL}                
              {Fore.BLUE}/ \\{Style.RESET_ALL}
  {Fore.YELLOW}_____ ____  {Fore.BLUE}| |{Style.RESET_ALL} {Fore.YELLOW}____  
 {Fore.YELLOW}| ____|  _ \ {Fore.BLUE}| |{Style.RESET_ALL}{Fore.YELLOW}/ ___| 
 {Fore.YELLOW}|  _| | | | |{Fore.BLUE}|{Fore.RED}E{Fore.BLUE}|{Style.RESET_ALL}{Fore.YELLOW}\___ \ 
 {Fore.YELLOW}| |___| |_| |{Fore.BLUE}|{Fore.RED}D{Fore.BLUE}|{Style.RESET_ALL}{Fore.YELLOW} ___) |
 {Fore.YELLOW}|_____|____/ {Fore.BLUE}|{Fore.RED}I{Fore.BLUE}|{Style.RESET_ALL}{Fore.YELLOW}|____/ 
              {Fore.BLUE}|{Fore.RED}S{Fore.BLUE}|{Style.RESET_ALL}
           {Fore.WHITE}~{Fore.YELLOW}\==8==/{Fore.WHITE}~
               {Fore.RED}8
               0{Style.RESET_ALL}""")

print(f"{Fore.WHITE}{Back.RED} [+] Encryption Decryption and Image Security. {Style.RESET_ALL}")

print(f'''
{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}''')

print(f"{Fore.GREEN}[+]{Fore.WHITE} press {Fore.YELLOW}C+Ctrl {Fore.WHITE}to Exit.{Style.RESET_ALL}")

voice_folder = "voice"
image_folder = "image"
os.makedirs(voice_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

encryption_progress = 0
decryption_progress = 0

encryption_progress_bar = None

decryption_progress_bar = None

root = tk.Tk()
root.title("Secure Tool")

encryption_progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
encryption_progress_bar.pack()

def update_gui_progress():
    global encryption_progress_bar
    global decryption_progress_bar

    if encryption_progress_bar is not None:
        encryption_progress_bar["value"] = encryption_progress
    if decryption_progress_bar is not None:
        decryption_progress_bar["value"] = decryption_progress

    root.after(100, update_gui_progress)

update_gui_progress()

def encode_image():
    global encryption_progress
    encryption_progress = 0

    spin("Encoding Progress ")

    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)

    _, buffer = cv2.imencode('.png', img)
    img_str = buffer.tobytes()

    with wave.open(os.path.join(voice_folder, "encoded_sound.wav"), 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(44100)
        wav_file.writeframes(img_str)

    spin("Encoding Progress", custom_spinner=True)

decryption_progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
decryption_progress_bar.pack()

def decode_sound():
    global decryption_progress
    decryption_progress = 0

    spin("Decoding Progress ")

    file_path = filedialog.askopenfilename()
    sound = AudioSegment.from_wav(file_path)

    decoded_image_array = np.frombuffer(sound.raw_data, dtype=np.uint8)
    decoded_image = cv2.imdecode(decoded_image_array, cv2.IMREAD_UNCHANGED)

    cv2.imwrite(os.path.join(image_folder, "decoded_image.jpg"), decoded_image)

    spin("Decoding Progress", custom_spinner=True)

def spin(progress_desc, custom_spinner=False):
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█'] if custom_spinner else None

    for _ in range(2):
        if custom_spinner:
            for i in spinner:
                message = f"[*] Please wait{progress_desc}...[{i}]"
                colored_message = colored(message, 'blue', attrs=['bold'])
                sys.stdout.write(f"\r{colored_message}   ")
                sys.stdout.flush()
                time.sleep(delay)
        else:
            sys.stdout.write(f"\r[*] Please wait{progress_desc}...   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored(f"[+] {progress_desc} completed.", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(0.5)


encode_button = tk.Button(root, text="[+] Encode Image to Sound", command=encode_image)
encode_button.pack()

decode_button = tk.Button(root, text="[+] Decode Sound to Image", command=decode_sound)
decode_button.pack()

root.mainloop()
