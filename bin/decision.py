import time
from pynput.keyboard import Controller

class Decision:

    keyboard = Controller()

    GOOMBA_DISTANCE_THREASH = 64
    KOOPA_DISTANCE_THREASH = 64
    PIPE_DISTANCE_THREASH = 64
    SMALL_GAP_DISTANCE_THREASH = 54
    GAP_DISTANCE_THREASH = 64
    
    jump_count = 0

    # takes the coordinates and makes a decision to press the "a" button or not
    def make_decision (self, mario, goombas, pipes, small_ground_gap, ground_gap, koopas, blocks, flag):
        """
        This function is responsible for deciding 
        weather or not to press the jump button.
        """

        if mario:
            if len(goombas) != 0:
                distance = abs(goombas[0][0] - mario[0])
                if distance <= self.GOOMBA_DISTANCE_THREASH: 
                    print("Goomba Distance From Mario: ", distance)
                    self.keyboard.press('s')
                    time.sleep(1)
                    self.keyboard.release('s')

            if len(koopas) != 0:
                distance = abs(koopas[0][0] - mario[0])
                if distance <= self.GOOMBA_DISTANCE_THREASH: 
                    print("Koopa Distance From Mario: ", distance)
                    self.keyboard.press('s')
                    time.sleep(1)
                    self.keyboard.release('s')

            if len(pipes) != 0:
                distance = abs(pipes[0][0] - mario[0])
                if distance <= self.PIPE_DISTANCE_THREASH:
                    print("Pipe Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(1)
                    self.keyboard.release('s')

            if flag != None:
                distance = abs(flag[0] - mario[0])
                if distance <= self.PIPE_DISTANCE_THREASH:
                    print("Flag Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(1)
                    self.keyboard.release('s')
                return True
            
            if len(blocks) != 0:
                self.jump_count = self.jump_count + 1
                if self.jump_count < 5: 
                    self.keyboard.press('s')
                    time.sleep(.25)
                    self.keyboard.release('s')
                else:
                    self.jump_count = 0
                    self.keyboard.press('s')
                    time.sleep(2)
                    self.keyboard.release('s')

            if small_ground_gap != None and len(blocks) == 0:
                distance = abs(small_ground_gap[0] - mario[0])
                if distance <= self.SMALL_GAP_DISTANCE_THREASH:
                    print("Small Gap Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(.6)
                    self.keyboard.release('s')

            if ground_gap != None:
                distance = abs(ground_gap[0] - mario[0])
                if distance <= self.GAP_DISTANCE_THREASH:
                    print("Gap Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(.6)
                    self.keyboard.release('s')

