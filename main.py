# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import math
import random
import time
from time import strftime
import datetime
from tkinter import *

# GUI Setup
def show_gui():
    root = Tk()
    root.title("PyAutoClicker")
    root.resizable(width = False, height = False)
    root.minsize(width = 300, height = 150)

    label0 = Label(root, text = "Please only select ONE mode.")
    mode_1_var = IntVar()
    check_box1 = Checkbutton(root, text = "Mode 1: Click for a number of clicks", variable = mode_1_var)
    mode_2_var = IntVar()
    check_box2 = Checkbutton(root, text = "Mode 2: Click for a number of minutes", variable = mode_2_var)
    label1 = Label(root, text = "Total Time: ")
    entry1 = Entry(root, bd = 5)
    label2 = Label(root, text = "Seconds per Click: ")
    entry2 = Entry(root, bd = 5)
    label3 = Label(root, text = "Random Time Factor: ")
    entry3 = Entry(root, bd = 5)
    lock_comp_var = IntVar()
    check_box3 = Checkbutton(root, text = "Lock computer after completion?", variable = lock_comp_var)
    entry1.focus_set()

    def start():
        # Output (Will be replaced by GUI in future)
        print('********** PyAutoClicker **********')

        if mode_1_var.get():
            NUMBER_OF_CLICKS = int(entry1.get())
        elif mode_2_var.get():
            TOTAL_RUN_TIME = float(entry1.get())

        TIME_BETWEEN_CLICKS = float(entry2.get())
        MAX_RANDOM_TIME_VALUE = float(entry3.get())
        
        print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))
        starting_time = datetime.datetime.now().replace(microsecond=0)

        # Main Logic
        if mode_1_var.get():
            mode_1(NUMBER_OF_CLICKS, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE)
        elif mode_2_var.get():
            mode_2(TOTAL_RUN_TIME, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE)

        print('END TIME:   ' + strftime("%Y-%m-%d %I:%M:%S"))
        ending_time = datetime.datetime.now().replace(microsecond=0)
        print('RAN FOR:    ' + str(ending_time - starting_time))

        if (lock_comp_var.get()):
            lock_computer()

    button = Button(root, text = "Submit", command = start)

    label0.pack()
    check_box1.pack()
    check_box2.pack()
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    label3.pack()
    entry3.pack()
    check_box3.pack()
    button.pack(side = BOTTOM)
    root.mainloop()

# Define Click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Define Lock Computer
def lock_computer():
    import ctypes
    ctypes.windll.user32.LockWorkStation()

# Define number of clicks mode (mode 1)
def mode_1(number_of_clicks, time_between_clicks, max_random_time_value):
    x = 0;
    while (x < number_of_clicks):
        time.sleep(time_between_clicks + max_random_time_value*random.random())
        a, b = win32api.GetCursorPos()
        click(a, b)
        x += 1

# Define total run time (mode 2)
def mode_2(total_run_time, time_between_clicks, max_random_time_value):
    start_time = time.time()
    end_time = start_time + total_run_time*60
    while (time.time() < end_time):
        time.sleep(time_between_clicks + max_random_time_value*random.random())
        a, b = win32api.GetCursorPos()
        click(a, b)

show_gui()