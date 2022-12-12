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
        add = ref.add_article(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisu', 2010, 5)
        
        self.assertTrue(add)
        
        
    def test_add_book(self):
        add = ref.add_book(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisija', 2010)
        
        self.assertTrue(add)
        
        
    def test_add_inproceedings(self):
        add = ref.add_inproceedings(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        
        self.assertTrue(add)
        
        
    def test_add_masterthesis(self):
        add = ref.add_masterthesis(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'koulu', 2010)
        
        self.assertTrue(add)
        
        
    def test_get_articles(self):
        ref.add_article(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisu', 2010, 5)
        articles = ref.get_articles(self.user_id)
        
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, 'otsikko')
        
    
    def test_get_books(self):
        ref.add_book(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisija', 2010)
        books = ref.get_books(self.user_id)
        
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'otsikko')
    
    
    def test_get_inproceedings(self):
        ref.add_inproceedings(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        inproceedings = ref.get_inproceedings(self.user_id)
        
        self.assertEqual(len(inproceedings), 1)
        self.assertEqual(inproceedings[0].title, 'otsikko')
        
    
    def test_get_masterthesis(self):
        ref.add_masterthesis(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        masterthesis = ref.get_master_thesis(self.user_id)
        
        self.assertEqual(len(masterthesis), 1)
        self.assertEqual(masterthesis[0].title, 'otsikko')
        
        
    def test_delete_all(self):
        ref.add_article(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisu', 2010, 5)
        ref.add_book(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'julkaisija', 2010)
        ref.add_inproceedings(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        ref.add_masterthesis(self.user_id, 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010)
        
        ref.delete_all()
        
        articles = ref.get_articles(self.user_id)
        books = ref.get_books(self.user_id)
        inproceedings = ref.get_inproceedings(self.user_id)
        masterthesis = ref.get_master_thesis(self.user_id)
        
        self.assertEqual(len(articles), 0)
        self.assertEqual(len(books), 0)
        self.assertEqual(len(inproceedings), 0)
        self.assertEqual(len(masterthesis), 0)


    
    
    