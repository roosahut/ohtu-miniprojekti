class App:
    def __init__(self, reference_service, io):
        self.reference_service = reference_service
        self.io = io

    def run(self):
        self.io.write("Lähdeviiteohjelma")
        while True:
            command = self.io.read(
                "\n> Lisää uusi viite komennolla 'lisaa' \n> Tulosta lisätyt viitteet komennolla 'lue' \n> Sulje ohjelma komennolla 'lopeta'\n\n")

            if command == "lisaa":
                key, author, name, year, publisher = self._read_values()
                reference = {key: {"author": author, "name": name,
                                   "year": year, "publisher": publisher}}

                self.reference_service.add_reference(reference)

            elif command == "lue":
                self._view_references()

            elif command == "lopeta":
                break

            else:
                continue

    def _read_values(self):
        key = self._ask_for_key_loop()
        author = self._ask_for_text_loop("Kirjoittaja", "Lisää kirjoittaja viitteelle")
        name = self._ask_for_text_loop("Teoksen nimi", "Lisää kirjan nimi")
        year = self._ask_for_year_loop()
        publisher = self._ask_for_text_loop("Julkaisija", "Lisää julkaisija")

        return key, author, name, year, publisher

    def _ask_for_text_loop(self, key, exception):
        while True:
            key = self.io.read(key + ": ")
            if not key:
                self.io.write(exception)
                continue
            if len(key) > 150:
                self.io.write("Syöte liian pitkä")
                continue
            else:
                return key

    def _ask_for_key_loop(self):
        while True:
            key = self.io.read("Viiteavain: ")
            if not key:
                self.io.write("Lisää jokin avain viitteelle, esim. 'abc17' ")
                continue
            if self.reference_service.find_by_key(key):
                self.io.write(f'Viite avaimella {key} on jo olemassa, valitse toinen avain!')
                continue
            if len(key) > 10:
                self.io.write("Avaimen kannattaa olla 2-10 merkin pituinen")
                continue
            else:
                return key
        

    def _ask_for_year_loop(self):
        while True:
            key = self.io.read("Vuosi: ")
            if not key.isdigit():
                self.io.write("Ilmoita vuosiluku numeroina")
                continue
            else:
                return key


    def _view_references(self):
        references = self.reference_service.find_all()
        self.io.write("\nLisätyt viitteet:")
        for i in references:
            reference = i.values
            self.io.write("----------------------")
            self.io.write("Viiteavain: " + list(reference.keys())[0])
            self.io.write("Kirjoittaja: " + list(reference.values())[0]["author"])
            self.io.write("Teoksen nimi: " + list(reference.values())[0]["name"])
            self.io.write("Vuosi: " + list(reference.values())[0]["year"])
            self.io.write("Julkaisija: " + list(reference.values())[0]["publisher"])
            self.io.write("----------------------")
