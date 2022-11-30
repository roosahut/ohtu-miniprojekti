import unittest
from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.reference_service = ReferenceService(ReferenceRepository())
        self.repository = self.reference_service.reference_repository
        self.dict1 = {"viite1": {
            "author": "Kirjoittaja1",
            "name": "Kirja1",
            "year": "2020",
            "publisher": "Julkaisija1"}}
        self.dict2 = {"viite2": {
            "author": "Kirjoittaja2",
            "name": "Kirja2",
            "year": "2022",
            "publisher": "Julkaisija2"}}

    def test_initialization_works(self):
        self.assertNotEqual(self.repository, None)

    def test_adding_one_reference_works(self):
        self.reference_service.add_reference(self.dict1)
        references = self.reference_service.find_all()

        self.assertEqual(len(references), 1)
        self.assertEqual(list(references[0].values.keys())[0], "viite1")

    def test_adding_two_references_works(self):
        self.reference_service.add_reference(self.dict1)
        self.reference_service.add_reference(self.dict2)
        references = self.reference_service.find_all()

        self.assertEqual(len(references), 2)
        self.assertEqual(list(references[1].values.keys())[0], "viite2")

    def test_adding_two_references_with_same_key_raises_an_exception(self):
        self.reference_service.add_reference(self.dict1)

        with self.assertRaises(Exception):
            self.reference_service.add_reference(self.dict1)

    def test_find_all_returns_empty_list_when_no_references_exist(self):
        references = self.reference_service.find_all()

        self.assertEqual(references, [])
