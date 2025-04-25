import os

import requests
from dotenv import load_dotenv

load_dotenv()

class CloudflareAISolver:
    def __init__(self):
        self.AI_MODEL = os.getenv("AI_MODEL")
        self.CLOUDFLARE_ACCOUNT_ID=os.getenv("CLOUDFLARE_ACCOUNT_ID")
        self.CLOUDFLARE_API_TOKEN=os.getenv("CLOUDFLARE_API_TOKEN")

        self.url = f"https://api.cloudflare.com/client/v4/accounts/{self.CLOUDFLARE_ACCOUNT_ID}/ai/run/{self.AI_MODEL}"

        self.headers = {
            "Authorization": f"Bearer {self.CLOUDFLARE_API_TOKEN}",
            "Content-Type": "application/json"
        }

    def get(self, task_description):

        payload = {"prompt": f"Объясни, как решить эту задачу: {task_description}. Дай ответ:в виде списка в каждом пункте по 10 слов максимум.не более 5 пунктов"}

        try:
            response = requests.post(self.url, json=payload, headers=self.headers, timeout=30)
            response.raise_for_status()
            return response.json()["result"]["response"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса к AI: {e}")
            return None
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            return None
