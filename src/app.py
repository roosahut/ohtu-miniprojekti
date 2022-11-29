class App:
    def __init__(self, reference_service, io):
        self.reference_service = reference_service
        self.io = io

    def run(self):
        while True:
            command = self.io.read("Kirjoita lisää lisätäksesi viitteen ja lue lukeaksesi viitteet: ")
        
            if command == "lisää":
                reference, author, name, year, publisher = self._read_credentials()
                reference = {reference: {"author": author, "name": name, "year": year, "publisher": publisher}}

                self.reference_service.add_reference(reference)
            
            elif command == "lue":
                self._view_references()

            else:
                continue
    
    def _read_credentials(self):
        reference = self.io.read("Viite: ")
        writer = self.io.read("Kirjoittaja: ")
        name = self.io.read("Nimi: ")
        year = self.io.read("Vuosi: ")
        author = self.io.read("Julkaisija: ")
        
        return reference, writer, name, year, author
    
    def _view_references(self):
        references = self.reference_service.find_all()
        for i in references:
            reference = i.values
            print("----------------------")
            print("Viite:",  list(reference.keys())[0])
            print("Kirjailija:", list(reference.values())[0]["author"])
            print("Kirjan nimi:", list(reference.values())[0]["name"])
            print("Vuosi:", list(reference.values())[0]["year"])
            print("Julkaisija:", list(reference.values())[0]["publisher"])
            print("----------------------")