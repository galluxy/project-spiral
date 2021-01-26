#right now I'm going to stick the base program in main using lists as 
#main data structures
#SQL and mutliple files to come later


import random as r

def random_race():
    #will return a random race using the same d100 probability
    #as the spell Ressurection

    return('Human')


def random_first_name(race):
    return('Grumblo')


def random_last_name(race):
    return('McTavish')


#data structures go here
#will use lists in the form of race_first, race_last and pull randomly

#####
def main():
   print('ok')
   return 



import unittest

class TestMain(unittest.TestCase):
    
    def test_main(self):
        self.assertEqual(None,main())

if __name__ == '__main__':
    unittest.main()
