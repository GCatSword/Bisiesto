import unittest
import bisiesto

class BisiestoTest(unittest.TestCase):

    def test_divisible_entre4(self):
        self.assertEqual(bisiesto.anno_bisiesto(2004), 'Es un año bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(2008), 'Es un año bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(2005), 'No es bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(333), 'No es bisiesto')

    def test_divisible_excepto100(self):

        self.assertEqual(bisiesto.anno_bisiesto(2100), 'No es bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(2200), 'No es bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(3000), 'No es bisiesto')

    def test_divisible_excepto400(self):

        self.assertEqual(bisiesto.anno_bisiesto(2000), 'Es un año bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(2400), 'Es un año bisiesto')
        self.assertEqual(bisiesto.anno_bisiesto(2800), 'Es un año bisiesto')

if __name__ == '__main__':
    unittest.main()