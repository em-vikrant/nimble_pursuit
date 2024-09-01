import pygame
from enum import Enum

class TimerType(Enum):
    SECONDS = 1
    MILLISECONDS = 2

class Timer:
    def __init__(self, timer_type: TimerType, timer_value):
        if isinstance(timer_type, TimerType):
            self.timer_type = timer_type
            self.timer_value = timer_value
            self.set_elapse_reset = False
            self.set()

    def set(self, timer_value = None):
        if timer_value != None:
            self.timer_value = timer_value
            
        if self.timer_type == TimerType.SECONDS:
                self.timer_limit = (self.timer_value * 1000 + pygame.time.get_ticks()) / 1000
        elif self.timer_type == TimerType.MILLISECONDS:
            self.timer_limit = self.timer_value + pygame.time.get_ticks()
    
    def setElapseReset(self, timer_value):
        self.timer_value = timer_value
        self.set_elapse_reset = True

    def isElapsed(self):
        curr_ticks = pygame.time.get_ticks()
        if self.timer_type == TimerType.SECONDS:
            curr_ticks /= 1000
        
        if curr_ticks >= self.timer_limit:
            return True
        return False

    def resetWhenElapsed(self):
        if self.isElapsed() and not self.set_elapse_reset:
            self.set()
            return True
        elif self.set_elapse_reset:
            self.set_elapse_reset = False
            return True
        return False

