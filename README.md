PyAutoClicker
=============

A customizable and open-sourced auto clicker for all your clicking needs.

![pyautoclicker](https://cloud.githubusercontent.com/assets/7663987/6499488/167604c4-c2ca-11e4-82d4-32e18412455f.png)

##Features

+ Customizable properties in the GUI
+ Start and stop using your mouse or keyboard
+ Left click at a specified rate
+ Click for a certain number of clicks
+ Click for a certain length of time
+ Click at random time intervals
+ Click within a random 5x5 pixel range of mouse location (effective against auto-ban algorithms)
+ Customizable keybindings to start and stop the autoclicker [*FUTURE UPDATE*]
+ Repeat a series of clicks [*IN PROGRESS*]

## Dependencies

+ `win32api` (for Windows low-level system calls)

## Build

To build your own executable python code, type `python setup.py` in the project directory. Note, this will require you to have `py2exe` installed.

## Install

Windows users can simply run the `setup.exe` file located in the `/dist` directory.

## Usage

The auto clicker can be used by either running the installed application as outlined above or from the command line. Simply type `python PyAutoClicker.py` in the directory where the tool exists.
