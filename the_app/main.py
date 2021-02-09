import random_npc as rn


def main():
    race = rn.random_race()
    name = rn.random_name(race)
    print(f'Your NPC is a', race, 'named', name)


main()
