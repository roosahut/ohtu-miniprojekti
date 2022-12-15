import unittest
import services.users as users
import services.references as ref


class TestReferences(unittest.TestCase):
    def setUp(self):
        ref.delete_all()
        users.delete_all()
        users.register('tunnus', 'salasana123')
        user = users.find_all()
        self.user_id = user[0][0]

    def test_add_article(self):
        add = ref.add_article(self.user_id, 'avain',
                              'kirjoittaja', 'otsikko', 'julkaisu', 2010, 5)

        self.assertTrue(add)

    def test_add_book(self):
        add = ref.add_book(self.user_id, 'avain',
                           'kirjoittaja', 'otsikko', 'julkaisija', 2010)

        self.assertTrue(add)

    def test_add_inproceedings(self):
        add = ref.add_inproceedings(
            self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)

        self.assertTrue(add)

    def test_add_masterthesis(self):
        add = ref.add_masterthesis(
            self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'koulu', 2010)

        self.assertTrue(add)

    def test_get_articles(self):
        ref.add_article(self.user_id, 'avain', 'kirjoittaja',
                        'otsikko', 'julkaisu', 2010, 5)
        articles = ref.get_articles(self.user_id, 'avain', '')

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, 'otsikko')

    def test_get_books(self):
        ref.add_book(self.user_id, 'avain', 'kirjoittaja',
                     'otsikko', 'julkaisija', 2010)
        books = ref.get_books(self.user_id, 'avain', '')

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'otsikko')

    def test_get_inproceedings(self):
        ref.add_inproceedings(self.user_id, 'avain',
                              'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        inproceedings = ref.get_inproceedings(self.user_id, 'avain', '')

        self.assertEqual(len(inproceedings), 1)
        self.assertEqual(inproceedings[0].title, 'otsikko')

    def test_get_masterthesis(self):
        ref.add_masterthesis(self.user_id, 'avain',
                             'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        masterthesis = ref.get_master_thesis(self.user_id, 'avain', '')

        self.assertEqual(len(masterthesis), 1)
        self.assertEqual(masterthesis[0].title, 'otsikko')

    def test_delete_all(self):
        ref.add_article(self.user_id, 'avain1', 'kirjoittaja',
                        'otsikko', 'julkaisu', 2010, 5)
        ref.add_book(self.user_id, 'avain2', 'kirjoittaja',
                     'otsikko', 'julkaisija', 2010)
        ref.add_inproceedings(self.user_id, 'avain3',
                              'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        ref.add_masterthesis(self.user_id, 'avain4',
                             'kirjoittaja', 'otsikko', 'koulu', 2010)

        ref.delete_all()

        articles = ref.get_articles(self.user_id, '', '')
        books = ref.get_books(self.user_id, '', '')
        inproceedings = ref.get_inproceedings(self.user_id, '', '')
        masterthesis = ref.get_master_thesis(self.user_id, '', '')

        self.assertEqual(len(articles), 0)
        self.assertEqual(len(books), 0)
        self.assertEqual(len(inproceedings), 0)
        self.assertEqual(len(masterthesis), 0)

    def test_check_refkey(self):
        ref.add_article(self.user_id, 'avain', 'kirjoittaja',
                        'otsikko', 'julkaisu', 2010, 5)
        check = ref.check_refkey(self.user_id, 'avain', 'articles')

        self.assertEqual(check[0].ref_key, 'avain')

    def test_find_refkey_within_books(self):
        ref.add_book(self.user_id, 'avain', 'kirjoittaja',
                     'otsikko', 'julkaisija', 2010)
        find = ref.find_refkey(self.user_id, 'avain')

        self.assertTrue(find)

    def test_find_refkey_within_articles(self):
        ref.add_article(self.user_id, 'avain', 'kirjoittaja',
                        'otsikko', 'julkaisu', 2010, 5)
        find = ref.find_refkey(self.user_id, 'avain')

        self.assertTrue(find)

    def test_find_refkey_within_mastersthesis(self):
        ref.add_masterthesis(self.user_id, 'avain',
                             'kirjoittaja', 'otsikko', 'koulu', 2010)
        find = ref.find_refkey(self.user_id, 'avain')

        self.assertTrue(find)

    def test_find_refkey_within_inproceedings(self):
        ref.add_inproceedings(self.user_id, 'avain',
                              'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        find = ref.find_refkey(self.user_id, 'avain')

        self.assertTrue(find)

    def test_find_refkey_with_nonexistent_key(self):
        find = ref.find_refkey(self.user_id, 'avain')

        self.assertFalse(find)

    def test_get_bibtex_forms(self):
        ref.add_article(self.user_id, 'avain1', 'kirjoittaja1',
                        'otsikko1', 'julkaisu1', 2010, 5)
        ref.add_book(self.user_id, 'avain2', 'kirjoittaja2',
                     'otsikko2', 'julkaisija2', 2010)
        ref.add_inproceedings(self.user_id, 'avain3',
                              'kirjoittaja3', 'otsikko3', 'kirjaotsikko3', 2010)
        ref.add_masterthesis(self.user_id, 'avain4',
                             'kirjoittaja4', 'otsikko4', 'koulu4', 2010)

        keys = ['avain1', 'avain2', 'avain3', 'avain4']

        article = [
            "@article{avain1,",
            "    author = {kirjoittaja1},",
            "    title = {otsikko1},",
            "    journal = {julkaisu1},",
            "    year = {2010}",
            "    volume = {5}",
            "}",
            ""
        ]

        book = [
            "@book{avain2,",
            "    author = {kirjoittaja2},",
            "    title = {otsikko2},",
            "    publisher = {julkaisija2},",
            "    year = {2010}",
            "}",
            ""
        ]

        inproceedings = [
            "@inproceedings{avain3,",
            "    author = {kirjoittaja3},",
            "    title = {otsikko3},",
            "    booktitle = {kirjaotsikko3},",
            "    year = {2010}",
            "}",
            ""
        ]

        mastersthesis = [
            "@mastersthesis{avain4,",
            "    author = {kirjoittaja4},",
            "    title = {otsikko4},",
            "    school = {koulu4},",
            "    year = {2010}",
            "}",
            ""
        ]

        bibtex_forms = ref.get_bibtex_forms(self.user_id, keys)

        self.assertEqual(bibtex_forms[0], article)
        self.assertEqual(bibtex_forms[1], book)
        self.assertEqual(bibtex_forms[2], inproceedings)
        self.assertEqual(bibtex_forms[3], mastersthesis)

    def test_add_references_to_file(self):
        ref.add_article(self.user_id, 'avain1', 'kirjoittaja1',
                        'otsikko1', 'julkaisu1', 2010, 5)
        ref.add_book(self.user_id, 'avain2', 'kirjoittaja2',
                     'otsikko2', 'julkaisija2', 2010)
        ref.add_inproceedings(self.user_id, 'avain3',
                              'kirjoittaja3', 'otsikko3', 'kirjaotsikko3', 2010)
        ref.add_masterthesis(self.user_id, 'avain4',
                             'kirjoittaja4', 'otsikko4', 'koulu4', 2010)

        keys = ['avain1', 'avain2', 'avain3', 'avain4']

        write_file = ref.add_references_to_file(self.user_id, keys)

        self.assertTrue(write_file)
