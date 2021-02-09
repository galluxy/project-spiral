class NPC:
  'Base class for all NPCs'
  # all is a class variable 
  # it allows the NPC class to keep track of its instances
  all = []

  def __init__(self, name, race, role=''):
      self.name = name
      self.race = race
      if role != '':
          self.is_advent = True
          self.role = role
      else:
          self.is_advent = False
      self.all.append(self)

  def displayNPCs(self):
      print(self.all)

  def say_hello(self):
      print(f'Hi! I am {self.name} and I am a {self.race}')

  def past_life(self):
      if self.is_advent:
          print(f'I was once an adventuring {self.role}!')
      else:
          print('I am just commonfolk.')

# Tests to ensure NPC is a class and can instantiate new objects
npc1 = NPC('Alex', 'Dragonborn')
npc2 = NPC('Brian', 'Elf', 'Rogue')
npc1.say_hello()
npc1.past_life()
npc2.say_hello()
npc2.past_life()
# print("NPC.all", NPC.all)
# print("All NPCs ", npc1 , npc2)
