import mss
import time
import cv2 as cv
import numpy as np
import pygetwindow as gwindow
from pynput.keyboard import Key, Controller
from matplotlib import pyplot as plt

# iterate through all screens                       X 
# take screenshot                                   X  
# do template matching only for mario               
# if mario is found, 
#   - find only the area that is mario (i.e focus the screen so it is only mario)

# window.activate for focusing
# window.restore to bring it to bring it fowards

if __name__ == "__main__":

    keyboard = Controller()

    windows = gwindow.getAllWindows()
    for window in windows:
        if windows:
            if not window.isMaximized: # brings window into view
                window.restore()
            window.activate() # focuses the window for pynput
            time.sleep(.2) # wait for application to show up on screen 
            size = {
                "top": window.top, "left": window.left, "width": window.width, "height": window.height 
            }
            with mss.MSS() as sct: # takes screenshot then closes
                screenshot = np.array(sct.grab(size))
                screenshot_rgb = cv.cvtColor(screenshot, cv.COLOR_BGRA2RGB)
                screenshot_resize = cv.resize(screenshot_rgb, (512, 480), interpolation=cv.INTER_NEAREST) # conduct this when template is matched
                plt.imshow (screenshot_resize)
                plt.show()

            print(window.title, " : ", window.width, " : ", window.height)