class ReferenceRepository:
    def __init__(self):
        self.references = []

    def create_reference(self, reference):
        existing = self.find_by_key(reference.key)
        if existing:
            raise Exception(f'Viite avaimella {reference.key} on jo olemassa')

        self.references.append(reference)

        return reference

    def find_by_key(self, key):
        references_with_key = [
            reference.key for reference in self.references if reference.key == key]

        if references_with_key > 0:
            return references_with_key[0]

        return None

    def find_all(self):
        return self.references
