class ReferenceRepository:
    def __init__(self):
        self.references = []

    def add_reference(self, reference):
        existing = self.find_by_key(reference.values.key)
        if existing:
            raise Exception(
                f'Viite avaimella {reference.values.key} on jo olemassa')

        self.references.append(reference)

        return reference

    def find_by_key(self, key):
        references_with_key = [
            reference.values.key for reference in self.references if reference.values.key == key]

        if references_with_key > 0:
            return references_with_key[0]

        return None

    def find_all(self):
        return self.references
