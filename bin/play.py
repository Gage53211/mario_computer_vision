import mss
import time
import pygame
import detect
from decision import Decision
import cv2 as cv
import numpy as np
import pygetwindow as gwindow
from pynput.keyboard import Key, Controller
from matplotlib import pyplot as plt

def crop_top (image):
    new_size = 0
    try:
        while image[new_size][100] != 157 and new_size < len(image):
            new_size += 1
        return new_size
    except IndexError:
        print("Could not crop top of screen, maybe the screen was black?")
        return None


def crop_left (image):
    new_size = 0
    try:
        while image[100][new_size] != 157:
            new_size += 1
        return new_size
    except IndexError:
        print("Could not crop left of screen, maybe the screen was black?")
        return None


def crop_height (image):
    new_size = image.shape[0] - 1
    try:
        while image[new_size][100] != 0 and image[new_size][100] != 90 and image[new_size][100] != 218:
            new_size -= 1
        return new_size
    except IndexError:
        print("Could not crop bottom of screen, maybe the screen was black?")
        return None


def crop_width (image):
    new_size = image.shape[1] - 1
    try:
        while image[100][new_size] != 157:
            new_size -= 1
        return new_size
    except IndexError:
            print("Could not crop right of screen, maybe the screen was black?")
            return None


if __name__ == "__main__":

    keyboard = Controller()
    pygame.init()

    try:
        window = gwindow.getWindowsWithTitle('Mesen - Super Mario Bros. (World)')[0]
    except IndexError:
        print("Mesen Emulator Running Super Mario Not Found, Try renaming rom to \"Super Mario Bros. (World)\"")
        exit()
   
    if window:
        if not window.isMaximized: # brings window into view
            window.restore()
        window.activate() # focuses the window for pynput
        time.sleep(.5) # wait for application to show up on screen
        size = {
            "top": window.top, "left": window.left, "width": window.width, "height": window.height
        }

        with keyboard.pressed(Key.ctrl):
            keyboard.press('r')
            time.sleep(.1)
            keyboard.release('r')
            time.sleep(1.5)

        #input start key
        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('w')

        #wait for black screen to clear then hold down right key
        time.sleep(3.5)
        keyboard.press(Key.right)

        new_top = None
        new_height = None
        new_width = None

        clock = pygame.time.Clock()
        dec = Decision()
        is_finished = False

        with mss.MSS() as sct:
            while not is_finished: # main loop for screen analysis
                screenshot = np.array(sct.grab(size))
                screenshot_grey = cv.cvtColor(screenshot, cv.COLOR_BGRA2GRAY)

                # crop when conditions are correct
                if new_top is None:
                    new_top = crop_top (screenshot_grey)
               
                if new_height is None:
                    new_height = crop_height (screenshot_grey)

                if new_width is None:    
                    new_width = crop_width (screenshot_grey)

                screenshot_grey = screenshot_grey[200 : new_height, 200 : new_width]

                # detect all objects
                mario_coords, mario_shape           = detect.find_single_item    (image=screenshot_grey, name="mario")
                small_gap_coords, small_gap_shape   = detect.find_single_item    (image=screenshot_grey, name="small_ground_gap")
                gap_coords, gap_shape               = detect.find_single_item    (image=screenshot_grey, name="ground_gap")
                flag_coords, flag_shape             = detect.find_single_item    (image=screenshot_grey, name="flag")

                pipes,  pipe_shape                  = detect.find_multiple_items (image=screenshot_grey, name="pipe")
                blocks, block_shape                 = detect.find_multiple_items (image=screenshot_grey, name="block")
                goombas, goomba_shape               = detect.find_multiple_items (image=screenshot_grey, name="goomba")
                koopas, koopa_shape                 = detect.find_multiple_items (image=screenshot_grey, name="koopa")

                is_finished = dec.make_decision(mario=mario_coords,
                                                goombas=goombas,
                                                pipes=pipes,
                                                small_ground_gap=small_gap_coords,
                                                ground_gap=gap_coords,
                                                koopas=koopas,
                                                blocks=blocks,
                                                flag=flag_coords)
                
                clock.tick(25) # limits framerate to 25 frames per second.

        # jump onto the flagpole
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')
        print ("1-1 Completed :)")
               


           
   


       
