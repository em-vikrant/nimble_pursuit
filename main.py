# FILE: main.py
# BRIEF: Main file for the game

from src.nimble_pursuit import Game

if __name__ == "__main__":
    # Create game object
    game = Game()

    print(f"[INFO] Game = {game.getName()}, Version = {game.getVersion()}")

    # Initialize the game
    game.init()

    # Run the game loop
    game.run()

    # Cloase the game
    game.close()