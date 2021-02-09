import random_npc as rn
from NPC import NPC

def main():
    race = rn.random_race()
    name = rn.random_name(race)
    new_npc = NPC(name, race)
    print(f'Your NPC is a', race, 'named', name)
    new_npc.say_hello()


main()
