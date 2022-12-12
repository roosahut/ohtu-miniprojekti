def book_to_bibtex(book):
    bibtex = f'@book{{{book[2]}, author = \"{book[3]}\", title = \"{book[4]}\", publisher = \"{book[5]}\", year = {book[6]}}}'
    return bibtex
