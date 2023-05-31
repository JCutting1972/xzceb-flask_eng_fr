import unittest

from translator import english_to_french
from translator import french_to_english

class TestTanslator(unittest.TestCase):
    def test_english_to_french(self):

        english_text = 'Blue'
       # languages = 'en-fr'
        french_expected = 'Bleu'
        self.assertEqual(english_to_french(english_text),french_expected)

        english_text = 'Red'
        #languages = 'en-fr'
        french_expected = 'Rouge'
        self.assertEqual(english_to_french(english_text),french_expected)
        
        english_text = 'Car'
        #languages = 'en-fr'
        french_expected = 'Voiture'
        self.assertEqual(english_to_french(english_text),french_expected)
        
        english_text = 'Hello'
        #languages = 'en-fr'
        french_expected = 'Bonjour'
        self.assertEqual(english_to_french(english_text),french_expected)

    def test_french_to_english(self):

        french_txt = 'Bleu'
        #languages = 'fr-en'        
        english_expected = 'Blue'
        self.assertEqual(french_to_english(french_txt),english_expected)

        french_txt = 'Rouge'
       # languages = 'fr-en'
        english_expected = 'Red'
        self.assertEqual(french_to_english(french_txt),english_expected)


        french_txt = 'Voiture'
        #languages = 'fr-en'
        english_expected = 'Car'
        self.assertEqual(french_to_english(french_txt),english_expected)


        french_txt = 'Bonjour'
        #languages = 'fr-en'
        english_expected = 'Hello'
        self.assertEqual(french_to_english(french_txt),english_expected)


if __name__ =='__main__':
      unittest.main()
