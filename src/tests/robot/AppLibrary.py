import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password):
        data = {
            "username": username,
            "password1": password,
            "password2": password
        }

        requests.post(f"{self._base_url}/register", data = data)

    def login(self, username, password):
        data = {
            "username": username,
            "password": password
        }

        requests.post(f"{self._base_url}/login", data = data)

    def add_book_reference(self, ref_key, author, title, publisher, year):
        data = {
            "ref_key": ref_key,
            "author": author,
            "title": title,
            "publisher": publisher,
            "year": year
        }

        requests.post(f"{self._base_url}/add_book", data = data)

