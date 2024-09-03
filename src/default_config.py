# File  : default_config.py
# Brief : This file is having all the preconfig constants for Jade (Hero)

from src.sprite_entity import Entity
from enum import Enum

class DefaultConfig:

    class HeroId(Enum):
        Jade = 1
        Karen = 2
        Rocket = 3

    def __init__(self):
        self.hero_dict = {
            DefaultConfig.HeroId.Jade : "Jade",
            DefaultConfig.HeroId.Karen : "Karen",
            DefaultConfig.HeroId.Rocket : "Rocket"
        }

        self.__hero_config_sprite_path_dict = {
            DefaultConfig.HeroId.Jade : {
                (Entity.SpriteType.STANDING, Entity.Direction.RIGHT) : "assets/images/Jade_right_standing_SS.png",
                (Entity.SpriteType.STANDING, Entity.Direction.LEFT) : "assets/images/Jade_left_standing_SS.png",
                (Entity.SpriteType.RUNNING, Entity.Direction.RIGHT) : "assets/images/Jade_right_sprinting_SS.png",
                (Entity.SpriteType.RUNNING, Entity.Direction.LEFT) : "assets/images/Jade_left_sprinting_SS.png",
                
                # TODO: JUST FOR TESTING ADD. Change the sprite path to actual animations
                (Entity.SpriteType.JUMPING, Entity.Direction.LEFT) : "assets/images/Jade_left_sprinting_SS.png",
                (Entity.SpriteType.JUMPING, Entity.Direction.LEFT) : "assets/images/Jade_left_sprinting_SS.png",
            }
        }
    
    def addAnimations(self, hero_entity:Entity, hero_name:str):
        for hero_id, name in self.hero_dict.items():
            if name == hero_name:
                return self.__addAllSprites(hero_entity, hero_id)
        return False

    def __addAllSprites(self, hero_entity:Entity, id:HeroId):
        for hero_id, sprite_dict in self.__hero_config_sprite_path_dict.items():
            if id == hero_id:
                for movement, sprite_path in sprite_dict.items():
                    hero_entity.addSpriteSheet(movement, sprite_path)
                return True
        return False