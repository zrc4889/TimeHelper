import threading
import tkinter
from tkinter.messagebox import askretrycancel
from ttkbootstrap import Style
from tkinter import ttk
from tkinter.messagebox import *
import os
import time
import datetime

# from repo "python" to repo "TimeHelper"

def timeclock():
    time_left = 2400
    while time_left > 0:
        # print('倒计时(s):', time_left)
        time.sleep(1)
        time_left = time_left - 1
    # tkinter.messagebox.showwarning(
    #     'Warning', 'The 20-minute usage time has expired, please save your work and leave this computer to rest immediately.')
    os.system("logoff")


def taskkill():
    os.system("taskkill /f /t /im qq.exe")
    os.system("taskkill /f /t /im WeChat.exe")
    os.system("taskkill /f /t /im QQMusic.exe")
    os.system("taskkill /f /t /im mailmaster.exe")


def dos():
    kill = threading.Thread(target=taskkill)
    kill.start()
    timec = threading.Thread(target=timeclock)
    timec.start()


# style = Style(theme='lumen')
# window = style.master
# if datetime.datetime.now().hour == 
n = datetime.datetime.now().hour
if n != 9 or n != 16 or n != 20:
    os.system("logoff")

dos()
# ttk.Button(window, text="Healthy Mode", command=dos, style='success.TButton').pack(
#     side='left', padx=5, pady=10)
# ttk.Button(window, text="Default", command=default, style='success.Outline.TButton').pack(
#     side='left', padx=5, pady=10)
# window.mainloop()
