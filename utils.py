import os
import time
import pyfiglet

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_logo(text, font="doom"):
    print(pyfiglet.figlet_format(text, font=font))

def pause(msg="Press Enter to start..."):
    input(msg)