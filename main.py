# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import time
import math
import random
from time import strftime

# Define Click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Output (Will be replaced by GUI in future)
print('********** PyAutoClicker **********')

# Pick operation mode (run for a certain amount of time or certain amount of clicks)
#TODO: Will be replaced by GUI
MODE = int(input("Enter '1' for number of clicks mode or '2' for timer mode: "))

# Define constants
if MODE == 1:
    NUMBER_OF_CLICKS = int(input("Number of clicks: "))
else:
    TOTAL_RUN_TIME = int(input("Total run time in minutes: "))

TIME_BETWEEN_CLICKS = float(input("Time between clicks in seconds: "))
MAX_RANDOM_TIME_VALUE = float(input("Maximum random time: "))
LOCK_COMPUTER_UPON_FINISHING = input("Lock computer after finishing? (type 'true' or 'false'): ") == "true"

print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))

# Main Logic
if MODE == 1:
    x = 0;
    while (x < NUMBER_OF_CLICKS):
        time.sleep(TIME_BETWEEN_CLICKS + MAX_RANDOM_TIME_VALUE*random.random())
        a, b = win32api.GetCursorPos()
        click(a, b)
        x = x + 1
elif MODE == 2:
    start_time = time.time()
    end_time = start_time + TOTAL_RUN_TIME*60
    while (time.time() < end_time):
        time.sleep(TIME_BETWEEN_CLICKS + MAX_RANDOM_TIME_VALUE*random.random())
        a, b = win32api.GetCursorPos()
        click(a, b)

print('END TIME:   ' + strftime("%Y-%m-%d %I:%M:%S"))

if (LOCK_COMPUTER_UPON_FINISHING):
    import ctypes
    ctypes.windll.user32.LockWorkStation()
