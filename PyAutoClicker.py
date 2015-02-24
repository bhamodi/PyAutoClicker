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
import tkinter.messagebox
from threading import Thread

global_state = ''

def main():
    # GUI setup
    root = Tk()
    root.title("PyAutoClicker")
    root.resizable(width = False, height = False)
    root.minsize(width = 310, height = 150)
    root.iconbitmap('assets/mouse.ico')

    mode_var = IntVar()
    mode_var.set(1)
    radio_button_1 = Radiobutton(root, text = "Mode 1: Click for a number of clicks", variable = mode_var, value = 1)
    radio_button_2 = Radiobutton(root, text = "Mode 2: Click for a number of minutes", variable = mode_var, value = 0)

    click_var = StringVar()
    click_var.set('Left Click')
    option_menu = OptionMenu(root, click_var, 'Left Click', 'Right Click')

    label1 = Label(root, text = "Number of clicks (OR number of minutes if in mode 2): ")
    entry1 = Entry(root, bd = 5)
    label2 = Label(root, text = "Seconds per click: ")
    entry2 = Entry(root, bd = 5)
    label3 = Label(root, text = "Maximum number of random seconds between clicks: ")
    entry3 = Entry(root, bd = 5)

    lock_comp_var = IntVar()
    check_box3 = Checkbutton(root, text = "Lock computer after completion?", variable = lock_comp_var)
    random_click_var = IntVar()
    check_box4 = Checkbutton(root, text = "Randomly click within 5x5 pixels of mouse?", variable = random_click_var)
    entry1.focus_set()

    def start(event = None):
        # Main Logic of PyAutoClicker
        global global_state
        global_state = "ON"

        if mode_var.get():
            NUMBER_OF_CLICKS = int(entry1.get())
        else:
            TOTAL_RUN_TIME = float(entry1.get())

        TIME_BETWEEN_CLICKS = float(entry2.get())
        MAX_RANDOM_TIME_VALUE = float(entry3.get())
        SHOULD_LOCK = lock_comp_var.get()
        RANDOM_CLICK = random_click_var.get()

        print('******** PyAutoClicker ********')
        if mode_var.get():
            thread = Thread(target = mode_1, args = (NUMBER_OF_CLICKS, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE, SHOULD_LOCK, RANDOM_CLICK))
            thread.start()
        else:
            thread = Thread(target = mode_2, args = (TOTAL_RUN_TIME, TIME_BETWEEN_CLICKS, MAX_RANDOM_TIME_VALUE, SHOULD_LOCK, RANDOM_CLICK))
            thread.start()

    def stop(event = None):
        global global_state
        global_state = "OFF"

    # Start via click or binded key.
    start_button = Button(root, text = "Start (F1)", command = start)
    root.bind('<F1>', start)

    # Stop via click or binded key.
    stop_button = Button(root, text = "Stop (F2)", command = stop)
    root.bind('<F2>', stop)

    # Check if user really meant to quit application.
    def confirm_quit():
        if tkinter.messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", confirm_quit)

    radio_button_1.pack()
    radio_button_2.pack()
    option_menu.pack()
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    label3.pack()
    entry3.pack()
    check_box3.pack()
    check_box4.pack()
    start_button.pack()
    stop_button.pack()
    root.mainloop()

# Define Click
def click(x, y, random_click):
    if random_click:
        original_x = x
        original_y = y
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    if random_click:
        win32api.SetCursorPos((original_x, original_y))

# Define Lock Computer
def lock_computer():
    import ctypes
    ctypes.windll.user32.LockWorkStation()

# Define number of clicks mode (mode 1)
def mode_1(number_of_clicks, time_between_clicks, max_random_time_value, should_lock, random_click):
    print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))
    starting_time = datetime.datetime.now().replace(microsecond = 0)
    x = 0;
    while (x < number_of_clicks):
        if global_state == "OFF":
            break
        time.sleep(time_between_clicks + max_random_time_value * random.random())
        a, b = win32api.GetCursorPos()
        click(a, b, random_click)
        x += 1
    print('END TIME:   ' + strftime("%Y-%m-%d %I:%M:%S"))
    ending_time = datetime.datetime.now().replace(microsecond = 0)
    print('RAN FOR:    ' + str(ending_time - starting_time))
    if should_lock:
        lock_computer()

# Define total run time (mode 2)
def mode_2(total_run_time, time_between_clicks, max_random_time_value, should_lock, random_click):
    print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))
    starting_time = datetime.datetime.now().replace(microsecond = 0)
    start_time = time.time()
    end_time = start_time + total_run_time * 60
    while (time.time() < end_time):
        if global_state == "OFF":
            break
        time.sleep(time_between_clicks + max_random_time_value * random.random())
        a, b = win32api.GetCursorPos()
        click(a, b, random_click)
    print('END TIME:   ' + strftime("%Y-%m-%d %I:%M:%S"))
    ending_time = datetime.datetime.now().replace(microsecond = 0)
    print('RAN FOR:    ' + str(ending_time - starting_time))
    if should_lock:
        lock_computer()

# Define mouse event follower function (mode 3)
def mode_3():
    # Press special key to start tracking (F6) (Happens in GUI)
    # Populate a data structure with click event coordinates and time
    click_sequence = []
    x, y = win32api.GetCursorPos()
    click_sequence.append(x, y, time.time())
    # Press special key to stop tracking (F7) (Happens in GUI)
    # Iterate through key events at the same time intervals they occured
    for i in range(len(click_sequence)):
        x = click_sequence[i][0]
        y = click_sequence[i][1]
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# Run PyAutoClicker
if __name__ == '__main__':
    main()
