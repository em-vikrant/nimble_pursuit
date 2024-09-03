# FILE: nimble_pursuit.py
# BRIEF: This is the main file containing the main game loop

import pygame
from src.hero import Hero
from src.sprite_entity import Entity
from src.default_config import DefaultConfig

class Game:
    __WINDOW_DIMENSIONS = (800, 600)      # Window dimensions

    # TODO: Add versions in config file
    __MAJOR_VERSION:int = 0             # Major version: !For new releases like theme change, map addition, level addition
    __MINOR_VERSION:int = 1             # Minor version: !For new additions like character additions, ability additions
    __SUB_MINOR_VERISON:int = 0         # Sub minor verison: !For bug fix releases

    __TITLE = "Nimble Pursuit"           # Game Title 

    def __init__(self, window_dimensions:tuple = None):
        if window_dimensions != None:
            self.__WINDOW_DIMENSIONS = window_dimensions

        # Initialize pygame window
        pygame.init()
        self.__window = pygame.display.set_mode(self.__WINDOW_DIMENSIONS)

        # Get default configs
        self.__default_configs = DefaultConfig()

        self.__game_running_flag = False

        # Get the game version
        self.__game_version:str = self.__fetchVersion()
        self.__TITLE:str = self.__fetchName()

    # Private Methods
    def __fetchVersion(self):
        # TODO: Fetch from config
        major_version = str(self.__MAJOR_VERSION)
        minor_version = str(self.__MINOR_VERSION)
        sub_minor_version = str(self.__SUB_MINOR_VERISON)
        return ".".join([major_version, minor_version, sub_minor_version])
    
    def __fetchName(self):
        # TODO: Fetch from config
        return "Nimble Pursuit"
    
    def __createEntities(self):
        self.hero_jade = Hero((0, 0))

    def __entityPreprocessing(self):
        self.__default_configs.addAnimations(self.hero_jade, "Jade")
        self.hero_jade.standing(Entity.Direction.RIGHT)
        self.hero_jade.setPosition((0, 100))
        self.hero_jade.setScale(2)

    # Public Methods
    def getVersion(self):
        return self.__game_version
    
    def getName(self):
        return self.__TITLE

    def init(self):
        self.__createEntities()
        self.__entityPreprocessing()
        self.__game_running_flag = True

    def run(self):
        while self.__game_running_flag:
        # While loop begin
            for self.event in pygame.event.get():
            # For loop begin
                if self.event.type == pygame.QUIT:
                    self.__game_running_flag = False

                if self.event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif self.event.type == pygame.MOUSEMOTION:
                    pass
                elif self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_UP:
                        print("Up Key pressed")
                    elif self.event.key == pygame.K_DOWN:
                        print("DOWN Key pressed")
                    elif self.event.key == pygame.K_LEFT:
                        print("LEFT key pressed")
                        self.hero_jade.run(Entity.Direction.LEFT)
                    elif self.event.key == pygame.K_RIGHT:
                        print("Right key pressed")
                        self.hero_jade.run(Entity.Direction.RIGHT)
                elif self.event.type == pygame.KEYUP:
                    if self.event.key == pygame.K_UP:
                        print("Up Key released")
                    elif self.event.key == pygame.K_DOWN:
                        print("DOWN Key released")
                    elif self.event.key == pygame.K_LEFT:
                        print("LEFT key released")
                        self.hero_jade.standing(Entity.Direction.LEFT)
                    elif self.event.key == pygame.K_RIGHT:
                        print("Right key released")
                        self.hero_jade.standing(Entity.Direction.RIGHT)
            # For loop end

            self.__window.fill((150, 150, 150))
            self.hero_jade.draw(self.__window)

            pygame.display.flip()
        #While loop end

    def close(self):
        self.__game_running_flag = False
        pygame.quit()