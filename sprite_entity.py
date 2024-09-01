import pygame
from enum import Enum

WHITE=(255, 255, 255)

class Entity(pygame.sprite.Sprite):
    class Direction(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4
        IDLE = 5
    
    class SpriteType(Enum):
        STANDING = 1
        RUNNING = 2
        JUMPING = 3
        NONE = 4

    def __init__(self, dimensions = None):
        super().__init__()
        self.dimensions = dimensions if dimensions != None else (64, 64)
        self.animation_sprites = {}
        self.current_animation_key = (Entity.SpriteType.NONE, Entity.Direction.IDLE)
    
    def setIndvSpriteDimensions(self, dimensions):
        self.dimensions = dimensions

    def addSpriteSheet(self, sprite_sheet_path, sprite_type, sprite_direction):
        if isinstance(sprite_type, Entity.SpriteType) and isinstance(sprite_direction, Entity.Direction):
            animation_frame_list = self.getFramesFromSprite(sprite_sheet_path)
            self.animation_sprites[((sprite_type, sprite_direction))] = animation_frame_list
    
    def getFramesFromSprite(self, sprite_sheet):
            frame_list = []
            width, height = self.dimensions
            sprite_image = pygame.image.load(sprite_sheet).convert_alpha()
            num_frames = sprite_image.get_width() // width
            for frame_number in range(num_frames):
                frame_image = pygame.Surface(self.dimensions).convert_alpha()
                frame_image.fill(WHITE)
                frame_image.blit(sprite_image, (0, 0), (frame_number * width, 0, width, height))
                frame_list.append(frame_image)
            return frame_list

    def updateAnimationSprite(self, sprite_type, sprite_direction):
        key = (sprite_type, sprite_direction)
        if key != self.current_animation_key:
            self.current_animation_key = key
            return True
        return False

    def getFrame(self, frame_number = 1, scale = 1):
        if self.current_animation_key in self.animation_sprites:
            frame_image = self.animation_sprites[self.current_animation_key][frame_number - 1]
            frame_image = pygame.transform.scale(frame_image, (frame_image.get_width() * scale, frame_image.get_height() * scale))
            frame_image.set_colorkey(WHITE)
        else:
            # Empty surface in case of no frame found
            frame_image = pygame.Surface(self.dimensions).convert_alpha()
            # print(f"Empty Frame from the getFrame")
        return frame_image
    
    def checkIfLastFrameVisited(self, frame_number):
        if self.current_animation_key in self.animation_sprites:
            if (frame_number - 1) == len(self.animation_sprites[self.current_animation_key]):
                return True
        return False
    
    def getAllFramesFromKey(self, key):
        if key in self.animation_sprites:
            return self.animation_sprites[key]
        return []
    
    def printDebugAllFrames(self, window, key, position):
        pos = position
        for frame in self.getAllFramesFromKey(key):
            frame_rect = frame.get_rect()
            frame_rect.topleft = pos
            window.blit(frame, frame_rect)
            pos = (pos[0] + frame.get_width() + 1, pos[1])