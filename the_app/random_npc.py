#right now I'm going to stick the base program in main using lists as 
#main data structures
#SQL and mutliple files to come later


def main():
   print('ok')
   return 



import unittest

class TestMain(unittest.TestCase):
    
    def test_main(self):
        self.assertEqual(None,main())

if __name__ == '__main__':
    unittest.main()
