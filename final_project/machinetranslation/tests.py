import unittest

from translator import EnglishToFrench

class TestTanslator(unittest.TestCase):
   def test_EnglishToFrench(self):
        self.assertEqual(EnglishToFrench(('blue'),'bleu'))
            

if __name__ =='__main__':
      unittest.main()
