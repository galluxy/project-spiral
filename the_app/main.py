import random_npc as rn

def main():
    race = rn.random_race()
    first_name, last_name = rn.random_name(race)
    print(f'Your NPC is a', race, 'named', first_name, last_name)


main()
