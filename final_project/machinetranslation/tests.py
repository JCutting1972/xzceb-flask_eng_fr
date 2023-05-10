import unittest

from translator import EnglishToFrench
french_result= 'error'
english_text = 'error'
#model_id = 'error'
languages = 'error'




class TestTanslator(unittest.TestCase):
    def test_EnglishToFrench(self):

        english_text = 'Blue'
        languages = 'en-fr'
        french_result = EnglishToFrench('blue','en-fr')
        french_expected = 'Bleu'
        self.assertEqual(EnglishToFrench(english_text,languages),french_expected)
            

if __name__ =='__main__':
      unittest.main()
