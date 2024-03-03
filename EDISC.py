import os
import cv2
import numpy as np
from pydub import AudioSegment
import wave
import time
import sys
from termcolor import colored
from colorama import Fore, Style, init, Back
os.system("clear")

init(autoreset=True)

print(f'''{Fore.WHITE}
⠀⠀⢠⡤⢺⣿⣿⣿⣿⣿⣶⣄
⠀⠀⠉⠀⠘⠛⠉⣽⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢉⣿⣿⣿⣿⡗
⠀⢀⣀⡀⢀⣀⣤⣤⣽⣿⣼⣿⢇⡄
⠀⠀{Fore.RED}⠙⠗{Fore.WHITE}⢸⣿⠁{Fore.RED}⠈⠋{Fore.WHITE}⢨⣏⡉⣳
⠀⠀⠀⠀⢸⣿⡄⢠⣴⣿⣿⣿
⠀⠀⠀⠀⠉⣻⣿⣿⣿⣿⣿⡟⡀
⠀⠀⠀⠀⠐⠘⣿⣶⡿⠟⠁⣴⣿⣄
⠀⠀⠀⠀⠀⠘⠛⠉⣠⣴⣾⣿⣿⣿⡦
⠀⠀⢀⣴⣠⣄⠸⠿⣻⣿⣿⣿⣿⠏
⠀⣠⣿⣿⠟⠁{Fore.LIGHTMAGENTA_EX}Version{Fore.WHITE} : {Fore.LIGHTGREEN_EX}1{Fore.BLUE}
░▒█▀▀▀░▒█▀▀▄░▀█▀░▒█▀▀▀█░▒█▀▀▄
░▒█▀▀▀░▒█░▒█░▒█░░░▀▀▀▄▄░▒█░░░
░▒█▄▄▄░▒█▄▄█░▄█▄░▒█▄▄▄█░▒█▄▄▀
{Style.RESET_ALL}''')
print(f'''
 {Fore.RED}+------------------------------------------------------------------+
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
 {Fore.RED}+------------------------------------------------------------------+
{Style.RESET_ALL}''')

print(f"{Fore.WHITE}{Back.RED} [+] Encryption Decryption and Image Security Classic. {Style.RESET_ALL}")

voice_folder = "voice"
image_folder = "image"
os.makedirs(voice_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

encryption_progress = 0
decryption_progress = 0

def update_progress(progress_desc, progress_value):
    sys.stdout.write(f"\r[*] {progress_desc} Progress: {progress_value}%   ")
    sys.stdout.flush()

def encode_image():
    global encryption_progress
    encryption_progress = 0

    update_progress("Encoding", encryption_progress)

    file_path = input(f"{Fore.GREEN}[+] Enter the path of the {Fore.BLUE}image{Fore.GREEN} file: ")
    img = cv2.imread(file_path)

    _, buffer = cv2.imencode('.png', img)
    img_str = buffer.tobytes()

    with wave.open(os.path.join(voice_folder, "encoded_sound.wav"), 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(44100)
        wav_file.writeframes(img_str)

    encryption_progress = 100
    update_progress("Encoding", encryption_progress)
    spin("Encoding Progress", custom_spinner=True)

def decode_sound():
    global decryption_progress
    decryption_progress = 0

    update_progress("Decoding", decryption_progress)

    file_path = input(f"{Fore.GREEN}[+] Enter the path of the {Fore.BLUE}sound{Fore.GREEN} file: ")
    sound = AudioSegment.from_wav(file_path)

    decoded_image_array = np.frombuffer(sound.raw_data, dtype=np.uint8)
    decoded_image = cv2.imdecode(decoded_image_array, cv2.IMREAD_UNCHANGED)

    cv2.imwrite(os.path.join(image_folder, "decoded_image.jpg"), decoded_image)

    decryption_progress = 100
    update_progress("Decoding", decryption_progress)
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

if __name__ == "__main__":
    print(f"{Fore.BLUE}[1] - Encode Image to Sound{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[2] - Decode Sound to Image{Style.RESET_ALL}")

    choice = input(f"{Fore.GREEN}[~] Choose an option {Fore.YELLOW}(1 {Fore.WHITE}or {Fore.YELLOW}2){Fore.WHITE}: {Style.RESET_ALL}")

    if choice == "1":
        encode_image()
    elif choice == "2":
        decode_sound()
    else:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid choice. Please choose 1 or 2.")
