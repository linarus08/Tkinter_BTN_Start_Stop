""" Кнопка старт и стоп выполнения бесконечной функции в Tkinter, без блокировки интерфейса"""
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
import threading

root = ttk.Window(themename="superhero")
root.title("BTN START STOP")
root.geometry("250x200")
running = True

count = 1


def f_start():
    btn_1['state'] = 'disabled'

    def thread_start():
        print("start")
        global running
        if not running:
            running = True
        while running:
            global count
            print(count, end='\r')
            print(count, end='')
            count += 1
            time.sleep(0.2)

    thr = threading.Thread(target=thread_start)
    thr.start()


def f_stop():
    global count
    count = 1
    btn_1['state'] = 'enabled'
    global running
    if running:
        running = False
        print("stop")


btn_1 = ttk.Button(text="Start", command=f_start, bootstyle=SUCCESS)
btn_1.pack(anchor=CENTER, expand=1)
btn_2 = ttk.Button(text="Stop", command=f_stop, bootstyle=(INFO, OUTLINE))
btn_2.pack(anchor=CENTER, expand=2)

if __name__ == '__main__':
    root.mainloop()
