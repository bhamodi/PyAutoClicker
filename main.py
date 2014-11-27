# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import time
import math
import random
from time import strftime

# Output (Will be replaced by GUI in future)
print('********** PyAutoClicker **********')

# Define constants
TIME_BETWEEN_CLICKS = float(input("Time between clicks: "))
NUMBER_OF_CLICKS = int(input("Number of clicks: "))
MAX_RANDOM_TIME_VALUE = float(input("Maximum random time: "))
LOCK_COMPUTER_UPON_FINISHING = input("Lock computer after finishing? (type 'true' or 'false'): ") == "true"

print('START TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))

# Define Click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Main Logic
x = 0;
while (x < NUMBER_OF_CLICKS):
    time.sleep(TIME_BETWEEN_CLICKS + MAX_RANDOM_TIME_VALUE*random.random())
    a, b = win32api.GetCursorPos()
    click(a, b)
    x = x + 1

print('END TIME: ' + strftime("%Y-%m-%d %I:%M:%S"))

if (LOCK_COMPUTER_UPON_FINISHING):
    import ctypes
    ctypes.windll.user32.LockWorkStation()
