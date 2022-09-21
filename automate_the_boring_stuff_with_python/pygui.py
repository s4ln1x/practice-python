#!/usr/bin/env python
# encoding: utf-8
import pyautogui

# NOTE: Important dependencies on linux = apt install scrot

########################################################################################
## Control the mouse with Python #######################################################
########################################################################################
#
## Get the size of the screen
## NOTE: Remember that the offset 0, 0 starts on the upper left corner of the
## screen
#width, height = pyautogui.size()
#print(f'The resolution of your screen is {width}x{height}')
#
## Get the current position of the mouse
#print(f'Your mouse current position is {pyautogui.position()}')
#
## Move the mouse to a given position
#pyautogui.moveTo(10, 10)
#
## Move the mouse to a given position during a given time
#pyautogui.moveTo(253, 45, duration=3)
#
## You can move the mouse with relative moves too
#pyautogui.moveRel(300, 300, duration=3)
#
## Click on something
#pyautogui.click()
#pyautogui.doubleClick()
#pyautogui.rightClick()
#pyautogui.middleClick()
#
## Drag the browser window from one position to another
#pyautogui.moveTo(504, 43)
#pyautogui.click()
#pyautogui.dragRel(0, 500, duration=1.0)
#pyautogui.dragRel(0, 0, duration=1.0)
#
## This will show the position of the mouse all the time, can be useful for
## getting coordinates of the screen, commenting to not stop the execution of
## the script
## print(pyautogui.displayMousePosition())
#
## NOTE: If you want to stop pyautogui, you need to put the mouse on the top
## left
## corner of the screen.
## Control the keyboard from python
#
########################################################################################
## Use the keyboard with Python ########################################################
########################################################################################
## Start writing to any text editor or terminal
#pyautogui.click(275, 77)
#pyautogui.typewrite('Hello World!')
#pyautogui.typewrite('Hello World!', interval=0.5)
#
## You can pass a list of single keys, also is worth saying that this format
## supports arrow keys and slow movement
## All the available keys are in the variable "pyautogui.KEYBOARD_KEYS"
#pyautogui.typewrite(['a', 'left', 'left', 'x'], interval=0.5)
#print(pyautogui.KEYBOARD_KEYS)
#
## You can simulate to press the keyboards too, like pressing escape or shift key
#pyautogui.press('f1')

## Shortcut simulation
#pyautogui.hotkey('shift', 'ctrl', 't')

########################################################################################
# Screenshots and image recognition with Python ########################################
########################################################################################
# Take a screenshot, this will create a pillow image object
pyautogui.screenshot()
# To store the object you need to give a location to the method
pyautogui.screenshot('/home/reycobra/Pictures/image_1.png')
# This method will return the X and Y coordinates and the size of the given image
print(pyautogui.locateOnScreen('/home/reycobra/Pictures/termi.png'))
# This method will return the X and Y coordinates
print(pyautogui.locateCenterOnScreen('/home/reycobra/Pictures/termi.png'))
# Move the mouse to any X and Y valid coordinate
pyautogui.moveTo((682, 46), duration=1)
pyautogui.click()
