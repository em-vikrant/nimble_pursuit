# FILE: main.py
# BRIEF: This is the main file containing the main game loop

import pygame
import sys
from heros import Hero
from sprite_entity import Entity


if __name__ == "__main__":
    print("[INFO] Game: Running Jade = Start")

    WINDOW_DIMENSIONS = (800, 600)

    pygame.init()
    window = pygame.display.set_mode(WINDOW_DIMENSIONS)
    pygame.display.set_caption("Running Jade")

    clock = pygame.time.Clock()

    hero = Hero((0, 0))
    hero.addSpriteSheet("assets/Jade_right_standing_SS.png", Entity.SpriteType.STANDING, Entity.Direction.RIGHT)
    hero.addSpriteSheet("assets/Jade_left_standing_SS.png", Entity.SpriteType.STANDING, Entity.Direction.LEFT)
    hero.addSpriteSheet("assets/Jade_left_sprinting_SS.png", Entity.SpriteType.RUNNING, Entity.Direction.LEFT)
    hero.addSpriteSheet("assets/Jade_right_sprinting_SS.png", Entity.SpriteType.RUNNING, Entity.Direction.RIGHT)
    hero.standing(Entity.Direction.RIGHT)
    hero.setScale(2)
    hero.setPosition((0, 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                pass

            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Up Key pressed")
                elif event.key == pygame.K_DOWN:
                    print("DOWN Key pressed")
                elif event.key == pygame.K_LEFT:
                    print("LEFT key pressed")
                    hero.run(Entity.Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    print("Right key pressed")
                    hero.run(Entity.Direction.RIGHT)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print("Up Key released")
                elif event.key == pygame.K_DOWN:
                    print("DOWN Key released")
                elif event.key == pygame.K_LEFT:
                    print("LEFT key released")
                    hero.standing(Entity.Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    print("Right key released")
                    hero.standing(Entity.Direction.RIGHT)

        window.fill((150, 150, 150))
        hero.draw(window)

        pygame.display.flip()
        # clock.tick(60)

    pygame.quit()
    sys.exit()


