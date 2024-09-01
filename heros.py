from sprite_entity import Entity
from utils import timer

class Hero(Entity):

    # Direction signs. To be used when moving the object.
    direction_sign_dict = {
        Entity.Direction.LEFT : -1,
        Entity.Direction.RIGHT : 1
    }

    def __init__(self, position_tuple, dimensions = None, scale = 1):
        super().__init__(dimensions)
        self.m_scale = scale
        self.m_frame_number = 0
        self.m_curr_position = position_tuple
        self.m_movement = (Entity.SpriteType.STANDING, Entity.Direction.RIGHT)
        self.m_speed = 0.2
        self.m_animation_timer = timer.Timer(timer.TimerType.MILLISECONDS, 120)
        self.setFrame()     # Pull empty frame to form the image attribute

    def setSpeed(self, speed):
        self.m_speed = speed
    
    def setPosition(self, position_tuple):
        self.m_curr_position = position_tuple
        print(f"POSITION CHANGED, {self.m_curr_position}")

    def getPosition(self):
        return self.m_curr_position

    def getDimensions(self):
        return (self.m_image.get_width(), self.m_image.get_height())

    def setScale(self, scale):
        self.m_scale = scale
    
    def getArealDimensions(self):
        x1, y1 = self.getPosition()
        x2, y2 = self.getDimensions()
        x2 = x2 + x1
        y2 = y2 + y1
        return (x1, y1, x2, y2)

    def setFrame(self, frame_number:int = 1):
        self.m_image = self.getFrame(frame_number, self.m_scale)
        self.m_rect = self.m_image.get_rect()

    def draw(self, window, position = None):
        if self.m_animation_timer.resetWhenElapsed():
            self.m_frame_number += 1
            if self.checkIfLastFrameVisited(self.m_frame_number):
                self.m_frame_number = 1
            self.setFrame(self.m_frame_number)
        
        if self.m_movement[0] != Entity.SpriteType.STANDING:
            self.setPosition(
                (self.m_curr_position[0] + self.direction_sign_dict[self.m_movement[1]] * self.m_speed, self.m_curr_position[1])
            )
        
        window.blit(self.m_image, self.getPosition())

    def standing(self, direction):
        if isinstance(direction, Entity.Direction):
            if (
                direction in [Entity.Direction.RIGHT, Entity.Direction.LEFT] and
                self.updateAnimationSprite(Entity.SpriteType.STANDING, direction)
            ):
                self.m_frame_number = 1
                self.m_movement = (Entity.SpriteType.STANDING, direction)
                self.m_animation_timer.setElapseReset(300)
    
    def run(self, direction):
        if isinstance(direction, Entity.Direction):
            if (
                direction in [Entity.Direction.RIGHT, Entity.Direction.LEFT] and
                self.updateAnimationSprite(Entity.SpriteType.RUNNING, direction)
            ):
                self.m_frame_number = 1
                self.m_movement = (Entity.SpriteType.RUNNING, direction)
                self.m_animation_timer.setElapseReset(120)

    def jump(self):
        # TODO: Jump operation
        pass
