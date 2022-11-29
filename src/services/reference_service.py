from entities.reference import Reference


class ReferenceService:
    def __init__(self, repository):
        self.reference_repository = repository

    def add_reference(self, values: dict):
        reference = self.reference_repository.add_reference(Reference(values))

        return reference
    
    def find_all(self):
        return self.reference_repository.find_all()
