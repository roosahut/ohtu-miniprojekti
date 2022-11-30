from repositories.reference_repository import ReferenceRepository
from services.reference_service import ReferenceService
from stub_io import StubIO
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._reference_repository = ReferenceRepository()
        self._reference_service = ReferenceService(self._reference_repository)
        self.app = App(self._reference_service, self._io)

    def input(self, value):
        self._io.add_input(value)

    def run_application(self):
        self._app.run()

    def output_should_contain(self, value):
        if value not in self._io.outputs:
            raise AssertionError(f'\"{value}\" not in {str(self._io.outputs)}')

    def add_reference(self, reference, author, name, year, publisher):
        reference = {reference: {'author': author,
                                 'name': name, 'year': year, 'publisher': publisher}}
        self._reference_service.add_reference(reference)

    def references_should_contain(self, reference, author, name, year, publisher):
        expected = {reference: {'author': author,
                                'name': name, 'year': year, 'publisher': publisher}}
        all_references = self._reference_service.find_all()
        all_reference_values = [
            reference.values for reference in all_references]
        if expected not in all_reference_values:
            raise AssertionError(
                f"Reference \"{expected}\" is not in {all_reference_values}"
            )
