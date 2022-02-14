import unittest

from romanos import arab_a_roman_mayor, arabigo_a_romano, roman_a_arab_mayor,  romano_a_arabigo, RomanError


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
        with self.assertRaises(ValueError):
            arabigo_a_romano(0)
            

    

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
        with self.assertRaises(RomanError):
            romano_a_arabigo('XXIIV')

        self.assertEqual(romano_a_arabigo('XXIII'), 23)

    def test_romano_a_arabigo_restas_prohibidas(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('XIC')    
        self.assertEqual(romano_a_arabigo('XIV'), 14)

        with self.assertRaises(RomanError):
            romano_a_arabigo('XD')

    def test_romano_a_arabigo_validaciones(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('SED')
        with self.assertRaises(RomanError):
            romano_a_arabigo('IK')
        with self.assertRaises(RomanError):
            romano_a_arabigo('KI')

    def test_romano_a_arabigo_minusculas(self):
        self.assertEqual(romano_a_arabigo('xli'),41)

    def test_arabigo_a_romano_mayor_de_3999(self):
        self.assertEqual(arab_a_roman_mayor(5430),'(V)CDXXX')
        self.assertEqual(arab_a_roman_mayor(234567),'(CCXXXIV)DLXVII')
        self.assertEqual(arab_a_roman_mayor(1234567),'((I)CCXXXIV)DLXVII')
        self.assertEqual(arabigo_a_romano(1234567),'((I)CCXXXIV)DLXVII')
        self.assertEqual(arabigo_a_romano(1234561232),'(((I)CCXXXIV)DLXI)CCXXXII')

    
    def test_romano_a_arabigo_mayor_de_3999(self):
        self.assertEqual(roman_a_arab_mayor('(V)CDXXX'),5430)
        self.assertEqual(roman_a_arab_mayor('(CCXXXIV)DLXVII'), 234567)
        self.assertEqual(roman_a_arab_mayor('(((I)CCXXXIV)DLXI)CCXXXII'), 1234561232)