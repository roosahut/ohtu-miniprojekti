class App:
    def __init__(self, reference_service, io):
        self.reference_service = reference_service
        self.io = io

    def run(self):
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
        key = self._ask_for_text_loop("Viiteavain: ", "Lisää jokin avain viitteelle, esim. 'abc17' ")
        author = self._ask_for_text_loop("Kirjoittaja: ", "Lisää kirjoittaja viitteelle")
        name = self._ask_for_text_loop("Teoksen nimi: ", "Lisää kirjan nimi")
        year = self._ask_for_year_loop()
        publisher = self._ask_for_text_loop("Julkaisija: ", "Lisää julkaisija")

        return key, author, name, year, publisher

    def _ask_for_text_loop(self, key, exception):
        while True:
            key = self.io.read(key)
            if not key:
                print(exception)
                continue
            if len(key)>150:
                print("Syöte liian pitkä")
                continue
            else:
                return key

    def _ask_for_year_loop(self):
        while True:
            key = self.io.read("Vuosi: ")
            if not key.isdigit():
                print("Ilmoita vuosiluku numeroina")
                continue
            else:
                return key


    def _view_references(self):
        references = self.reference_service.find_all()
        print("\nLisätyt viitteet:")
        for i in references:
            reference = i.values
            print("----------------------")
            print("Viiteavain:",  list(reference.keys())[0])
            print("Kirjoittaja:", list(reference.values())[0]["author"])
            print("Teoksen nimi:", list(reference.values())[0]["name"])
            print("Vuosi:", list(reference.values())[0]["year"])
            print("Julkaisija:", list(reference.values())[0]["publisher"])
            print("----------------------")
