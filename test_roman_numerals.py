import unittest

from roman_numerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):
    def test_1(self):
        expected = 'I'
        actual = RomanNumerals(1).get_value()
        self.assertEqual(expected, actual)

    def test_3(self):
        expected = 'III'
        actual = RomanNumerals(3).get_value()
        self.assertEqual(expected, actual)

    def test_4(self):
        expected = 'IV'
        actual = RomanNumerals(4).get_value()
        self.assertEqual(expected, actual)

    def test_5(self):
        expected = 'V'
        actual = RomanNumerals(5).get_value()
        self.assertEqual(expected, actual)

    def test_6(self):
        expected = 'VI'
        actual = RomanNumerals(6).get_value()
        self.assertEqual(expected, actual)

    def test_8(self):
        expected = 'VIII'
        actual = RomanNumerals(8).get_value()
        self.assertEqual(expected, actual)

    def test_9(self):
        expected = 'IX'
        actual = RomanNumerals(9).get_value()
        self.assertEqual(expected, actual)

    def test_10(self):
        expected = 'X'
        actual = RomanNumerals(10).get_value()
        self.assertEqual(expected, actual)

    def test_30(self):
        expected = 'XXX'
        actual = RomanNumerals(30).get_value()
        self.assertEqual(expected, actual)

    def test_40(self):
        expected = 'XL'
        actual = RomanNumerals(40).get_value()
        self.assertEqual(expected, actual)

    def test_50(self):
        expected = 'L'
        actual = RomanNumerals(50).get_value()
        self.assertEqual(expected, actual)

    def test_60(self):
        expected = 'LX'
        actual = RomanNumerals(60).get_value()
        self.assertEqual(expected, actual)

    def test_80(self):
        expected = 'LXXX'
        actual = RomanNumerals(80).get_value()
        self.assertEqual(expected, actual)

    def test_90(self):
        expected = 'XC'
        actual = RomanNumerals(90).get_value()
        self.assertEqual(expected, actual)

    def test_100(self):
        expected = 'C'
        actual = RomanNumerals(100).get_value()
        self.assertEqual(expected, actual)

    def test_300(self):
        expected = 'CCC'
        actual = RomanNumerals(300).get_value()
        self.assertEqual(expected, actual)

    def test_400(self):
        expected = 'CD'
        actual = RomanNumerals(400).get_value()
        self.assertEqual(expected, actual)

    def test_500(self):
        expected = 'D'
        actual = RomanNumerals(500).get_value()
        self.assertEqual(expected, actual)

    def test_600(self):
        expected = 'DC'
        actual = RomanNumerals(600).get_value()
        self.assertEqual(expected, actual)

    def test_800(self):
        expected = 'DCCC'
        actual = RomanNumerals(800).get_value()
        self.assertEqual(expected, actual)

    def test_900(self):
        expected = 'CM'
        actual = RomanNumerals(900).get_value()
        self.assertEqual(expected, actual)

    def test_1000(self):
        expected = 'M'
        actual = RomanNumerals(1000).get_value()
        self.assertEqual(expected, actual)

    def test_3000(self):
        expected = 'MMM'
        actual = RomanNumerals(3000).get_value()
        self.assertEqual(expected, actual)

    def test_3999(self):
        expected = 'MMMCMXCIX'
        actual = RomanNumerals(3999).get_value()
        self.assertEqual(expected, actual)

