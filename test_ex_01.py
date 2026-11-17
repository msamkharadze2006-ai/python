import unittest
from ex_01_wbt import*


class TestTask1(unittest.TestCase):

    def test_br_to_am_1(self):
        self.assertEqual("color", br_to_am("colour"))
        self.assertEqual("honor", br_to_am("honour"))

    def test_br_to_am_2(self):
        self.assertEqual("behavior", br_to_am("behaviour"))
        self.assertEqual("neighbor", br_to_am("neighbour"))
        self.assertEqual("cut", br_to_am("cut"))
        self.assertEqual("usage", br_to_am("usage"))


class TestTask2(unittest.TestCase):

    def test_pig_latin_1(self):
        self.assertEqual("ordway", pig_latin("word"))
        self.assertEqual("ackJay", pig_latin("Jack"))

    def test_pig_latin_2(self):
        self.assertEqual("aximmay", pig_latin("maxim"))
        self.assertEqual("okyoTay", pig_latin("Tokyo"))


class TestTask3(unittest.TestCase):

    def test_pig_latin_name_1(self):
        self.assertEqual("Ackjay", pig_latin_name("Jack"))

    def test_pig_latin_name_2(self):
        self.assertEqual("Ordway", pig_latin_name("Word"))
        self.assertEqual("Okyotay", pig_latin_name("Tokyo"))

    def test_pig_latin_name_3(self):
        self.assertEqual("Aximmay", pig_latin_name("MaxiM"))

    def test_pig_latin_name_4(self):
        self.assertEqual("Übingentay", pig_latin_name("Tübingen"))
        self.assertEqual("Nna-lenaaay", pig_latin_name("Anna-Lena"))


if __name__ == '__main__':
    unittest.main()
    