import unittest
import services.users as users
import services.references as ref
import services.bibtex_format as bib


class TestBibtexFormat(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_book_to_bibtex(self):
        book = ['id', 'user_id', 'avain', 'kirjoittaja', 'otsikko', 'julkaisija', 2010]
        
        bibtex = [
            "@book{avain,",
            "    author = {kirjoittaja},",
            "    title = {otsikko},",
            "    publisher = {julkaisija},",
            "    year = {2010}",
            "}",
            ""
        ]
        
        self.assertEqual(bib.book_to_bibtex(book), bibtex)
        
    def test_article_to_bibtex(self):
        article = ['id', 'user_id', 'avain', 'kirjoittaja', 'otsikko', 'julkaisu', 2010, 5]
        
        bibtex = [
            "@article{avain,",
            "    author = {kirjoittaja},",
            "    title = {otsikko},",
            "    journal = {julkaisu},",
            "    year = {2010}",
            "    volume = {5}",
            "}",
            ""
        ]
        
        self.assertEqual(bib.article_to_bibtex(article), bibtex)
        
    def test_inproceedings_to_bibtex(self):
        inproceedings = ['id', 'user_id', 'avain', 'kirjoittaja', 'otsikko', 'kirjaotsikko', 2010]
        bibtex = [
            "@inproceedings{avain,",
            "    author = {kirjoittaja},",
            "    title = {otsikko},",
            "    booktitle = {kirjaotsikko},",
            "    year = {2010}",
            "}",
            ""
        ]
        
        self.assertEqual(bib.inproceedings_to_bibtex(inproceedings), bibtex)
        
    def test_mastersthesis_to_bibtex(self):
        mastersthesis = ['id', 'user_id', 'avain', 'kirjoittaja', 'otsikko', 'koulu', 2010]
        bibtex = [
            "@mastersthesis{avain,",
            "    author = {kirjoittaja},",
            "    title = {otsikko},",
            "    school = {koulu},",
            "    year = {2010}",
            "}",
            ""
        ]
        
        self.assertEqual(bib.masterthesis_to_bibtex(mastersthesis), bibtex)