# The Python Auto Clicker
# Author: Baraa Hamodi

# Imports
import win32api, win32con
import time
import math

# Define Click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

# Main Logic
x = 0;
while (x < 5):
    time.sleep(2)
    a, b = win32api.GetCursorPos()
    click(a, b)
    x = x + 1
