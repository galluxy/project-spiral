class NPC:
  'Base class for all NPCs'
  all = []

  def __init__(self, name, race):
      self.name = name
      self.race = race
      self.is_advent = False
      self.all.append(self)

  def displayNPCs(self):
      print(self.all)

  def say_hello(self):
      print(f'Hi! I am {self.name} and I am a {self.race}')

# Tests to ensure NPC is a class and can instantiate new objects
npc1 = NPC('Alex', 'Dragonborn')
npc2 = NPC('Brian', 'Elf')
npc1.say_hello()
npc2.say_hello()
print("NPC.all", NPC.all)
print("All NPCs ", npc1 , npc2)
