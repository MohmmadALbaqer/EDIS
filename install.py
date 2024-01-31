import os 
os.system("clear")

print('''
 ___            _          _  _ 
|_ _| _ _   ___| |_  __ _ | || |
 | | | ' \ (_-/|  _|/ _` || || |
|___||_||_|/__/ \__|\__/_||_||_|

''')

libraries_to_install = [
    "colorama",
    "termcolor",
    "wave",
    "numpy",
    "opencv-python",
    "pydub",
    "tk"
]

for library in libraries_to_install:
    os.system(f"pip install {library}")
    os.system("chmod +x * EDISC.py")
    os.system("chmod +x * EDIS.py")
