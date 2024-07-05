#!/usr/bin/python3
#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pydub import AudioSegment
import cv2
import numpy as np
import os; os.system('cls' if os.name == 'nt' else 'clear')
import wave
import time
import sys
from termcolor import colored

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m "
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"

def admin():
    try:
        if os.geteuid() != 0:
            sudo = "\033[1;31m" + "sudo" + "\033[0m"
            root = "\033[93;1m" + "root" + "\033[97;1m"
            print(f"{please} {W}please use {root} Type a command {sudo}")
            sys.exit(0)
        else:
            print(f"""
               {B}.{W}                 
              {B}/ \{Y}          
{Y}  _____ ____  {B}| |{Y} ____     
{Y} | ____|  _ \ {B}| |{Y}/ ___|    
{Y} |  _| | | | |{B}|{R}E{B}|{Y}\___ \    
{Y} | |___| |_| |{B}|{R}D{B}|{Y} ___) |   
{Y} |_____|____/ {B}|{R}I{B}|{Y}|____/    
              {B}|{R}S{B}|{Y}          
           {W}~{Y}\==8==/{W}~       
               {R}8{W}           
               {R}0{W}  
{W}[{R}-{G}-{B}-{W}]   - {B}[INSTAGRAM]  {W}: {Y}https://www.instagram.com/r94xs/        {W}[{R}-{G}-{B}-{W}]
{W}[{R}-{G}-{B}-{W}]   - {G}[GitHub]     {W}: {Y}https://www.github.com/MohmmadALbaqer/  {W}[{R}-{G}-{B}-{W}]         
""")
    except Exception as e:
        print(ERROR + str(e))
admin()

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

encode_button = tk.Button(root, text="[Encode Image to Sound]", command=encode_image)
encode_button.pack()

decode_button = tk.Button(root, text="[Decode Sound to Image]", command=decode_sound)
decode_button.pack()

root.mainloop()
