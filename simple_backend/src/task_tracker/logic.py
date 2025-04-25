from ABC_CRUD import BaseCRUD
from DB.json_DB import JSON
from integrate_cloudflare.api_cloudflare import CloudflareAISolver
from online_json.mockapi import MockAPIClient


class TasksCRUD(BaseCRUD):
    @staticmethod
    def get():
        return JSON().get()

    @staticmethod
    def create(task_model):
        task_model.task=task_model.task + "\n" + CloudflareAISolver().get(task_model.task)
        data = JSON().create(task_model.model_dump())
        return data

    @staticmethod
    def update(task_id,task_model):
        task_id = str(task_id)
        data_obj = JSON()
        if task_id in data_obj.get():
            # "" чтобы не делать запрос в нейронку
            if task_model.task.strip() != "":
                task_model.task = task_model.task + "\n" + CloudflareAISolver().get(task_model.task)
            else:
                task_model.task=data_obj.get()[task_id]["task"]
            data_obj.update(task_id, task_model.model_dump())
        return data_obj.get()

    @staticmethod
    def delete(task_id):
        task_id = str(task_id)
        data_obj = JSON()
        data_obj.delete(task_id)
        return data_obj.get()



class TaskCloud:
    @staticmethod
    def local_sync():
        j_obj=JSON()
        cloud_data=MockAPIClient().get()
        j_obj.data_json=cloud_data
        j_obj._save_to_file()
        return j_obj.get()

    @staticmethod
    def cloud_sync():
        local_data=JSON().get()
        result=MockAPIClient().update(local_data)
        return result

