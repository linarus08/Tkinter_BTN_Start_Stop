""" Кнопка старт и стоп выполнения бесконечной функции в Tkinter, без блокировки интерфейса"""
from tkinter import *
from tkinter import ttk
import time
import threading

root = Tk()
root.title("BTN START STOP")
root.geometry("250x200")
running = True

count = 1


def func_start():
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
            time.sleep(0.5)

    thr = threading.Thread(target=thread_start)
    thr.start()


def func_stop():
    global count
    count = 1
    btn_1['state'] = 'enabled'
    global running
    if running:
        running = False
        print(" stop")


btn_1 = ttk.Button(text="Start", command=func_start)
btn_1.pack(anchor=CENTER, expand=1)
btn_2 = ttk.Button(text="Stop", command=func_stop)
btn_2.pack(anchor=CENTER, expand=2)

if __name__ == '__main__':
    root.mainloop()
