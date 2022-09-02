from battle.game.manager import GameManager

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.create_hero("Dumbledore", "wand")
    game_manager.create_enemy("Voldemort", "sword")
    game_manager.start_game()
