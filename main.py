# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import time
import math
import random

# Define constants
TIME_BETWEEN_CLICKS = 20
NUMBER_OF_CLICKS = 500
MAX_RANDOM_TIME_VALUE = 1.5

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
