import unittest

from translator import EnglishToFrench
french_result= 'error'
english_text = 'error'
model_id = 'en-fr'


   # french_result = EnglishToFrench('blue','en-fr')

class TestTanslator(unittest.TestCase):
    def test_EnglishToFrench(self):

    #french_result = EnlishToFrench('blue','en-fr')
        french_result = EnglishToFrench('blue','en-fr')
        french_expected = 'Bleu'
        self.assertEqual(EnglishToFrench('blue','en-fr'),french_expected)
            

if __name__ =='__main__':
      unittest.main()
