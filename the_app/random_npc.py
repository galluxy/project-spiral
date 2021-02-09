#right now I'm going to stick the base program in main using lists as 
#main data structures
#SQL and mutliple files to come later


import random as rand

def random_race():
    #will return a random race using the same d100 probability
    #as the spell Reincarnate

    race = rand.choice(race_list)
    return(race)


def random_name(race):

    #some inelegant if checks to find the race
    if race == 'Half-Elf':
        clan = rand.choice(human_clans)
        num = rand.randint(1,2)
        if num == 1:
            return rand.choice(human_first_names[clan]) + ' ' + rand.choice(last_names['Elf'])
        else:
            return rand.choice(first_names['Elf']) + ' ' + rand.choice(human_last_names[clan])
    elif race == 'Half-Orc':
        return rand.choice(first_names[race])
    elif 'Dwarf' in race:
        return rand.choice(first_names['Dwarf']) + ' ' + rand.choice(last_names['Dwarf'])
    elif 'Elf' in race:
        return rand.choice(first_names['Elf']) + ' ' + rand.choice(last_names['Elf'])
    elif 'Halfling' in race:
        return rand.choice(first_names['Halfling']) + ' ' +  rand.choice(last_names['Halfling'])
    elif 'Gnome' in race:
        return rand.choice(first_names['Gnome']) + ' ' + rand.choice(last_names['Gnome']) + ' and nicknamed ' + rand.choice(gnome_nicknames)
    elif race == 'Human':
        clan = rand.choice(human_clans)
        return rand.choice(human_first_names[clan]) + ' ' + rand.choice(human_last_names[clan])
    elif race == 'Tiefling':
        return rand.choice(first_names[race])
    else:
        #dragonborn
        return rand.choice(first_names[race]) + ' ' + rand.choice(last_names[race])
    




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
             'Human','Human','Human','Human','Tiefling','Tiefling','Tiefling','Tiefling']


####Name nested dicts####

first_names = {'Dragonborn':
               #male names
               ['Arjhan','Balasar','Bharash','Donaar','Ghesh','Heskan','Kriv','Medrash',
                'Mehen','Nadarr','Panjed','Patrin','Rhogar','Shamash','Shedinn','Tarhun','Torinn',
                #female names
                'Akra','Biri','Daar','Farideh','Harann','Havilar','Jheri','Kava','Korinn',
                'Mishann','Nala','Perra','Raiann','Sora','Surina','Thava','Uadjit'],
               
               'Dwarf' :
               #male names
               ['Adrik','Alberich','Baern','Barendd','Brottor','Bruenor','Dain','Darrak','Delg',
                'Eberk','Einkil','Fargrim','Flint','Gardain','Harbek','Kildrak','Morgran','Orsik',
                'Oskar','Rangrim','Rurik','Taklinn','Thoradin','Thorin','Tordek','Traubon',
                'Travok','Ulfgar','Veit','Vondal',
               #female names
               'Amber','Artin','Audhild','Bardryn','Dagnal','Diesa','Eldeth','Falkrunn','Finellen',
                'Gunnloda','Gurdis','Helja','Hlin','Kathra','Kirstryd','Ilde','Liftrasa','Mardred',
                'Riswynn','Sannl','Torbera','Torgga','Vistra'],
               
               'Elf' :
               #adult male names
               ['Adran','Aelar','Aramil','Arannis','Aust','Beiro','Berrian','Carric','Enialis','Erdan',
                'Erevan','Galinndan','Hadarai','Heian','Himo','Immeral','Ivellios','Laucian','Mindartis',
                'Paelias','Peren','Quarion','Riardon','Rolen','Soveliss','Thamior','Tharivol',
                'Theren','Varis',
               #adult female names
               'Adrie','Althaea','Anastrianna','Andraste','Antinua','Bethrynna','Birel','Caelynn',
                'Drusilia','Enna','Felosial','Ielenia','Jelenneth','Keyleth','Leshanna','Lia',
                'Meriele','Mialee','Naivara','Quelenna','Quillathe','Sariel','Shanairra','Shava',
                'Silaqui','Theirastra','Thia','Vadania','Valanthe','Xanaphia'],
               
               'Gnome' :
               #male names
               ['Alston','Alvyn','Boddynock','Brocc','Burgell','Dimble','Eldon','Erky','Fonkin',
                'Frug','Gerbo','Gimble','Glim','Jebeddo','Kellen','Namfoodle','Orryn',
                'Roondar','Seebo','Sindri','Warryn','Wrenn','Zook',
                #female names
                'Bimpnottin','Breena','Caramip','Carlin','Donella','Duvamil','Ella','Ellyjobell',
                'Ellywick','Lilli','Loopmottin','Lorilla','Mardnab','Nissa','Nyx','Oda',
                'Orla','Roywyn','Shamil','Tana','Waywocket','Zanna'
                ],
               
               'Half-Orc' :
               #male names
               ['Dench','Feng','Gell','Henk','Holg','Imsh','Keth','Krusk','Mhurren','Ront','Shump','Thokk',
                #female names
                'Baggi','Emen','Engong','Kansif','Myev','Neega','Ovak','Ownka','Shautha','Sutha','Vola','Volen','Yevelda'
                   ],
               
               'Halfling' :
               #male names
               ['Alton','Ander','Cade','Corrin','Eldon','Errich','Finnan','Garret','Lindal','Lyle',
                'Merric','Milo','Osborn','Perrin','Reed','Roscoe','Wellby',
                #female names
                'Andry','Bree','Callie','Cora','Euphemia','Jillian','Kithri','Lavinia','Lidda','Merla',
                'Nedda','Paela','Portia','Seraphina','Shaena','Trym','Vani','Verna'],
               
               'Tiefling' :
               #male names
               ['Akmenos','Amnon','Barakas','Damakos','Ekemon','Iados','Kairon','Leucis','Melech',
                'Mordai','Morthos','Pelaios','Skamos','Therai',
               #female names
                'Akta','Anakis','Bryseis','Criella','Damaia','Ea','Kallista','Lerissa','Makaria',
                'Nemeia','Orianna','Phelaia','Rieta',
               #virtue names
                'Art','Carrion','Chant','Creed','Despair','Excellence','Fear','Glory','Hope','Ideal',
                'Music','Nowhere','Open','Poetry','Quest','Random','Reverence','Sorrow','Temerity',
                'Torment','Weary']
                               }

last_names = {'Dragonborn':
              ['Clethtinthiallor','Daardendrian','Delmirev','Drachedandion','Fenkenkabradon',
               'Kepeshkmolik','Kerrhylon','Kimbatuul','Linxakasendalor','Myastan','Nemmonis',
               'Norixius','Ophinshtalajirr','Prexijandilin','Shestendeliath','Turnuroth',
               'Verthisathurgiesh','Yarjerit'],
              
               'Dwarf' :
              ['Balderk','Battlehammer','Brawnanvil','Dankil','Fireforge','Frostbeard',
                          'Gorunn','Holderhek','Ironfist','Loderr','Lutgehr','Rumnaheim',
                          'Strakeln','Torunn','Ungart'],
              
               'Elf' :
              ['Amakiir','Amastacia','Galanodel','Holimion','Ilphelkiir','Liadon',
                        'Meliamne','Nailo','Siannodel','Xiloscient'],
              
               'Gnome' :
              ['Beren','Daergel','Folkor','Garrick','Nackle','Murnig','Ningel','Raulnor','Scheppen',
               'Timbers','Turen'],
              
               'Halfling' :
              ['Brushgather','Goodbarrel','Greenbottle','High-hill','Hilltopple','Leagallow','Tealeaf',
               'Thorngage','Tosscobble','Underbough'],
              }

gnome_nicknames = ['Aleslosh','Ashhearth','Badger','Cloak','Doublelock','Flichbatter','Fnipper','Ku','Nim',
                   'Oneshoe','Pock','Sparklegem','Stumbleduck']

#Humans

human_clans = ['Calishite','Chondathan','Damaran','Illuskan','Mulan','Rashemi','Shou','Turami']

human_first_names = {'Calishite' :
                     #male names
                     ['Aseir','Bardeid','Haseid','Khemed','Mehmen','Sudeiman','Zasheir',
                      #female names
                      'Atala','Ceidil','Hama','Jasmal','Meilil','Seipora','Yasheira','Zasheida'],
                     'Chondathan' :
                     #male names
                     ['Darvin','Dorn','Evendur','Gorstag','Grim','Helm','Malark','Morn','Randal','Stedd',
                      #female names
                      'Arveene','Esvele','Jhessail','Kerri','Lureene','Miri','Rowan','Shandri','Tessele'],
                     'Damaran' :
                     #male names
                     ['Bor','Fodel','Glar','Grigor','Igan','Ivor','Kosef','Mival','Orel','Pavel','Sergor',
                      #female names
                      'Aethra','Kara','Katernin','Mara','Natali','Olma','Tana','Zora'],
                     'Illuskan' :
                     #male names
                     ['Ander','Blath','Bran','Frath','Geth','Lander','Luth','Malcer','Stor','Taman','Urth',
                      #female names
                      'Amafrey','Betha','Cefrey','Kethra','Mara','Olga','Silifrey','Westra'],
                     'Mulan' :
                     #male names
                     ['Aoth','Bareris','Ehput-Ki','Kethoth','Mumed','Ramas','So-Kehur','Thazar-De','Urhur',
                      #female names
                      'Arizima','Chathi','Nephis','Nulara','Murithi','Sefris','Thola','Umara','Zolis'],
                     'Rashemi' :
                     #male names
                     ['Borivik','Faurgar','Jandar','Kanithar','Madislak','Ralmevik','Shaumar','Vladislak',
                      #female names
                      'Fyevarra','Hulmarra','Immith','Imzel','Navarra','Shevarra','Tammith','Yuldra'],
                     'Shou' :
                     #male names
                     ['An','Chen','Chi','Fai','Jiang','Jun','Lian','Long','Meng','On','Shan','Shui','Wen',
                      #female names
                      'Bai','Chao','Jia','Lei','Mei','Qiao','Shui','Tai'],
                     'Turami' :
                     #male names
                     ['Anton','Diero','Marcon','Pieron','Rimardo','Romero','Salazar','Umbero',
                      #female names
                      'Balama','Dona','Faila','Jalana','Luisa','Marta','Quara','Selise','Vonda']}

human_last_names = {'Calishite' :
                    ['Basha','Dumein','Jassan','Khalid','Mostana','Pashar','Rein'],
                    'Chondathan' :
                    ['Amblecrown','Buckman','Dundragon','Evenwood','Greycastle','Tallstag'],
                    'Damaran' :
                    ['Bersk','Chernin','Dotsk','Kulenov','Marsk','Nemetsk','Shemov','Starag'],
                    'Illuskan' :
                    ['Brightwood','Helder','Hornraven','Lackman','Stormwind','Windrivver'],
                    'Mulan' :
                    ['Ankhalab','Anskuld','Fezim','Hahpet','Nathandem','Sepret','Uuthrakt'],
                    'Rashemi' :
                    ['Chergoba','Dyernina','Iltazyara','Murnyethara','Stayanoga','Ulkmokina'],
                    'Shou' :
                    ['Chien','Huang','Kao','Kung','Lao','Ling','Mei','Pin','Shin','Sum','Tan','Wan'],
                    'Turami' :
                    ['Agosto','Astorio','Calabra','Domine','Falone','Marivaldi','Pisacar','Ramondo']}



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
