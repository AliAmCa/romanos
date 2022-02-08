import unittest

from romanos import arabigo_a_romano,  romano_a_arabigo, RomanError


class RomanosFuncionesTest(unittest.TestCase):
    def test_arabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(36), 'XXXVI')

    def test_arabigo_a_romano_con_restas(self):
        self.assertEqual(arabigo_a_romano(464), 'CDLXIV')

    def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabigo_a_romano('lolailo')


    def test_arabigo_a_romano_solo_enteros_positivos(self):
        with self.assertRaises(ValueError):
            arabigo_a_romano(-23)
            

    

class RomanosFuncionesDeRomanoTest(unittest.TestCase):
    def test_romano_a_arabigo_sin_restas(self):
        self.assertEqual(romano_a_arabigo('XXXVI'), 36)

    def test_romano_a_arabigo_con_restas(self):
        self.assertEqual(romano_a_arabigo('MMCDXLIII'), 2443)

    def test_romano_a_arabigo_tres_repeticiones_ok(self):
        self.assertEqual(romano_a_arabigo('III'), 3)

    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('VVIII')

    def test_romano_a_arabigo_dos_repeticiones_de_VLD_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('VV')
        with self.assertRaises(RomanError):
            romano_a_arabigo('DD')
        with self.assertRaises(RomanError):
            romano_a_arabigo('LL')

    def test_romano_a_arabigo_VLD_no_restan(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('VX')
        with self.assertRaises(RomanError):
            romano_a_arabigo('LC')
        with self.assertRaises(RomanError):
            romano_a_arabigo('DM')
            
    def test_romano_a_arabigo_tras_repeticion_no_se_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('XXL')
        

            

'''


from romanos import arabigo_a_romano,  romano_a_arabigo

print(arabigo_a_romano(36)) #XXXVI
print(arabigo_a_romano(46)) #XLVI

print(romano_a_arabigo('XXXVI'))#36
print(romano_a_arabigo('XLVI'))#46
print(romano_a_arabigo('MMCDXLIII'))#2443
print(romano_a_arabigo('MMMMM'))
'''