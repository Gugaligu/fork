import json
from pathlib import Path

from ABC_CRUD import BaseCRUD


class JSON(BaseCRUD):
    _instance = None

    def __new__(cls, name=r"DB\JSON_TASK_DB.json", *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name

            # Создаем файл, если его нет
            if not Path(name).exists():
                with open(name, 'w', encoding="utf-8") as file:
                    json.dump({}, file)
            # Загружаем данные из файла в память
            with open(name, encoding="utf-8") as file:
                cls._instance.data_json = json.load(file)

        return cls._instance

    def get(self):
        return self.data_json

    def create(self, data:dict):
        new_id = str(len(self.data_json) + 1)
        self.data_json[new_id] = data
        self._save_to_file()
        return self.data_json

    def update(self, task_id:str, data:dict):
        if task_id in self.data_json:
            self.data_json[task_id]=data
            self._save_to_file()
        return self.data_json

    def delete(self, task_id:str):
        if task_id in self.data_json:
            del self.data_json[task_id]
            # Перенумеровываем
            self.data_json = {
                str(new_id): self.data_json[old_id]
                for new_id, old_id in enumerate(self.data_json.keys(),start=1)
            }
            self._save_to_file()
        return self.data_json

    def _save_to_file(self):
        with open(self.name, "w", encoding="utf-8") as file:
            json.dump(self.data_json, file, indent=4, ensure_ascii=False)
