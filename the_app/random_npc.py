#right now I'm going to stick the base program in main using lists as 
#main data structures
#SQL and mutliple files to come later


import random as rand

def random_race():
    #will return a random race using the same d100 probability
    #as the spell Reincarnate

    race = rand.choice(race_list)
    return(race)


def random_first_name(race):
    
    return rand.choice(first_names[race])
    


def random_last_name(race):
    return rand.choice(last_names[race])


#data structures go here
#will use lists in the form of race_first, race_last and pull randomly


race_list = ['Dragonborn','Dragonborn','Dragonborn','Dragonborn','Hill Dwarf',
             'Hill Dwarf','Hill Dwarf','Hill Dwarf','Hill Dwarf','Hill Dwarf',
             'Hill Dwarf','Hill Dwarf','Hill Dwarf','Mountain Dwarf','Mountain Dwarf',
             'Mountain Dwarf','Mountain Dwarf','Mountain Dwarf','Mountain Dwarf','Mountain Dwarf',
             'Mountain Dwarf','Drow Elf','Drow Elf','Drow Elf','Drow Elf','High Elf',
             'High Elf','High Elf','High Elf','High Elf','High Elf','High Elf','High Elf','High Elf',
             'Wood Elf','Wood Elf','Wood Elf','Wood Elf','Wood Elf','Wood Elf','Wood Elf','Wood Elf',
             'Forest Gnome','Forest Gnome','Forest Gnome','Forest Gnome','Rock Gnome','Rock Gnome',
             'Rock Gnome','Rock Gnome','Rock Gnome','Rock Gnome','Half-Elf','Half-Elf','Half-Elf',
             'Half-Elf','Half-Orc','Half-Orc','Half-Orc','Half-Orc','Lightfoot Halfling',
             'Lightfoot Halfling','Lightfoot Halfling','Lightfoot Halfling','Lightfoot Halfling',
             'Lightfoot Halfling','Lightfoot Halfling','Lightfoot Halfling','Stout Halfling',
             'Stout Halfling','Stout Halfling','Stout Halfling','Stout Halfling','Stout Halfling',
             'Stout Halfling','Stout Halfling','Human','Human','Human','Human','Human','Human',
             'Human','Human','Human','Human','Human','Human','Human','Human','Human','Human',
             'Human','Human','Human','Human','Tiefling','Tiefling','Tiefling','Tiefling',]


####Name nested dicts####

first_names = {'Dragonborn': ['dragonfirst'],
               'Hill Dwarf' : ['hdwarffirst'],
               'Mountain Dwarf' : ['mdwarffirst'],
               'Drow Elf' : ['drowfirst'],
               'High Elf' : ['highelffirst'],
               'Wood Elf' : ['woodelffirst'],
               'Forest Gnome' : ['forestgnomefirst'],
               'Rock Gnome' : ['rockgnomefirst'],
               'Half-Elf' : ['halfelffirst'],
               'Half-Orc' : ['halforcfirst'],
               'Lightfoot Halfling' : ['lightfoothalflingfirst'],
               'Stout Halfling' : ['stouthalflingfirst'],
               'Human' : ['humanfirst1','humanfirst2'],
               'Tiefling' : ['tieflingfirst']}

last_names = {'Dragonborn': ['dragonlast'],
               'Hill Dwarf' : ['hdwarflast'],
               'Mountain Dwarf' : ['mdwarflast'],
               'Drow Elf' : ['drowlast'],
               'High Elf' : ['highelflast'],
               'Wood Elf' : ['woodelflast'],
               'Forest Gnome' : ['forestgnomelast'],
               'Rock Gnome' : ['rockgnomelast'],
               'Half-Elf' : ['halfelflast'],
               'Half-Orc' : ['halforclast'],
               'Lightfoot Halfling' : ['lightfoothalflinglast'],
               'Stout Halfling' : ['stouthalflinglast'],
               'Human' : ['humanlast1','humanlast2'],
               'Tiefling' : ['tieflinglast']}


import unittest

class TestMain(unittest.TestCase):

    def test_randomness(self):
        #current tolerance is set at 5 in either direction
        #accepting suggestions how to make this less lengthy,
        #basically running the function a bunch and verifying it's within a certain range of expected randomness
        count_dragonborn = 0
        count_hill_dwarf = 0
        count_mountain_dwarf = 0
        count_drow_elf = 0
        count_high_elf = 0
        count_wood_elf = 0
        count_forest_gnome = 0
        count_rock_gnome = 0
        count_half_elf = 0
        count_half_orc = 0
        count_lightfoot_halfling = 0
        count_stout_halfling = 0
        count_human = 0
        count_tiefling = 0
        for _ in range(10000):
            i = random_race()
            if i == 'Dragonborn':
                count_dragonborn += 1
            elif i == 'Hill Dwarf':
                count_hill_dwarf += 1
            elif i == 'Mountain Dwarf':
                count_mountain_dwarf += 1
            elif i == 'Drow Elf':
                count_drow_elf += 1
            elif i == 'High Elf':
                count_high_elf += 1
            elif i == 'Wood Elf':
                count_wood_elf += 1
            elif i == 'Forest Gnome':
                count_forest_gnome += 1
            elif i == 'Rock Gnome':
                count_rock_gnome += 1
            elif i == 'Half-Elf':
                count_half_elf += 1
            elif i == 'Half-Orc':
                count_half_orc += 1
            elif i == 'Lightfoot Halfling':
                count_lightfoot_halfling += 1
            elif i == 'Stout Halfling':
                count_stout_halfling += 1
            elif i == 'Human':
                count_human += 1
            elif i == 'Tiefling':
                count_tiefling += 1
                
        count_dragonborn = count_dragonborn/100
        #ideal is 4
        self.assertTrue(0 < count_dragonborn <= 9)

        count_hill_dwarf = count_hill_dwarf/100
        #ideal is 9
        self.assertTrue(4 <= count_hill_dwarf <= 14)

        count_mountain_dwarf = count_mountain_dwarf/100
        #ideal is 8
        self.assertTrue(3 <= count_hill_dwarf <= 13)

        count_drow_elf = count_drow_elf/100
        #ideal is 4
        self.assertTrue(0 <= count_drow_elf <= 9)

        count_high_elf = count_high_elf/100
        #ideal is 9
        self.assertTrue(4 <= count_high_elf <= 13)

        count_wood_elf = count_wood_elf/100
        #ideal is 8
        self.assertTrue(3 <= count_wood_elf  <= 13)

        count_forest_gnome = count_forest_gnome/100
        #ideal is 4
        self.assertTrue(0 <= count_forest_gnome  <= 9)
        
        count_rock_gnome = count_rock_gnome/100
        #ideal is 6
        self.assertTrue(1 <= count_rock_gnome <= 11)
        
        count_half_elf = count_half_elf/100
        #ideal is 4
        self.assertTrue(0 <= count_half_elf <= 9)
        
        count_half_orc = count_half_orc/100
        #ideal is 4
        self.assertTrue(0 <= count_half_orc <= 9)
        
        count_lightfoot_halfling = count_lightfoot_halfling/100
        #ideal is 8
        self.assertTrue(3 <= count_lightfoot_halfling <= 13)
        
        count_stout_halfling = count_stout_halfling/100
        #ideal is 9
        self.assertTrue(4 <= count_stout_halfling <= 14)
        
        count_human = count_human/100
        #ideal is 20
        self.assertTrue(15 <= count_human <= 25)
        
        count_tiefling = count_tiefling/100
        #ideal is 4
        self.assertTrue(0 <= count_tiefling <= 9)




if __name__ == '__main__':
    unittest.main()
