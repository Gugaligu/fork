import os

import requests
from dotenv import load_dotenv


load_dotenv()

class MockAPIClient:
    def __init__(self):
        self.base_url = os.getenv("MOCKAPI_URL")
        self.headers = {"Content-Type": "application/json"}

    def get_all(self):
        response = requests.get(self.base_url, headers=self.headers)
        _json=response.json()[0]
        del _json["id"]
        response.raise_for_status()
        return _json

    def new_json(self, data):
        try:
            self._delete()        #переделать если пустое то ненадо удалять
        except requests.exceptions.HTTPError:
             print("нечего удалять")
        response = requests.post(
            self.base_url,
            json=data,
            headers=self.headers
        )
        _json = response.json()
        del _json["id"]
        response.raise_for_status()
        return _json

    def _delete(self):
        response = requests.delete(
            f"{self.base_url}/{1}",
            headers=self.headers
        )
        response.raise_for_status()
        return True
