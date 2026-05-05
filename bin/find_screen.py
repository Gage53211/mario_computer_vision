import mss
import cv2 as cv
import pygetwindow as gwindow
from pynput.keyboard import Key, Controller

# iterate through all screens
# take screenshot
# do template matching only for mario
# if mario is found, 
#   - find only the area that is mario (i.e focus the screen so it is only mario)


if __name__ == "__main__":

    keyboard = Controller()

    windows = gwindow.getAllWindows()
    for window in windows:
        if window.title ==  "Spotify Premium": 
            if not window.isMaximized:
                window.restore()
            window.activate()
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            print(window.title, " : ", window.width, " : ", window.height)
            break