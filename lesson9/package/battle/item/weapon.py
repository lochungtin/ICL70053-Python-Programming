class Weapon:
    def __init__(self, weapon_type="wand", damage=5, power=5):
        self.type = weapon_type
        self.damage = damage
        self.power = power
        
    def charge(self):
        self.power += 20
    
    def is_charged(self):
        return self.power >= 5
        
        
def _test_weapon():
    print("Testing weapon")
    weapon = Weapon("wand")
    assert weapon.is_charged() == True
    print("Test complete")
    
if __name__ == "__main__":
    _test_weapon()