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
