import random_npc as rn

def main():
    race = rn.random_race()
    name_string = rn.random_name(race)
    print(f'Your NPC is a', race, 'named', name_string)


main()
