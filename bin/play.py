import mss
import time
import pygame
import detect
from decision import Decision
import cv2 as cv
import numpy as np
import pygetwindow as gwindow
from pynput.keyboard import Key, Controller


class Play ():
    
    is_finished = None
    new_height = None
    new_width = None

    keyboard = None
    clock = None
    dec = None

    def __init__ (self):
        """This function preps the emulator for pynput input"""

        pygame.init()

        self.is_finished = False
        self.new_height = None
        self.new_width = None
        self.size = None
        self.window = None

        self.keyboard = Controller()
        self.clock = pygame.time.Clock()
        self.dec = Decision()
        
        try:
            self.window = gwindow.getWindowsWithTitle('Mesen - Super Mario Bros')[0]
            print("Mesen Emulator Running Super Mario Found,", 
                  "DO NOT MOVE WINDOW")
        except IndexError:
            print("Mesen Emulator Running Super Mario Not Found,", 
                  "\nIf the emulator is running, Try renaming .nes file to \"Super Mario Bros\"")
            exit()

        if self.window:
            if not self.window.isMaximized: # brings window into view
                self.window.restore()
            self.window.activate() # focuses the window for pynput
            time.sleep(.5) # wait for application to show up on screen

            # have the emulator display at 2x resolution
            with self.keyboard.pressed(Key.alt):
                self.keyboard.press('2')
                time.sleep(.1)
                self.keyboard.release('2')
                time.sleep(.5)

            self.size = {
                "top": self.window.top, "left": self.window.left, "width": self.window.width, "height": self.window.height
            }
            
            # have the emulator reset the game
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press('r')
                time.sleep(.1)
                self.keyboard.release('r')
                time.sleep(1.5)

            # input start key
            self.keyboard.press('w')
            time.sleep(.1)
            self.keyboard.release('w')

            # wait for black screen to clear then hold down right key
            time.sleep(3.5)
            self.keyboard.press(Key.right)
    
    def main_loop (self):
        """
        This function gets the position of Mario,
        enemies, and obstacles from detect.py and
        sends them to decision.py 25 times per 
        second.
        """

        with mss.MSS() as sct:
            while not self.is_finished: 
                screenshot = np.array(sct.grab(self.size))
                screenshot_grey = cv.cvtColor(screenshot, cv.COLOR_BGRA2GRAY)

                self.size = {
                    "top": self.window.top, "left": self.window.left, "width": self.window.width, "height": self.window.height
                }

                # crop when conditions are correct
                if self.new_height is None:
                    self.new_height = self.crop_height (screenshot_grey)

                if self.new_width is None:    
                    self.new_width = self.crop_width (screenshot_grey)

                if self.new_height != -1 or self.new_width != -1:
                    screenshot_grey = screenshot_grey[200 : self.new_height, 200 : self.new_width]
                else:  
                    print ("Could not crop screen... ",
                           "\nThis could be due the screen being black. ",
                           "\nIt could also be due to your display scale being set below or above 100%")

                # detect all objects
                mario_coords, mario_shape           = detect.find_single_item    (image=screenshot_grey, name="mario")
                small_gap_coords, small_gap_shape   = detect.find_single_item    (image=screenshot_grey, name="small_ground_gap")
                gap_coords, gap_shape               = detect.find_single_item    (image=screenshot_grey, name="ground_gap")
                flag_coords, flag_shape             = detect.find_single_item    (image=screenshot_grey, name="flag")

                pipes,  pipe_shape                  = detect.find_multiple_items (image=screenshot_grey, name="pipe")
                blocks, block_shape                 = detect.find_multiple_items (image=screenshot_grey, name="block")
                goombas, goomba_shape               = detect.find_multiple_items (image=screenshot_grey, name="goomba")
                koopas, koopa_shape                 = detect.find_multiple_items (image=screenshot_grey, name="koopa")

                self.is_finished = self.dec.make_decision(mario=mario_coords,
                                                          goombas=goombas,
                                                          pipes=pipes,
                                                          small_ground_gap=small_gap_coords,
                                                          ground_gap=gap_coords,
                                                          koopas=koopas,
                                                          blocks=blocks,
                                                          flag=flag_coords)
                
                self.clock.tick(25) # limits while loop to run 25 times per second.

        # jump onto the flagpole
        self.keyboard.press('s')
        time.sleep(1)
        self.keyboard.release('s')
        print ("1-1 Completed :)")

    def crop_height (self, image):
        """Crops out anything thats not related to super mario on the bottom"""

        new_size = image.shape[0] - 1
        try:
            while image[new_size][100] != 0 and image[new_size][100] != 90 and image[new_size][100] != 218:
                new_size -= 1
            return new_size
        except IndexError:
            return -1

    def crop_width (self, image):
        """Crops out anything thats not related to super mario on the right hand side"""

        new_size = image.shape[1] - 1
        try:
            while image[100][new_size] != 157:
                new_size -= 1
            return new_size
        except IndexError:
            return -1
    
if __name__ == "__main__":

    game = Play()
    game.main_loop()