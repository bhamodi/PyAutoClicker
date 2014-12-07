# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import math
import random
import time
from time import strftime
import datetime

# GUI Setup
def show_gui():
    from tkinter import *
    root = Tk()
    root.title("PyAutoClicker")
    root.resizable(width = False, height = False)
    root.minsize(width = 300, height = 150)

    label1 = Label(root, text = "Total Time: ")
    entry1 = Entry(root, bd = 5)
    entry1.focus_set()
    label2 = Label(root, text = "Seconds per Click: ")
    entry2 = Entry(root, bd = 5)
    label3 = Label(root, text = "Random Time Factor: ")
    entry3 = Entry(root, bd = 5)

    def start():
        print(entry1.get())
        print(entry2.get())
        print(entry3.get())

    button = Button(root, text = "Submit", command = start)

    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    label3.pack()
    entry3.pack()
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

# Output (Will be replaced by GUI in future)
print('********** PyAutoClicker **********')

# Pick operation mode (run for a certain amount of time or certain amount of clicks)
#TODO: Will be replaced by GUI
MODE = int(input("Enter '1' for number of clicks mode or '2' for timer mode: "))

# Define constants
if MODE == 1:
    NUMBER_OF_CLICKS = int(input("Number of clicks: "))
else:
    TOTAL_RUN_TIME = float(input("Total run time in minutes: "))

TIME_BETWEEN_CLICKS = float(input("Time between clicks in seconds: "))
MAX_RANDOM_TIME_VALUE = float(input("Maximum random time: "))
LOCK_COMPUTER_UPON_FINISHING = input("Lock computer after finishing? (type 'true' or 'false'): ") == "true"

print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))
starting_time = datetime.datetime.now().replace(microsecond=0)

# Main Logic
if MODE == 1:
    mode_1(NUMBER_OF_CLICKS, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE)
elif MODE == 2:
    mode_2(TOTAL_RUN_TIME, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE)

print('END TIME:   ' + strftime("%Y-%m-%d %I:%M:%S"))
ending_time = datetime.datetime.now().replace(microsecond=0)
print('RAN FOR:    ' + str(ending_time - starting_time))

if (LOCK_COMPUTER_UPON_FINISHING):
    lock_computer()