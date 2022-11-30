import unittest
from entities.reference import Reference


class TestReference(unittest.TestCase):
    def setUp(self):
        self.reference = Reference({"key": {
            "author": "Kirjoittaja",
            "name": "Teoksen nimi",
            "year": "Julkaisuvuosi",
            "publisher": "Julkaisija"
        }})

    def test_reference_initialization_works(self):
        self.assertNotEqual(self.reference, None)
