def book_to_bibtex(book):
    bibtex = [
        "@book{" + book[2] + ",",
        "    author = {" + book[3] + "},",
        "    title = {" + book[4] + "},",
        "    publisher = {" + book[5] + "},",
        "    year = {" + str(book[6]) + "}",
        "}",
        ""
    ]
    return bibtex


def article_to_bibtex(article):
    bibtex = [
        "@article{" + article[2] + ",",
        "    author = {" + article[3] + "},",
        "    title = {" + article[4] + "},",
        "    journal = {" + article[5] + "},",
        "    year = {" + str(article[6]) + "}",
        "    volume = {" + str(article[7]) + "}",
        "}",
        ""
    ]
    return bibtex


def inproceedings_to_bibtex(inproceeding):
    bibtex = [
        "@inproceeding{" + inproceeding[2] + ",",
        "    author = {" + inproceeding[3] + "},",
        "    title = {" + inproceeding[4] + "},",
        "    booktitle = {" + inproceeding[5] + "},",
        "    year = {" + str(inproceeding[6]) + "}",
        "}",
        ""
    ]
    return bibtex


def masterthesis_to_bibtex(masterthesis):
    bibtex = [
        "@masterthesis{" + masterthesis[2] + ",",
        "    author = {" + masterthesis[3] + "},",
        "    title = {" + masterthesis[4] + "},",
        "    school = {" + masterthesis[5] + "},",
        "    year = {" + str(masterthesis[6]) + "}",
        "}",
        ""
    ]
    return bibtex
