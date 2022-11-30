from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository
from console_io import ConsoleIO
from app import App


def main():
    reference_repository = ReferenceRepository()
    reference_service = ReferenceService(reference_repository)
    console_io = ConsoleIO()
    app = App(reference_service, console_io)
    app.run()


if __name__ == "__main__":
    main()
