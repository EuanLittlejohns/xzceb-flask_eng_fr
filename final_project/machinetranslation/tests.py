import unittest
from translator import french_to_english, english_to_french

class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Hello'), 'Bonjour')
        
class Test_english_to_french(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Bonjour'), 'Hello')
        
unittest.main()