import time
from pynput.keyboard import Controller

class Decision:

    keyboard = Controller()

    GOOMBA_DISTANCE_THREASH = 64
    KOOPA_DISTANCE_THREASH = 64
    PIPE_DISTANCE_THREASH = 64
    FLAG_DISTANCE_THREASH = 64
    SMALL_GAP_DISTANCE_THREASH = 54
    GAP_DISTANCE_THREASH = 64

    GOOMBA_JUMP_TIME = 1.5
    KOOPA_JUMP_TIME = 1.0
    PIPE_JUMP_TIME = 1.0
    FLAG_JUMP_TIME = 1.0
    SMALL_GAP_JUMP_TIME = 0.6
    GAP_JUMP_TIME = 0.6
    
    BLOCK_JUMP_TIME = .027
    ON_BLOCK_WAIT_TIME = .320
    BLOCK_JUMP_TIME_EXTENDED = 2
    APPROACHING_HILL_TIME = 1.6
    HILL_JUMP_COUNT = 4
    

    def __init__(self):
         self.jump_count = 0
         self.approaching_hill = True


    # takes the coordinates and makes a decision to press the "a" button or not
    def make_decision (self, mario, goombas, pipes, small_ground_gap, ground_gap, koopas, blocks, flag):
        """
        This function is responsible for deciding 
        weather or not to press the jump button.
        """

        if mario:
            if len(goombas) != 0 and len(blocks) == 0:
                distance = abs(goombas[0][0] - mario[0])
                if distance <= self.GOOMBA_DISTANCE_THREASH: 
                    print("Goomba Distance From Mario: ", distance)
                    self.keyboard.press('s')
                    time.sleep(self.GOOMBA_JUMP_TIME)
                    self.keyboard.release('s')

            if len(koopas) != 0:
                distance = abs(koopas[0][0] - mario[0])
                if distance <= self.GOOMBA_DISTANCE_THREASH: 
                    print("Koopa Distance From Mario: ", distance)
                    self.keyboard.press('s')
                    time.sleep(self.KOOPA_JUMP_TIME)
                    self.keyboard.release('s')

            if len(pipes) != 0:
                distance = abs(pipes[0][0] - mario[0])
                if distance <= self.PIPE_DISTANCE_THREASH:
                    print("Pipe Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(self.PIPE_JUMP_TIME)
                    self.keyboard.release('s')

            if flag != None:
                distance = abs(flag[0] - mario[0])
                if distance <= self.FLAG_DISTANCE_THREASH:
                    print("Flag Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(self.FLAG_JUMP_TIME)
                    self.keyboard.release('s')
                return True
            
            if len(blocks) != 0:
                if self.approaching_hill:
                    time.sleep(self.APPROACHING_HILL_TIME)
                    self.approaching_hill = False
                    print ("Approaching Hill")
                if self.jump_count < self.HILL_JUMP_COUNT: 
                    self.keyboard.press('s')
                    time.sleep(self.BLOCK_JUMP_TIME)
                    self.keyboard.release('s')
                    time.sleep(self.ON_BLOCK_WAIT_TIME)
                    self.jump_count = self.jump_count + 1
                    print("Hill Jump: ", self.jump_count)
                else:
                    print("big jump?")
                    self.jump_count = 0
                    self.keyboard.press('s')
                    time.sleep(self.BLOCK_JUMP_TIME_EXTENDED)
                    self.keyboard.release('s')

            if small_ground_gap != None and len(blocks) == 0:
                distance = abs(small_ground_gap[0] - mario[0])
                if distance <= self.SMALL_GAP_DISTANCE_THREASH:
                    print("Small Gap Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(self.SMALL_GAP_JUMP_TIME)
                    self.keyboard.release('s')

            if ground_gap != None:
                distance = abs(ground_gap[0] - mario[0])
                if distance <= self.GAP_DISTANCE_THREASH:
                    print("Gap Distance From Mario: ", distance) 
                    self.keyboard.press('s')
                    time.sleep(self.GAP_JUMP_TIME)
                    self.keyboard.release('s')


       
