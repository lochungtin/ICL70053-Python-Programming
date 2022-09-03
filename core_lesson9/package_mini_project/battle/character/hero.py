import random

class Hero:
    def __init__(self, name, health, strength, defence, luck, weapon):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.luck = luck
        self.weapon = weapon

    def attack(self, enemy):
        if self.weapon.type == "wand":
            spell_power = self.cast_spell()
            attack_power = self.strength * spell_power
        else:
            attack_power = self.strength
            
        enemy.reduce_health(attack_power)

    def cast_spell(self, spell_name="Expulso"):
        if spell_name == "Expulso":
            if self.weapon.is_charged():
                return 1.3
            else:
                return 1.2
        else:
            return 1.0
    
    def reduce_health(self, attack_power):
        number = random.randint(1, 50)
        if number > self.luck:
            self.health = self.health - attack_power + self.defence
                      
    def is_dead(self):
        return self.health <= 0
        
    def declare_victory(self):
        print(f"{self.name}: Good conquers all!")


def _test_hero():
    from battle.item.weapon import Weapon
    print("Testing hero")
    weapon = Weapon("wand")
    hero = Hero("Gandalf", 30, 20, 10, 10, weapon)
    hero.declare_victory()


if __name__ == "__main__":
    _test_hero()