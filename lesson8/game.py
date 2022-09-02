import libmonster

print(libmonster.FACTOR)

print(libmonster.calculate_growthrate(2))

monsters = libmonster.spawn_monsters()

new_monster = libmonster.Monster("Crazy", "sashimi")
monsters.append(new_monster)

for monster in monsters:
    print(f"{monster.name} love {monster.food}!")
