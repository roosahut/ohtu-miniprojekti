import unittest
from repositories.reference_repository import ReferenceRepository
from entities.reference import Reference


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        self.reference_repository = ReferenceRepository()
        self.reference1 = Reference({"viite1": {
            "author": "Kirjoittaja1",
            "name": "Kirja1",
            "year": "2020",
            "publisher": "Julkaisija1"}})
        self.reference2 = Reference({"viite2": {
            "author": "Kirjoittaja2",
            "name": "Kirja2",
            "year": "2022",
            "publisher": "Julkaisija2"}})

    def test_adding_one_reference_works(self):
        self.reference_repository.add_reference(self.reference1)
        references = self.reference_repository.find_all()

        self.assertEqual(len(references), 1)
        self.assertEqual(list(references[0].values.keys())[0], "viite1")

    def test_adding_two_references_works(self):
        self.reference_repository.add_reference(self.reference1)
        self.reference_repository.add_reference(self.reference2)
        references = self.reference_repository.find_all()

        self.assertEqual(len(references), 2)
        self.assertEqual(list(references[1].values.keys())[0], "viite2")

    def test_adding_two_references_with_same_key_raises_an_exception(self):
        self.reference_repository.add_reference(self.reference1)

        with self.assertRaises(Exception):
            self.reference_repository.add_reference(self.reference1)

    def test_find_by_key_works_when_key_exists(self):
        self.reference_repository.add_reference(self.reference1)
        key = self.reference_repository.find_by_key("viite1")

        self.assertEqual(key, "viite1")

    def test_find_by_key_returns_none_when_key_does_not_exist(self):
        self.reference_repository.add_reference(self.reference1)
        key = self.reference_repository.find_by_key("avain")

        self.assertEqual(key, None)

    def test_find_all_returns_empty_list_when_no_references_exist(self):
        references = self.reference_repository.find_all()

        self.assertEqual(references, [])
