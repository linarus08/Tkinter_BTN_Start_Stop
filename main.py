from tkinter import *
from tkinter import ttk
import time
import threading

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
running = True


def func_1():
    def qwer():
        global running
        if not running:
            running = True
        while running:
            print(5)
            time.sleep(1)

    threading.Thread(target=qwer).start()


def func_2():
    global running
    if running:
        running = False
        print("false")


# th_1 = threading.Thread(target=func_1)
th_2 = threading.Thread(target=func_2)

btn_1 = ttk.Button(text="Click_1", command=func_1)
btn_1.pack(anchor=CENTER, expand=1)
btn_2 = ttk.Button(text="Click_2", command=th_2.start)
btn_2.pack(anchor=CENTER, expand=2)

if __name__ == '__main__':
    root.mainloop()
