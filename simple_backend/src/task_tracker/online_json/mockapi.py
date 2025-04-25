import os

import requests
from dotenv import load_dotenv

load_dotenv()


class MockAPIClient:
    def __init__(self):
        self.base_url = os.getenv("MOCKAPI_URL")
        self.headers = {"Content-Type": "application/json"}

    def get(self):
        response = requests.get(self.base_url, headers=self.headers)
        response.raise_for_status()
        result = response.json()
        if result:
            result = result[0]
            result.pop("id")
        else:
            return {}
        return result

    def update(self, data):
        item_id=1
        if self.get():
            requests.delete(
                f"{self.base_url}/{item_id}",
            )
            response = requests.post(
                f"{self.base_url}",
                json=data,
                headers=self.headers
            )
        else:
            response = requests.post(
                self.base_url,
                json=data,
                headers=self.headers
            )
        response.raise_for_status()
        return data
