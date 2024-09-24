"""due to the acuring of key-state at starting the "anti-virus" may block the installation, 
thus make sure to analyse the code and trust the project"""

import os
from pynput.keyboard import Key, Listener
from threading import *
import pystray
import win32api
from PIL import Image

state_num = win32api.GetKeyState(0x90)
num_flag = state_num & 0x0001 == 1

state_cap = win32api.GetKeyState(0x14)
cap_flag = state_cap == 1
visited = False

class qt:
    def qut(self):
        os.abort()

if cap_flag:
    image_cap = Image.open(f"capon.ico")
else:
    image_cap = Image.open(f"capoff.ico")

if num_flag:
    image_num = Image.open(f"numon.ico")
else:
    image_num = Image.open(f"numoff.ico")

icon_cap = pystray.Icon("GFG", image_cap, menu=pystray.Menu(pystray.MenuItem("stop", qt.qut)))
icon_cap.run_detached()

icon_num = pystray.Icon("GFG", image_num,  menu=pystray.Menu(pystray.MenuItem("stop", qt.qut)))
icon_num.run_detached()


def docap(txt):
    global image_cap, icon_cap
    icon_cap.stop()
    image_cap = Image.open(f"{txt}.ico")
    icon_cap = pystray.Icon("GFG", image_cap, menu=pystray.Menu(pystray.MenuItem("stop", qt.qut)))
    icon_cap._update_icon()
    icon_cap.run_detached()

def donum(txt):
    global image_num, icon_num
    icon_num.stop()
    image_num = Image.open(f"{txt}.ico")
    icon_num = pystray.Icon("GFG", image_num, menu=pystray.Menu(pystray.MenuItem("stop", qt.qut)))
    icon_num._update_icon()
    icon_num.run_detached()


def on_press(key):
    global cap_flag, num_flag, visited
    if not visited:
        visited = True
        if key == Key.caps_lock:
            if not cap_flag:
                cap_flag = True
            else:
                cap_flag = False
                
        elif key == Key.num_lock:
            if not num_flag:
                num_flag = True
            else:
                num_flag = False

def on_release(key):
    global cap_flag, num_flag, visited
    if visited:
        visited = False
        if key == Key.caps_lock:
            if cap_flag:
                Thread(target=docap, args=("capon",)).start()
            else: 
                Thread(target=docap, args=("capoff",)).start()
        elif key == Key.num_lock:
            if num_flag:
                Thread(target=donum, args=("numon",)).start()
            else: 
                Thread(target=donum, args=("numoff",)).start()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
