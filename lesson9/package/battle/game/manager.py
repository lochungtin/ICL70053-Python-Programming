from battle.character.hero import Hero
from battle.character.enemy import Enemy
from battle.item.weapon import Weapon

class GameManager:
    def __init__(self):
        self.hero = None
        self.enemy = None
    
    def start_game(self):
        if self.hero is None:
            print(f"Please create a hero character before you start.")
            return
        if self.enemy is None:
            print(f"Please create an enemy character before you start.")
            return
            
        while not self.hero.is_dead() and not self.enemy.is_dead():
            print(f"{self.hero.name} attacks {self.enemy.name}")
            self.hero.attack(self.enemy)
 
            if not self.enemy.is_dead():
                print(f"{self.enemy.name} attacks {self.hero.name}")
                self.enemy.attack(self.hero) 

        if self.enemy.is_dead():
            print(f"{self.enemy.name} is dead. {self.hero.name} wins!")
            self.hero.declare_victory() 
        else:
            print(f"{self.hero.name} is dead. {self.enemy.name} wins!")
            self.enemy.declare_victory() 

    def create_hero(self, name, weapon_type):
        weapon = Weapon(weapon_type)
        self.hero = Hero(name, 30, 30, 20, 10, weapon)
        
    def create_enemy(self, name, weapon_type):
        weapon = Weapon(weapon_type)
        self.enemy = Enemy(name, 30, 30, 20, 5, weapon)
        