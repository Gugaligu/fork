import os

import requests
from dotenv import load_dotenv

load_dotenv()

class CloudflareAISolver:

    def __init__(self):
        self.account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
        self.api_token = os.getenv("CLOUDFLARE_API_TOKEN")
        self.model = "@cf/meta/llama-3.1-8b-instruct"  # Модель по умолчанию
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run"

    def get_solution(self, task_description):
        url = f"{self.base_url}/{self.model}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {"prompt": f"Объясни, как решить эту задачу: {task_description}. Дай ответ:в виде списка в каждом пункте по 10 слов максимум.не более 5 пунктов"}

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json().get("result", {}).get("response")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса к AI: {e}")
            return None
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            return None
